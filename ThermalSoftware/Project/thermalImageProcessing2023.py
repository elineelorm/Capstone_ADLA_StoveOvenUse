import cv2
import PIL
import numpy as np
import math
import sys
from matplotlib import pyplot as plt
import time
import math
from statistics import mean

"""
    thermalImageProcessing2023.py
    This file includes all the functions that the application uses to extract features from the video frame
    
    Author: Group from 2021/2022 (Jonathan Mack)
    Edited by Hiu Sum Jaime Yue and Eline Elorm Nuviadenu

"""
tempRange = np.load('Project/brightness2Temperature.npy')

def find_nearest(value):
    array = tempRange[:, 1]
    idx = (np.abs(array - value)).argmin()
    return (tempRange[idx][0], int(tempRange[idx][1]))

def cropImage(img, percent):
    width = img.shape[1]
    height = img.shape[0]
    widthCrop = int(width * percent / 100)
    heightCrop = int(height * percent / 100)
    return img[heightCrop:height-heightCrop, widthCrop:width-widthCrop]

"""
This function samples a video at the given sampleRate in seconds. And
returns an array of images of the sampled stills. 
"""
def sampleVideo(vid, sampleRate):
    
    video = cv2.VideoCapture(vid)

    fps = video.get(cv2.CAP_PROP_FPS)
    #Therefore we need to sample every xth frame
    sampleDuration = fps * sampleRate
    sampledList = []
    index = 0
    ret, frame = video.read()
    sampledList.append(frame)
    while(True):
        ret, frame = video.read()
        if not ret: 
            break
        if index%(sampleDuration)==0:
            sampledList.append(frame)
        index += 1
    
    return sampledList

"""
This function resizes the image keep aspect ratio.
"""
def resizeImage(img, percent):
    width = int(img.shape[1] * percent / 100)
    height = int(img.shape[0] * percent / 100)
    dim = (width, height)

    # resize image
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

"""
This function determines the average temperature of all contours
detected in the pan (including pan). The largest item returned is the pan
"""
def getContourHeat(contours, img, frame):
    # For each list of contour points...
    contourFeatures = []
    temperatureList = []
    for i in range(len(contours)):
        # Create a mask image that contains the contour filled in
        cimg = np.zeros_like(img)
        cv2.drawContours(cimg, contours, i, color=255, thickness=-1)

        # Access the image pixels and create a 1D numpy array
        pts = np.column_stack(np.where(cimg == 255))
        totalTemp = 0
        objectTemp = []
        for p in pts:
            temp, brightness = find_nearest(frame[p[0], p[1]])
            objectTemp.append(temp)
            totalTemp += temp
        avgTemp = totalTemp/(len(pts))
        #print("Average Temp of Contour is: %.2f" % avgTemp, "°C")
        contourFeatures.append((avgTemp, len(pts)))
        temperatureList.append(objectTemp)

    return contourFeatures, temperatureList

"""
This function returns the average temperature of the image
"""
def getAverageImageTemperature(image):
    height, width = image.shape
    sum = 0
    for x in range(0, width-1):
        for y in range(0, height-1):
            temp, brightness = find_nearest(image[y, x])
            sum += temp

    return sum / (height*width)

"""
This function returns the area of where the pan is,
              in An array of coordinates (x, y)
"""
def contourMask(image):
    pts = np.where(image != 0)
    #print(len(pts[0]))
    coordinates = []
    for i in range(len(pts[0])):
        coordinates.append((pts[0][i], pts[1][i]))
    # print("Contour Mask")
    # print(coordinates)
    return coordinates

"""
This function is trying to find the outline of the pan in the image
"""
def findPan(frame, image):
    original = np.copy(frame)
    image_cropped = cropImage(np.copy(image), 2)
    contours, _ = cv2.findContours(image_cropped, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    biggest_contour = contour_sizes[0]
    for i in range(1, len(contour_sizes)):
        if(biggest_contour[0] < contour_sizes[i][0]):
            biggest_contour = contour_sizes[i][0], contour_sizes[i][1]

    cv2.drawContours(original, contours, contourIdx=-1, color=255, thickness=4)
    # Find the rotated rectangles and ellipses for each contour
    if biggest_contour[1].shape[0] > 5:
            minEllipse = cv2.fitEllipse(biggest_contour[1])

    # Draw contours + rotated rects + ellipses
    contours = [biggest_contour]
    blackFrame = 0 * np.ones((image.shape[0], image.shape[1],3), np.uint8)
    for i, c in enumerate(contours):
        color = (255, 255, 255) #White
        # ellipse
        if c[1].shape[0] > 5:
            cv2.ellipse(blackFrame, minEllipse, color, -1)
    # print("Black Frame")
    # print(blackFrame)
    return blackFrame

def open_Morph(image):
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(image,kernel,iterations = 2)
    dilation = cv2.dilate(erosion,kernel,iterations = 1)
    return dilation

def getContoursInsidePan(image, frame):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_L1)
    image_cpy = frame.copy()
    cv2.drawContours(image=image_cpy, contours=contours, contourIdx=-1, color=(0,255,255),
                thickness=1, lineType=cv2.LINE_AA)
    
    return image_cpy, contours

def getPercentageOfMode(image):
    height, width = image.shape
    sum = 0
    temps = []
    for x in range(0, width-1):
        for y in range(0, height-1):
            temp, brightness = find_nearest(image[y, x])                
            temps.append(temp)

    counts, bins = np.histogram(temps, 15)
    sum = np.sum(counts)
    return (np.amax(counts)/sum)

