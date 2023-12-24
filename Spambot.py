import pyautogui as py
import time

limit = int(input("Enter limit : "))
message = input("Message : ")
i = 0
time.sleep(5)

while i<limit:
    py.typewrite(message)
    py.press("enter")
    i+=1