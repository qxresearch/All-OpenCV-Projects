import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread(r'E:\AI projects\Opencv\myphoto.jpg')
print('This is the image type:',type(image),
      'with dimensions:', image.shape)

img_copy = np.copy(image)
image_copy = cv.cvtColor(img_copy,cv.COLOR_BGR2RGB)
plt.imshow(image_copy)

lower_green = np.array([0,200,0])
upper_green = np.array([250,255,250])

mask = cv.inRange(image_copy,
                  lower_green,
                  upper_green)
plt.imshow(mask, cmap='gray')

masked_image = np.copy(image_copy)
masked_image[mask !=0] = [0,0,0]
plt.imshow(masked_image)

background_image = cv.imread('./images/london.jpg')
background_image = cv.cvtColor(background_image,
                               cv.COLOR_BGR2RGB)

crop_background = background_image[0:450, 0:660]
crop_background[mask==0]=[0,0,0]
plt.imshow(crop_background)

x=390
y=300
h=450
w=660
background_image = cv.imread('./images/london.jpg')
background_image = cv.cvtColor(background_image,
                               cv.COLOR_BGR2RGB)

crop_background = background_image[y:y+h, x:x+w]

crop_background[mask==0]=[0,0,0]
plt.imshow(crop_background)

complete_image = masked_image + crop_background
plt.imshow(complete_image);