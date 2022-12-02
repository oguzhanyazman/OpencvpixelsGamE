
import cv2
import numpy as np
import pyautogui
import keyboard
from pynput.mouse import Controller as Controller
from pynput.mouse import Button
import time


if __name__ == '__main__':
    print('Starting...')

   
    mouse = Controller()
    enabled = False
    tm = int(round(time.time() * 1000))
    fps = 1
    fps1 = 0

    
    while True:
        # get the image at the position 955, 535 with 10 by 10 pixels
        img = pyautogui.screenshot(region=(955, 535, 10, 10))
      
        img = np.array(img)
        frame = np.array(img).sum()

        # if you press f you activate the bot or deactivate if it is already running and take the first value
        if keyboard.is_pressed('f'):
            print('Predicting...')
            frame1 = np.array(img).sum()
            if enabled == True:
                enabled = False
            else:
                enabled = True
            
            # wait 0.2 seconds in order to prevent on accidentally  double clicking
            time.sleep(0.1)

       
        if enabled == True:
            
            if frame1 > (frame+1000) or frame1 < (frame-1000): # cs:go 1000, Valorant 500
                mouse.press(Button.left)
                time.sleep(0.1)
                mouse.release(Button.left)
                enabled = False
                print('Shot')

           
            if frame1 > (frame+100) or frame1 < (frame-100): # cs:go 100, Valorant 50
                frame1 = np.array(img).sum()

       
        if int(round(time.time() * 1000))-tm > 1000:
            fps1 = fps
            tm = int(round(time.time() * 1000))
            fps = 0
        fps += 1
            
      
        r = 200.0 / img.shape[1]
        dim = (200, int(img.shape[0] * r))
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow("screenshot", img)
        if cv2.waitKey(1) == ord("q"):
            break
            cv2.destroyAllWindows()