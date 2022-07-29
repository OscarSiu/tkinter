import cv2
import numpy as np

img = cv2.imread('iu.jpeg', 1);
print(img.shape);

img_resized = cv2.resize(img, (540, 355), interpolation = cv2.INTER_NEAREST);
cv2.imshow('resized', img_resized);

cv2.waitKey(0);
cv2.destroyAllWindows();

#INTER_NEAREST   nearest-neighbor interpolation
#INTER_LINEAR    bilinear interpolation (use by default)
#INTER_AREA      resampling by pixel area relation
#INTER_CUBIC     bicubic interpolation over 4x4 pixel neighborhood
#INTER_LANCZOS4  Lanczos interpolation over 8x8 pixel neighborhood
