# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 19:12:55 2022

@author: Rechacalos"""
from threading import Thread
from alarme_test1 import *
from transformateur_image_en_video import *

if __name__ == '__main__':
    
    camera = 0
    
    kernel_blur=3
    
    seuil=15
    
    surface=1000
    
    
    Thread( target= alarme, args=(seuil,surface,kernel_blur,camera)).start()
    Thread(target = trans()).start()
    
    
    



