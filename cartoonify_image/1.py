import cv2 #importing for image processing
import tkinter as tk #importing for making GUI
from tkinter import filedialog
from tkinter import *
import numpy as np # importing for numerical operations
import matplotlib.pyplot as plt
import os 
import sys # for system operations
import imageio # for saving and accessing images
import easygui # for accessing already built GUI designs
from PIL import ImageTk, Image  #to convert images for tkinter


#function to get the image path
def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)

#function to cartoonify the image
def cartoonify(ImagePath):
    original_image = cv2.imread(ImagePath)

    # converting the image to more accesible RGB format
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    if original_image is None:
        print("Image not found")
        sys.exit()

    resized_image = cv2.resize(original_image,(960,540))
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    smooth_gray_image = cv2.medianBlur(gray_image, 5)

    getEdge = cv2.adaptiveThreshold(smooth_gray_image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,9)
    
    color_img = cv2.bilateralFilter(resized_image, 9, 500, 500)
    cartoonImage = cv2.bitwise_and(gray_image, smooth_gray_image, mask=getEdge)

# Displaying the images using matplotlib
    images = [original_image, gray_image, smooth_gray_image, getEdge, color_img, cartoonImage]
    fig, axes = plt.subplots(3,2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, 
    gridspec_kw=dict(hspace=0.1, wspace=0.1))
    
    for i, ax in enumerate(axes.flat): #enumerate to get index(i) and object(ax) , ax has objects
    #axes.flat is used to get a 1d array of axes from 2d
        ax.imshow(images[i], cmap='gray')

    plt.show()

cartoonify("cartoonify_image/person_img.jpg")
 #to show the images
