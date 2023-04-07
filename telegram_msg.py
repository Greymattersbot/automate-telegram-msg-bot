import pyautogui as pg
import time 

time.sleep(3)

# print(pg.position())

pg.leftClick(944, 1042, 1, 1)
time.sleep(1)
pg.typewrite("web.telegram.org/z/")
time.sleep(1)
pg.press("enter")

pg.leftClick(288, 272, 1, 1)

for i in range (10):
    pg.typewrite("Hello GreyMatte's Here")
    pg.press("enter")

print("Done!")
