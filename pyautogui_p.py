import pyautogui
pyautogui.hotkey('win', 'r')
pyautogui.write(' cmd', interval=1)
pyautogui.hotkey('enter')
pyautogui.write(' ping google.com -4', interval=1)
pyautogui.hotkey('enter')
