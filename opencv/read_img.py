import cv2
import numpy as np

path = 'iu.jpeg'
img = cv2.imread(path,1); #1= colour & neglect transparency, 0= greyscale, -1 = unchanged including alpha channel
cv2.imshow('IU',img);

cv2.waitKey(1000);

cv2.destroyAllWindows();

status = cv2.imwrite(path,img);
print('image written success?', status);

