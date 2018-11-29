import cv2
import numpy as np
def laplace(img,channel='3ch',threshold=200,minLineLength=150,maxLineGap=10,
            thickness=6,draw_rgb=(255,0,0)):
    img_copy = np.copy(img)
    gray = cv2.cvtColor(img_copy,cv2.COLOR_BGR2GRAY)
    dst3 = cv2.Laplacian(gray, cv2.CV_32F, ksize=3)
    dst3 = np.where(dst3<0,0,dst3)
    lines = cv2.HoughLinesP(
        dst3.astype(np.uint8),
        1,
        np.pi/180,
        threshold,
        minLineLength,
        maxLineGap)
    if channel == '3ch':
        try:
            for line in lines:
                x1,y1,x2,y2 = line[0]
                cv2.line(img_copy,(x1,y1),(x2,y2),draw_rgb,thickness)
        except TypeError:
            pass
        return img_copy
    elif channel == '4ch':
        img_out = np.zeros_like(img_copy)
        try:
            for line in lines:
                x1,y1,x2,y2 = line[0]
                cv2.line(img_out,(x1,y1),(x2,y2),(255,0,0),thickness) 
        except TypeError:
            pass
        img_copy = np.dstack((img_copy,img_out[:,:,0]))
        return img_copy
    else:
        print('func laplace:set channel')
        return
