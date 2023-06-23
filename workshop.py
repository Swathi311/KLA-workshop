import pandas as pd
import numpy as np
import json
import cv2
from PIL import Image
import csv


def isInCareArea(x,y):
    for area in care_areas:
        side1 = (area[0]['top-left']['x'] - area[0]['top-left']['x']) * (y - area[0]['top-left']['y']) - (x - area[0]['top-left']['x']) * (area[0]['bottom-right']['y'] - area[0]['top-left']['y'])
        #find side 2,3,4
        #If D > 0, the point is on the left-hand side. If D < 0, the point is on the right-hand side. If D = 0, the point is on the line.
        # test whether the point lies to the left of the edge (in the left-hand half-plane). If all edges pass the test - the point is inside. If at least one fails - the point is outside.

with open('/Users/swathis/Desktop/Level_1_Input_Data/input.json') as json_data:
    data = json.load(json_data)
    die_width = data['die']['width']
    die_height = data['die']['height']
    care_areas = data['care_areas']
    total_care_areas = len(data['care_areas'])
    exclusion_zones = data['exclusion_zones']


output = open("/Users/swathis/Desktop/output.csv", "w")
writer = csv.writer(output)
for i in range(1,6):

    img1 = Image.open("/Users/swathis/Desktop/Level_1_Input_Data/wafer_image_"+str(i)+".png")
    image1 = img1.load()
    img_width,img_height = img1.size
    no_of_images = int(die_width/img_width)
    if (i == 5):
        img_to_cmp = Image.open("/Users/swathis/Desktop/Level_1_Input_Data/wafer_image_"+str(i-no_of_images)+".png")
    else:
        img_to_cmp = Image.open("/Users/swathis/Desktop/Level_1_Input_Data/wafer_image_" + str(i + no_of_images) + ".png")
    image2 = img_to_cmp.load()
    x=0
    for x in range(img_width):
        for y in reversed(range(img_height)):
            if(image1[x,y] == image2[x,y]):
                continue
            else:
                if(image1[x,y] == (128,128,128)):
                    continue
                else:
                    writer.writerow([i, x, 600-y-1])









