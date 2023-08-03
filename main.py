import cv2          # opencv-python
import numpy as np
import pyautogui

cv2.namedWindow('My_window', cv2.WINDOW_NORMAL)
cv2.moveWindow('My_window', 1600, 0)
while True:
    # 1920, 1080 screen resolution of my laptop
    image = pyautogui.screenshot(region=(300, 600, 255, 250))    # left, top, width, and height
    # image.show()
    # print("5s passed")
    # print(np.array(image))
    # OpenCV: color order is BGR (blue, green, red); Pillow (used by pyautogui): color order is RGB (red, green, blue).
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    black_pixel_count = np.sum(image < 100)
    white_pixel_count = np.sum(image > 100)
    print(f"Number of black pixels: {black_pixel_count}")
    print(f"Number of white pixels: {white_pixel_count}")
    # light mode
    if black_pixel_count > 4000 and black_pixel_count < 30000:
        pyautogui.press('up')
    # dark mode
    if white_pixel_count > 4000 and white_pixel_count < 30000:
        pyautogui.press('up')

    cv2.imshow('My_window', image)
    # cv2.imshow('image', image)
    # time in milliseconds
    if cv2.waitKey(25) == ord('q'):
        cv2.destroyAllWindows()
        break


