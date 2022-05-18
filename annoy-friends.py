import pyautogui

while True: 
    msgBox = pyautogui.confirm('Follow Mr Programmer')
    if msgBox == 'OK':
        break