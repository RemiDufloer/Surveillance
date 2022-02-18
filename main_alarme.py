# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 13:07:05 2022

@author: Rechacalos
"""

from threading import Thread
from alarme_test1 import *
from transformateur_image_en_video import *

if __name__ == '__main__':
    
    camera = 1
    
    kernel_blur=3
    
    seuil=15
    
    surface=1000
    
    
    alarme(seuil,surface,kernel_blur,camera)
    
    
    
    
    