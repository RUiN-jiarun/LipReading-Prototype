# encoding: utf-8
import numpy as np
import glob
import time
import cv2
import os
from torch.utils.data import Dataset
from .cvtransforms import *
import torch
#from turbojpeg import TurboJPEG, TJPF_GRAY, TJSAMP_GRAY, TJFLAG_PROGRESSIVE


from PIL import Image
# jpeg = TurboJPEG()
class LRWDataset(Dataset):
    def __init__(self, phase, args):

        with open('label_sorted.txt') as myfile:
            self.labels = myfile.read().splitlines()            
        
        self.list = []
        self.unlabel_list = []
        self.phase = phase        
        # self.args = args
        
        # if(not hasattr(self.args, 'is_aug')):
        #     setattr(self.args, 'is_aug', True)

        for (i, label) in enumerate(self.labels):
            files = glob.glob(os.path.join('DataSet', label, phase, '*.mp4'))
            files = sorted(files)
            

            self.list += [(file,i) for file in files]
            
        
    def __getitem__(self, idx):


        cap = cv2.VideoCapture(self.list[idx][0])

        video = []
        while (cap.isOpened()):
            ret, frame = cap.read()
            if (frame is not None):
                video.append(frame)
            else:
                break

        # load a pkl created by torch.save()
        #        torch.save({
        #         'video': video,
        #         'label': model.state_dict(),
        #         'duration': optimizer.state_dict(),
        #         }, PATH)


        inputs = video
        print("inputs")
        # inputs = [jpeg.decode(img, pixel_format=TJPF_GRAY) for img in inputs]
        inputs = np.stack(inputs, 0) / 255.0
        inputs = inputs[:, :, :, 0]

        
                
        if(self.phase == 'train'):
            batch_img = RandomCrop(inputs, (88, 88))
            batch_img = HorizontalFlip(batch_img)
        elif self.phase == 'val' or self.phase == 'test':
            batch_img = CenterCrop(inputs, (88, 88))
        
        result = {}            
        result['video'] = torch.FloatTensor(batch_img[:,np.newaxis,...])
        #print(result['video'].size())
        result['label'] = (int)(self.list[idx][1])

        result['duration'] = 1.0 * self.load_duration(self.list[idx][0].replace('.mp4', '.txt')) .astype(np.bool)

        return result

    def __len__(self):
        return len(self.list)

    def load_duration(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if(line.find('Duration') != -1):
                    duration = float(line.split(' ')[1])
        
        tensor = np.zeros(29)
        mid = 29 / 2
        start = int(mid - duration / 2 * 25)
        end = int(mid + duration / 2 * 25)
        tensor[start:end] = 1.0
        return tensor



