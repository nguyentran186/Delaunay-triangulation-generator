import os
import cv2
import numpy as np
from PIL import Image

directory = "D:\VScode\Python\ML\Delaunay triangulation\sub_image"
os.chdir(directory)

num_of_image = 99


def generate_video():
    image_folder = '.'
    video_name = 'ascii_image.avi'
    os.chdir(directory)

    linlist = []
    for i in range(0, 100):
        linlist.append(100-i)

    images = [img for img in os.listdir(image_folder)]
    images = ["img{}.jpg".format(int(index)) for index in linlist]

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 5, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    # for i in range (0,5):
    #     video.write(cv2.imread("D:\VScode\Python\ML\Delaunay triangulation\image.jpg"))

    cv2.destroyAllWindows()
    video.release()


generate_video()
