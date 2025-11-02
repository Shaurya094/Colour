import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('example.jpg')

brightness_matric = np.ones(image.shape, dtype="uint8") * 50
brighter = cv2.add(image, brightness_matric)
bright = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(bright)
plt.title('brighter image')
plt.show()

crop = image[100:300, 20:400]
cropped_image = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_image)
plt.title('cropped image')
plt.show()