"""
This function returns the average of temperature using pnts,
              in float, used for avgPanTemp
"""
def getAverageTemperature_pnts(pnts, image):
    sum = 0
    for p in pnts:
        temp, brightness = find_nearest(image[p[0], p[1]])
        sum += int(temp)
    # print("getAvgPanTemp")
    # print(sum/len(pnts))
    return sum/len(pnts)

def thermalImagingProcess(frames, rate):
    #Iterate over every sampled frame in video
    backgroundTemp = 24
    #background = resizeImage(frames[0], 25)
    prevIsBG = True
    entries = []
    startTime = time.time()
    i=0
    for frame in frames:
        #foreground is just the original frame to grey
        foreground = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)

        #Convert to grayscale and blur, image to grey to compare easier 
        #than actual thermal screenshot's colour
        print("Frame: "+str(i)+" - Blurring Image. ElapsedTime: " + str(time.time() - startTime))
        blur= cv2.medianBlur(np.copy(foreground),5)
        print("Frame: "+str(i)+" - Thresholding Image. ElapsedTime: " + str(time.time() - startTime))
        thresh_gray = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 127, 1)
        print("Frame: "+str(i)+" - Morphing Image. ElapsedTime: " + str(time.time() - startTime))
        open_morph = open_Morph(thresh_gray)
        #Try to identify pan
        print("Frame: "+str(i)+" - FindPan. ElapsedTime: " + str(time.time() - startTime))
        ellipse = cv2.cvtColor(findPan(foreground, open_morph), cv2.COLOR_BGR2GRAY)
        # Mask the outline of the pan
        print("Frame: "+str(i)+" - BitwiseMask Image. ElapsedTime: " + str(time.time() - startTime))
        ellipseMask = cv2.bitwise_and(foreground, ellipse)
        print("Frame: "+str(i)+" - Column Stack Image. ElapsedTime: " + str(time.time() - startTime))
        
        # 2023 get Temp for missing pan (Set Avg temp of frame)
        missingPanTemp = 0
        
        #Now take the pan shape and analyze 
        if not len(np.column_stack(np.where(ellipse != 0))) == 0:

            print("Frame: "+str(i)+" - ContourMask. ElapsedTime: " + str(time.time() - startTime))
            pnts = list(set(contourMask(ellipse)))
            print("Frame: "+str(i)+" - Get PanTemp Image. ElapsedTime: " + str(time.time() - startTime))
            panTemp = getAverageTemperature_pnts(pnts, foreground)
            print("Frame: "+str(i)+" - After PanTemp Image. ElapsedTime: " + str(time.time() - startTime))
            if not (backgroundTemp - panTemp > - 10):
                blurPan = cv2.medianBlur(np.copy(ellipseMask),5)
                thresh_insidePan = cv2.adaptiveThreshold(blurPan, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 127, 1)
                thresh_insidePan = np.where(ellipse == 0, 0, thresh_insidePan)
                open_morphPan = open_Morph(thresh_insidePan)
                insidePan, contours = getContoursInsidePan(open_morphPan, foreground)

                print("Frame: "+str(i)+" - Get Contour Heat. ElapsedTime: " + str(time.time() - startTime))
                pts, temperatureList = getContourHeat(contours, thresh_insidePan, foreground)
                print("Frame: "+str(i)+" - After Contour Heat. ElapsedTime: " + str(time.time() - startTime))
                if temperatureList is not None and all(x is None for x in temperatureList):
                    for tempL in temperatureList[1:len(temperatureList)-1]:
                        for x in tempL:
                            try:
                                temperatureList[0].remove(x)
                            except ValueError:
                                pass

                print("Frame: "+str(i)+" - After Temperature List. ElapsedTime: " + str(time.time() - startTime))    
                pts = list(filter(lambda x: x[1] > 50, pts)) 

                # 2023: new fix for ValueError:max() arg is an empty sequence when pan have nothing
                try:
                    pan = max(pts,key=lambda item:item[1])
                except ValueError:
                    pan = [0, 0]
                # fix end

                if(len(pts) > 1):
                    food = pts.copy()
                    food.remove(pan)
                    #Now remove food from pan pixels and average temp
                    for f in food:
                        panAvg = (pan[0]*pan[1]-f[0]*f[1])/(pan[1]-f[1])
                        pan = (panAvg, pan[1] - f[1])
                    foodTemp = [x[0] for x in food]
                    foodSize = [x[1] for x in food]

                    # 2023: i * rate of the 20 equally spaced frames
                    entries.append((i*rate, pan[0], str(max(max(temperatureList))), str(min(min(temperatureList))), str(mean(foodTemp)), str(max(foodTemp)), str(min(foodTemp))))
                
                # 2023 Case Cannot find food but detected heat with 2023 changes
                else:   
                    entries.append((i*rate, panTemp, panTemp, panTemp, panTemp, panTemp, panTemp))    
            
            # 2023 Stove off case (if (backgroundTemp - panTemp > - 10))
            else:
                print("Frame: " + str(i) + " - Cannot find temp difference between background and pan" + 
                 " current detected PanTemp is " + str(panTemp)) 
                entries.append((i*rate, panTemp, panTemp, panTemp, panTemp, panTemp, panTemp))   
        
        # 2023 Can't find Pan  
        else:
            entries.append((i*rate, missingPanTemp, missingPanTemp, missingPanTemp, missingPanTemp, missingPanTemp, missingPanTemp))   
        i += 1
        if i >= 20:
            break
    return entries

"""
This function will sample a thermal video with a rate of sampleRate
and will add the data derived for each frame to the table
"""
def processVideo(video, sampleRate):
    frames = sampleVideo(video, sampleRate)
    entries = thermalImagingProcess(frames, sampleRate)
    return entries