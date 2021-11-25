import os
import cv2

# Add path to the folder containing images
path = 'D:\\Pilot\\Carlsbergproj\\Images\\SFDC\\Arnab\\'
for count, file in enumerate(os.listdir(path)):
	 
	img_path = path+file
	img = cv2.imread(img_path)
	height, width, channels = img.shape

	# Minimum height and width that will be used in the cfg while setting 
	# configuring the custom settings. 
	# 416 used here
	if (height and width) < 416:

		print(file)