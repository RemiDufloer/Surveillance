# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 14:07:01 2022

@author: starx
"""
import cv2
import os
import sys
import time

def trans():
    j=1
    compt=0
    while j:
        path= os.path.dirname(os.path.realpath(__file__))
        l = os.listdir(path+'\image') 
        print(l)
        number_files = len(l)
        if number_files == 0  :
            continue
        time.sleep(2)
        l = os.listdir(path+'\image') 
        print( number_files)
        image=list()
        for i in l:
            image.append(cv2.imread('./image/'+i))
        
            
        height,width,layers=image[0].shape
    
        video=cv2.VideoWriter('./intrus/video'+str(compt)+'.mp4',-1,1,(width,height))
        print('je vais save une video '  )
        print(len(image))
        for j in range(len(image)):
            video.write(image[j])
        
        print('jai save')
        compt+=1
        for i in l:
            
            os.remove('./image/'+i)
        video.release()
            
        
    
            