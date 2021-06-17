import keyboard
import time

x = 23
y = 0


keyboard.wait('q') # This is your hotkey you press to initiate the automation.

while y < x:

  keyboard.press_and_release('tab')
  time.sleep(0.25)
  keyboard.press_and_release('tab')
  time.sleep(0.25)
  keyboard.press_and_release('tab')
  time.sleep(0.25) 
  keyboard.press_and_release('alt+enter')
  time.sleep(0.25) 
  keyboard.press_and_release('down')
  time.sleep(0.25) 
  keyboard.press_and_release('enter')
  time.sleep(0.25) 
  keyboard.press_and_release('tab')
  time.sleep(0.25)
  keyboard.press_and_release('tab')
  time.sleep(0.25)
  keyboard.press_and_release('tab')
  time.sleep(0.25) 
  keyboard.press_and_release('enter')
  time.sleep(0.25)
  y += 1