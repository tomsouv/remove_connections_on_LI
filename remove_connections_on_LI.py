# Name: Remove connections on LinkedIn
# Written by tomsouv (github.com/tomsouv)
# 06-17-2021

import keyboard
import time

x = 25 # Change this value to however many connections you want to remove at a time.
y = 0

keyboard.wait('q') # This is your hotkey you press to initiate the automation.

while y < x:

  keyboard.press_and_release('tab')
  time.sleep(0.25) # Change the interval to your liking, due to latency your results may vary.
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
