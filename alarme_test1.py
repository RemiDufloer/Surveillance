# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 11:47:25 2022

@author: Rechacalos
"""




import numpy as np
import cv2
from datetime import datetime



def alarme(seuil,surface,kernel_blur,cam):
    cap=cv2.VideoCapture(cam) # appel a la camera pour lui demander de capturer des images en continue
    
    
    ret, originale=cap.read() #on recupere les image ret etant si nous arrivons a ouvrir la camera ou pas
    if ret is False:
        print('nous ne sommes pas parvenue à ouvrir la caméra')
        quit()
    originale=cv2.cvtColor(originale, cv2.COLOR_BGR2GRAY) #On convertie l'image en noir et blanc
    originale=cv2.GaussianBlur(originale, (kernel_blur, kernel_blur), 0) # on applique a cette image quelque seuil pour ne pas être déranger via les pixel
    kernel_dilate=np.ones((5, 5), np.uint8) 
    alarme=0
    intrus=0
    i=1
    while i:
        ret, frame=cap.read()
        if ret is False:
            quit()
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_blur=cv2.GaussianBlur(gray, (kernel_blur, kernel_blur), 0)
        mask=cv2.absdiff(originale, gray_blur)
        mask=cv2.threshold(mask, seuil, 255, cv2.THRESH_BINARY)[1]
        mask=cv2.dilate(mask, kernel_dilate, iterations=3)
        contours, _=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        frame_contour=frame.copy()
        for c in contours:
            if cv2.contourArea(c)<surface:
                continue
            cv2.drawContours(frame_contour, [c], 0, (0, 255, 0), 2)
            x, y, w, h=cv2.boundingRect(c)
            alarme=1
            intrus=1
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            if intrus:
                save(frame)
                cv2.putText(frame, "INTRUS", (x, y-20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
        originale=gray_blur
        if alarme:
            cv2.putText(frame, "ALARME", (10, 60), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
        cv2.putText(frame, "[o|l]seuil: {:d}  [p|m]blur: {:d}  [i|k]surface: {:d}".format(seuil, kernel_blur, surface), (10, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 255), 2)
        cv2.imshow("frame", frame)
        cv2.imshow("Mask", mask)
        intrus=0
        key=cv2.waitKey(30)&0xFF
        if key==ord('q'):
            i=0
        if key==ord('p'):
            kernel_blur=min(43, kernel_blur+2)
        if key==ord('m'):
            kernel_blur=max(1, kernel_blur-2)
        if key==ord('o'):
            seuil=min(255, seuil+1)
        if key==ord('l'):
            seuil=max(1, seuil-1)
        if key==ord('i'):
            surface+=1000
        if key==ord('k'):
            surface=max(500, surface-1000)
        if key==ord('a'):
            alarme=0
    cap.release()
    cv2.destroyAllWindows()
    
    
def save(image):
    i= datetime.now().strftime('%Y-%m-%d-_-%H_%M_%S')
    j= str(datetime.now()).split('.')
    j=j[1]
    
    print('je vais save ' + i )
    cv2.imwrite('./image/intrus'+i+'_'+j[0]+'.png', image)
    print('jai save')
    