
import numpy as np
import random
import time
import cv2
import math
import cannon as cn

if __name__ == "__main__":
    #creates a bunch of jpgs that can be made into a git     
    k = cn.Cannon()
    img = np.zeros([28,28,3])
    length = 20
    x, y = k.generate_28x28(1, length)
    for i in xrange(length/2):
        img[:,:,0] = x[0,i*2,:].reshape(28,28)
        img[:,:,1] = x[0,i*2,:].reshape(28,28)
        img[:,:,2] = x[0,i*2,:].reshape(28,28)
        cv2.imwrite(str(i).zfill(3) + '.jpg', img*255)
        cv2.imshow('image', img)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
    

