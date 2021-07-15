import numpy
import numpy as np
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
# import argparse
import imutils
import dlib
import cv2
import math
import pyttsx3

import main_window


def mouth_aspect_ratio(mouth):
	# compute the euclidean distances between the two sets of
	# vertical mouth landmarks (x, y)-coordinates
	A = dist.euclidean(mouth[2], mouth[10]) # 51, 59
	B = dist.euclidean(mouth[4], mouth[8]) # 53, 57

	# compute the euclidean distance between the horizontal
	# mouth landmark (x, y)-coordinates
	C = dist.euclidean(mouth[0], mouth[6]) # 49, 55

	# compute the mouth aspect ratio
	mar = (A + B) / (2.0 * C)

	return mar

# define one constants, for mouth aspect ratio to indicate open mouth
MOUTH_AR_THRESH = 0.73

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# grab the indexes of the facial landmarks for the mouth
(mStart, mEnd) = (49, 68)
speaker = pyttsx3.init()
IF_Speaker = 0

def real_time_detect():

	# start the video stream thread
	print("[INFO] starting video stream thread...")
	# vs = VideoStream(src=0).start()
	cap = cv2.VideoCapture(0)
	cap.set(3,640)

	# time.sleep(1.0)

	frame_width = 640
	frame_height = 480
	write_flag = False


	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	out = cv2.VideoWriter('raw/output.mp4', fourcc, 25.0, (640,480)) 

	speakingFrame = []

	res = ["","",""]
	cur_text=""

	def voice_box__clicked():
		voice_box = mainWindow.ui.checkBox
		global IF_Speaker
		if voice_box.isChecked():
			voice_box.setText("Speaker")
			print("Speaker On")
			IF_Speaker = 1
		else:
			voice_box.setText("Speaker")
			print("Speaker Off")
			IF_Speaker = 0

	def item_clicked(item):
		# print(item, str(item.text()))
		nonlocal cur_text
		split = item.text().split()
		if (len(split) == 2):
			temp_text = item.text().split()[1]
			cur_text = cur_text + temp_text + "\n"
			mainWindow.ui.plainTextEdit.setPlainText(cur_text)
			if(IF_Speaker):
				# pyttsx3.speak(temp_text)
				speaker.say(temp_text)
				speaker.runAndWait()

	mainWindow.ui.listWidget.itemClicked.connect(item_clicked)
	# mainWindow.ui.listWidget.item(0).setSizeHint(100.50)

	mainWindow.ui.checkBox.stateChanged.connect(voice_box__clicked)

	# loop over frames from the video stream
	while cap.isOpened():
		# grab the frame from the threaded video file stream, resize
		# it, and convert it to grayscale
		# channels)
		ret,frame = cap.read()


		# frame = imutils.resize(frame, width=640)
		# print(frame.shape)

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# detect faces in the grayscale frame
		rects = detector(gray, 0)
		mar=-1
		for rect in rects:
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)

			mouth = shape[mStart:mEnd]

			mouthMAR = mouth_aspect_ratio(mouth)
			mar = mouthMAR
			mouthShape = cv2.convexHull(mouth)
			# mouthHull = cv2.boundingRect(mouthShape)
			x, y, w, h = cv2.boundingRect(mouthShape)

			
			# cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			# cv2.drawContours(frame, [mouthShape], -1, (0, 255, 0), 1)
			cv2.putText(frame, "Recording..." if write_flag else "Press Space Key to Start Recording", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			cv2.putText(frame, "MAR: {:.2f}".format(mar), (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

			if mar > MOUTH_AR_THRESH:
				cv2.putText(frame, "Mouth is Open!", (30, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)
				
			

		mainWindow.setImg(frame)
		# cv2.imshow("Frame", frame)

		key = cv2.waitKey(1) & 0xFF

		if write_flag:
			# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

			out.write(frame)
			if mar > MOUTH_AR_THRESH:
				speakingFrame.append(1)
			else:
				speakingFrame.append(0)

		if(mainWindow.isRecording==False and write_flag == True):
			# frame=np.array(frame)*0.4
			# frame=np.rint(frame)
			tmpFrame=frame.copy()
			cv2.line(frame, (0, 260), (640, 300), (50, 50, 50), 100)
			frame=cv2.addWeighted(frame,0.5,tmpFrame,0.5,0)
			cv2.putText(frame, "Processing...", (120, 280), cv2.FONT_HERSHEY_SIMPLEX,1.5, (50, 50, 200), 4)

			mainWindow.setImg(frame)
			mainWindow.ui.control_bt.setText("Processing")
			cv2.waitKey(1)
			out.release()
			duration, start, end = get_duration(speakingFrame)
			crop(start, end)

			from main_visual import LipRead
			res = LipRead("data")
			# print(res)
			mainWindow.ui.listWidget.item(0).setText("1. "+res[0])
			mainWindow.ui.listWidget.item(1).setText("2. "+res[1])
			mainWindow.ui.listWidget.item(2).setText("3. "+res[2])


			speakingFrame = []
			out = cv2.VideoWriter('raw/output.mp4', fourcc, 25.0, (640, 480))

			mainWindow.ui.control_bt.setText("Start")

		write_flag = mainWindow.isRecording

		# if key == 27:
		# 	break

	cv2.destroyAllWindows()
	# vs.stop()
	out.release()
	
	return speakingFrame



def get_duration(speakingFrame):
	# fvs = FileVideoStream('output.mp4').start()
	# time.sleep(1.0)
	fvs = cv2.VideoCapture('raw/output.mp4')
	print(fvs.get(cv2.CAP_PROP_FRAME_COUNT))
	start_time = 0.0
	isStart = False
	end_time = 0.0
	start_frame = 0
	end_frame = 0
	ret, frame = fvs.read()
	cnt = 0
	while ret:
		frame = imutils.resize(frame, width=640)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		rects = detector(gray, 0)

		for rect in rects:

			if speakingFrame[cnt] and isStart == False:
				start_time = fvs.get(cv2.CAP_PROP_POS_MSEC)
				start_frame = cnt + 1
				isStart = True
			
			if speakingFrame[cnt-1] and isStart:
				end_time = fvs.get(cv2.CAP_PROP_POS_MSEC)
				end_frame = cnt + 1


		cnt += 1
		

		ret, frame = fvs.read()

	if end_frame == 0:
		end_frame = start_frame + 28

	# start_time = start_time / 1000.00
	# end_time = end_time / 1000.00
	# print(start_time, end_time)
	
	
	duration_frame = end_frame - start_frame + 1
	# duration = end_time - start_time
	duration = duration_frame / 25.0
	
	if duration_frame % 2 == 0:
		duration_frame += 1
	# print(duration_frame)
	frame_1 = start_frame - ((29 - duration_frame) // 2)
	frame_2 = end_frame + ((29 - duration_frame) // 2) + 1

	info = open('data/output.txt', 'w')
	info.write('Duration: ' + str(duration) + ' seconds')
	info.close()

	print('***')
	print(duration_frame, duration, frame_1, frame_2)
	return duration, frame_1, frame_2

def crop(start, end):
	print('[INFO]Preprocessing recording video...')
	fvs = cv2.VideoCapture('raw/output.mp4')
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	out = cv2.VideoWriter('data/output.mp4', fourcc, 25.0, (96,96),True)
	ret, frame = fvs.read()
	isFix = (start < 0)
	cnt = 1
	detect = True
	x, y, w, h = 0, 0, 0, 0
	# print(ret)
	while ret:
		frame = imutils.resize(frame, width=640)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		rects = detector(gray, 0)

		for rect in rects:
			# print('test')
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)
			mouth = shape[mStart:mEnd]

			if detect == True:
				mouthShape = cv2.convexHull(mouth)
				x, y, w, h = cv2.boundingRect(mouthShape)
				
				detect = False
				# cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

		if isFix:
			cropFrame = frame[y-50:y+w+50, x-40:x+w+40]
			cropFrame = cv2.resize(cropFrame, (96,96), cv2.INTER_LINEAR)
			for i in range (1, 0-start):
				out.write(cropFrame)
			isFix = False
			

		if cnt >= start and cnt <= end:
			# shape = predictor(gray, rect)
			# shape = face_utils.shape_to_np(shape)
			# mouth = shape[mStart:mEnd]
			# print(x, y, w, h)
			# cropFrame = frame[y-25:y+w+25, x-30:x+w+30]
			cropFrame = frame[y-50:y+w+50, x-40:x+w+40]
			cropFrame = cv2.resize(cropFrame, (96,96), cv2.INTER_LINEAR)
			out.write(cropFrame)	

		cnt += 1

		ret, frame = fvs.read()
	out.release()
	# print(x, y, w, h)

def new_crop():
	fvs = cv2.VideoCapture('raw/output.mp4')
	length = fvs.get(cv2.CAP_PROP_FRAME_COUNT)
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	out = cv2.VideoWriter('data/output.mp4', fourcc, 25.0, (96,96),True)
	print('Frames count: ', length)
	ret, frame = fvs.read()
	x, y, w, h = 0, 0, 0, 0
	cnt = 1

	isShort = length < 29

	if isShort:
		fix_len = (29 - length) / 2
	else:
		fix_len = (length - 29) / 2
		

	while ret:
		frame = imutils.resize(frame, width=640)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		rects = detector(gray, 0)

		for rect in rects:
			# print('test')
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)
			mouth = shape[mStart:mEnd]

			if detect == True:
				mouthShape = cv2.convexHull(mouth)
				x, y, w, h = cv2.boundingRect(mouthShape)
				
				detect = False
				# cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

		if isShort:
			if cnt == 1:
				fixFrame = frame[y-50:y+w+50, x-40:x+w+40]
				fixFrame = cv2.resize(fixFrame, (96,96), cv2.INTER_LINEAR)
				for i in range (1, math.floor(fix_len)):
					out.write(fixFrame)
		else:
			# TODO: compression
			pass

		# if cnt >= start and cnt <= end:
		# shape = predictor(gray, rect)
		# shape = face_utils.shape_to_np(shape)
		# mouth = shape[mStart:mEnd]
		# print(x, y, w, h)
		# cropFrame = frame[y-25:y+w+25, x-30:x+w+30]
		

		cropFrame = frame[y-50:y+w+50, x-40:x+w+40]
		cropFrame = cv2.resize(cropFrame, (96,96), cv2.INTER_LINEAR)

		if not isShort:
			if cnt >= fix_len and cnt < length - fix_len: 
				out.write(cropFrame)
		else:
			out.write(cropFrame)	

		cnt += 1


		if isShort and cnt > length:
			fixFrame = frame[y-50:y+w+50, x-40:x+w+40]
			fixFrame = cv2.resize(fixFrame, (96,96), cv2.INTER_LINEAR)
			for i in range (1, math.ceil(fix_len)):
				out.write(fixFrame)

		ret, frame = fvs.read()

	duration = (length - 2) / 25.0

	info = open('data/output.txt', 'w')
	info.write('Duration: ' + str(duration) + ' seconds')
	info.close()


	out.release()

def preprocess():
	speakingFrame = real_time_detect()
	# speakingFrame = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	# print(get_duration(speakingFrame))
	# duration = 0.68
	# start = 3
	# end = 31
	# duration, start, end = get_duration(speakingFrame)
	# crop(start, end)
	new_crop()


import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
	app =  QApplication(sys.argv)

	# create and show mainWindow
	mainWindow = main_window.MainWindow()
	mainWindow.show()

	# sys.exit(app.exec_())
	preprocess()