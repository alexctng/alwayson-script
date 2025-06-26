#0626
import pyautogui
import time
from datetime import datetime

# Disable the fail-safe
pyautogui.FAILSAFE = False

while True:
    print("Moving mouse...")
    # move the mouse by 1 pixel
    pyautogui.move(1, 0)
    time.sleep(1)
    # move the mouse back to original position
    pyautogui.move(-1, 0)
    print("Mouse moved.")
    time.sleep(1)
    # press the 'shift' key
    pyautogui.press('shift')

    # get the current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"Key pressed at {current_time}.")
    time.sleep(300)  # sleep for 300 seconds
