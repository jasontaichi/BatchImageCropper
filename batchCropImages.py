import numpy as np
import cv2
import glob
import os

startPoint_x = 440
startPoint_y = 0
endPoint_x = 840
endPoint_y = 720

def Crop_Image(filename):
    # The cropped image will be named "<original_filename>_cropped.jpg"
    base_filename, file_extension = os.path.splitext(filename)
    cropped_filename = f"{base_filename}_cropped{file_extension}"

    # Create and save cropped image
    img = cv2.imread(filename)
    height, width = img.shape[0:2]

    startRow = int(startPoint_y)
    startCol = int(startPoint_x)
    endRow = int(endPoint_y)
    endCol = int(endPoint_x)

    croppedImage = img[startRow:endRow, startCol:endCol]

    """
    cv2.imshow('Original image', img)
    cv2.imshow('Cropped image', croppedImage)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    """
    cv2.imwrite(cropped_filename, croppedImage)

    return cropped_filename


# Loop through all jpeg files in the folder and make a cropped image for each file
for image_file in glob.glob("*.jpg"):
    cropped_file = Crop_Image(image_file)

    print(f"A cropped file for {image_file} was saved as {cropped_file}")