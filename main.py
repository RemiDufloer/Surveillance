# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 15:55:57 2021

@author: rechaclos
"""


"""
cette version prend juste une camera regarde si il n'y a qu'une seul couleur
si ce n'est pas le cas elle ecrit dans un fichier texte
il y a plusieur problème à cette version on ne prend pas encore en compte la taille
on n'envoie aucune chose sur une base de donée
on boucle que 500 fois (environ 5 sec)
 
est ce que la caméra ce trouve a chaque bac de camion ? 
est ce que la météo peut affluencer notre camera est donc avoir differente couleur (soleil)?
est ce que nous devrions nous pas mettre une variance au couleur en fonction de la luminosité 
accepter une différence de variation par exemple accepter tout entre 255 255 255 et 245 245 245 ?




pour la base de donnée chaque rasberry auras un identifiant, un trajet et une date
a chaque chargement on met en route le dispositif et lorsqu'on a tout decharger on arrete le dispostif 
pour empecher le surdosage de la bdd

pour l'affichage sur le télephone il faudrait savoir quelle trajet on veut surveiller, pour cela 
on peut mettre un qrcode sur le rasbery pour que la google list comprenne ou chercher
les images dans la bdd

"""

import sys
import cv2
from analyseur_d_image import *

from PIL import Image

if __name__ == '__main__':
    f = open('result.txt','w')
    i=1
    camera = cv2.VideoCapture(0)
    while i !=500:
        return_value, image = camera.read()
        cv2.imwrite('./image/opencv'+str(i)+'.png', image)
        img=Image.open('./image/opencv'+str(i)+'.png')
        colors = convert_in_colors(img)
        print(colors)
        if object_in(colors):
            f.write(str(i))
            
            f.write('\n')
        i+=1
    f.close()
    del(camera)
            