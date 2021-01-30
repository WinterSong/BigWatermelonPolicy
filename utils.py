import pyautogui, cv2
import numpy as np


# use screen-shot to locate the game website
# and replace the params

def detect_monitor_location():
    return {'top': 135, 'left': 0, 'width': 500, 'height': 750}

def detect_init_location():
    # the start key
    return (250, 680)

def detect_cycles(img_gray):
    minDist = 100
    param1 = 30  # 500
    param2 = 100  # 200 #smaller value-> more false circles
    minRadius = 1
    maxRadius = 300  # 10
    circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
    return circles

def display_circles(img_gray, circles):
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(img_gray, (i[0], i[1]), i[2], (0, 0, 0), 10)

    cv2.imshow('img', img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
