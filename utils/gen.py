
import cv2
import torch
cap = cv2.VideoCapture('sunday.mp4')

video=[]
while(cap.isOpened()):
    ret, frame = cap.read()
    if(frame is not None):
        frame = cv2.imencode('.jpg',frame)[1]
        video.append(frame)
    else: break

for frame in video:
    frame=cv2.imdecode(frame, cv2.IMREAD_COLOR)
    cv2.imshow('video',frame)
    k = cv2.waitKey(20)

# # -*- coding: utf-8 -*-
# import numpy as np
# import urllib
# import cv2
#
# img = cv2.imread('0122.jpg')
# # '.jpg'表示把当前图片img按照jpg格式编码，按照不同格式编码的结果不一样
# img_encode = cv2.imencode('.jpg', img)[1]
# # imgg = cv2.imencode('.png', img)
#
# data_encode = np.array(img_encode)
# str_encode = data_encode.tostring()
#
# # 缓存数据保存到本地，以txt格式保存
# with open('img_encode.txt', 'w') as f:
#     f.write(str_encode)
#     f.flush
#
# with open('img_encode.txt', 'r') as f:
#     str_encode = f.read()
#
# nparr = np.fromstring(str_encode, np.uint8)
# img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
# cv2.imshow("img_decode", img_decode)
#
#

#
# torch.save({
# 'video': video,
# 'label': model.state_dict(),
# 'duration': optimizer.state_dict(),
# }, PATH)