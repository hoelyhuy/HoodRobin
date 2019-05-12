#https://github.com/jennyzeng/Minecraft-AI/blob/master/src/Img_Preprocess/ImgPreprocess.py

from PIL import Image
import cv2
import numpy as np

def saveArrayAsImg(array, width, height, outfile, wantDepth=False, outfile_d=None):
    array = np.array(array)
    array = array.reshape(height, width, 3)
    im = Image.fromarray(array, mode='RGB')
    im.save(outfile)
    return True
