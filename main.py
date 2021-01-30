import time, pyautogui, cv2, mss, numpy as np
from utils import *
from Policy import *

policy = Policy()

pyautogui.click(detect_init_location())
print("game start")
with mss.mss() as sct:

    monitor = detect_monitor_location()

    while 'Screen capturing':
        img = np.array(sct.grab(monitor))

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        circles = detect_cycles(img_gray)
        # display_circles(img_gray, circles)

        click_x, click_y = policy.guess_click_location(circles)
        pyautogui.click(click_x, click_y)

        time.sleep(3)

