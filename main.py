import cv2
import numpy as np
import os
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


directory = "D:\VScode\Python\ML\Delaunay triangulation"
out_path = "D:\VScode\Python\ML\Delaunay triangulation\sub_image\img{}.jpg"
os.chdir(directory)

image_name = "image.jpg"

color_image = cv2.imread(image_name)
image = cv2.imread(image_name, 0)
gaussian_image = cv2.GaussianBlur(image, (5, 5), 1000)
_, thresh = cv2.threshold(gaussian_image, 8, 255, cv2.THRESH_BINARY)
# cv2.imshow("Image", thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
height, width = gaussian_image.shape

def generator(div):
    div_val = div
    points = []
    # for row in range(2, int(height/5)-2):
    #     for col in range(2, int(width/5)-2):
    #         row_index, col_index = row*5, col*5
    #         if abs(gaussian_image[row_index][col_index]-gaussian_image[row_index+5][col_index]) > 20 \
    #                 or abs(gaussian_image[row_index][col_index]-gaussian_image[row_index-5][col_index]) > 20 \
    #                 or abs(gaussian_image[row_index][col_index]-gaussian_image[row_index][col_index+5]) > 20 \
    #                 or abs(gaussian_image[row_index][col_index]-gaussian_image[row_index][col_index-5]) > 20 \
    #                 or abs(gaussian_image[row_index][col_index]-gaussian_image[row_index+5][col_index-5]) > 20 \
    #                 or abs(gaussian_image[row_index][col_index]-gaussian_image[row_index-5][col_index-5]) > 20 \
    #                 or abs(gaussian_image[row_index][col_index]-gaussian_image[row_index+5][col_index+5]) > 20 \
    #                 or abs(gaussian_image[row_index][col_index]-gaussian_image[row_index-5][col_index+5]) > 20:
    #             points.append([row_index, col_index])


    for i in range(0, int(width/div_val)):
        for j in range(0, int(height/div_val)):
            col = i*div_val
            row = j*div_val
            if thresh[row][col] == 255:
                points.append([row,col])

    points = np.array(points)
    # print(points)
    tri = Delaunay(points)

    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)
    for i in range (0, len(tri.simplices)):
        first_point = tri.simplices[i][0]
        sec_point = tri.simplices[i][1]
        third_point = tri.simplices[i][2]
        x1, y1 = points[first_point]
        x2, y2 = points[sec_point]
        x3, y3 = points[third_point]
        b = color_image[x1][y1][0]
        g = color_image[x2][y2][1]
        r = color_image[x3][y3][2]
        # b = int((color_image[x1][y1][0]+color_image[x2][y2][0]+color_image[x3][y3][0])/3)
        # g = int((color_image[x1][y1][1]+color_image[x2][y2][1]+color_image[x3][y3][1])/3)
        # r = int((color_image[x1][y1][2]+color_image[x2][y2][2]+color_image[x3][y3][2])/3)
        draw.polygon(((y1,x1),(y2,x2),(y3,x3)), fill=(r,g,b))
    image.save(out_path.format(div_val))
    ############PLOT USING PLT
    # plt.triplot(points[:, 1], -1*points[:, 0], tri.simplices, color = 'black')
    # for i in range (0,len(points)):
    #     x = points[i,1]
    #     y = points[i,0]

    #     b = color_image[y][x][0]/255
    #     g = color_image[y][x][1]/255
    #     r = color_image[y][x][2]/255
    #     plt.plot(points[i,1], -1*points[i,0], '.', color = [r,g,b])
    # plt.axis('off')
    # plt.gca().set_aspect('equal')
    # plt.show()
for i in range(1,100):
    print(i)
    generator(i)