import pyautogui
import cv2
import win32api, win32con
import time
import mouse
import numpy as np
from PIL import ImageGrab
from PIL import Image
from pynput.keyboard import Key, Controller

# ----------ЗАДАЧА----------
# Сделать 3 метода полной готовки на каждое место
# Делать 3 картинки
# Замерить время, нужное, чтобы клиент ушел и пришел новый
# *** Брать 4 пикселя с заказа и сравнивать с массивом цвета '/

white = cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\pixWhite.png')
red = cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\pixRed.png')
green = cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\pixGreen.png')
orange = cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\pixOrange.png')
greenRGB = cv2.cvtColor(green, cv2.COLOR_BGR2RGB)
whiteRGB = cv2.cvtColor(white, cv2.COLOR_BGR2RGB)
orangeRGB = cv2.cvtColor(orange, cv2.COLOR_BGR2RGB)
redRGB = cv2.cvtColor(red, cv2.COLOR_BGR2RGB)

whiteIceCream = cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\pixWhiteIceCream.png')
whiteIceCream1 = cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\pixWhiteIceCream2.png')
whiteIceCream2 = cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\pixWhiteIceCream3.png')
pinkIceCream = cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\pixPinkIceCream.png')
brownIceCream = cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\pixBrownIceCream.png')
brownIceCream1 = cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\pixBrownIceCream2.png')
whiteIceCreamRGB = cv2.cvtColor(whiteIceCream, cv2.COLOR_BGR2RGB)
whiteIceCreamRGB1 = cv2.cvtColor(whiteIceCream1, cv2.COLOR_BGR2RGB)
whiteIceCreamRGB2 = cv2.cvtColor(whiteIceCream2, cv2.COLOR_BGR2RGB)
pinkIceCreamRGB = cv2.cvtColor(pinkIceCream, cv2.COLOR_BGR2RGB)
brownIceCreamRGB = cv2.cvtColor(brownIceCream, cv2.COLOR_BGR2RGB)
brownIceCreamRGB1 = cv2.cvtColor(brownIceCream1, cv2.COLOR_BGR2RGB)


def TakeAScreenShot():
    image = ImageGrab.grab(bbox=(725, 286, 727, 288))
    image.save(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\coctailOrder1.png')
    image = ImageGrab.grab(bbox=(1310, 286, 1312, 288))
    image.save(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\coctailOrder2.png')
    image = ImageGrab.grab(bbox=(1890, 286, 1892, 288))
    image.save(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\coctailOrder3.png')

    image = ImageGrab.grab(bbox=(886, 239, 888, 241))
    image.save(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\iceCreamOrder1.png')
    image = ImageGrab.grab(bbox=(1474, 235, 1476, 237))
    image.save(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\iceCreamOrder2.png')
    image = ImageGrab.grab(bbox=(2052, 227, 2054, 229))
    image.save(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\iceCreamOrder3.png')


def ServeCart(pos):
    mouse.move(811, 1107, True, 0)
    mouse.click('left')
    if pos == 1:
        mouse.move(855, 800, True, 0)
    elif pos == 2:
        mouse.move(1350, 760, True, 0)
    else:
        mouse.move(1860, 777, True, 0)
    mouse.click('left')
    print("#4/5 We have put a cart on a table")


def MakeGreenCoctail(pos):
    mouse.move(595, 1230, True, 0)
    mouse.click('left')
    if pos == 1:
        mouse.move(855, 800, True, 0)
        mouse.click('left')
        mouse.move(640, 950, True, 0)
        mouse.click('left')
        mouse.move(715, 722, True, 0)
        mouse.click('left')
    elif pos == 2:
        mouse.move(1350, 760, True, 0)
        mouse.click('left')
        mouse.move(640, 950, True, 0)
        mouse.click('left')
        mouse.move(1210, 690, True, 0)
        mouse.click('left')
    else:
        mouse.move(1860, 777, True, 0)
        mouse.click('left')
        mouse.move(640, 950, True, 0)
        mouse.click('left')
        mouse.move(1720, 716, True, 0)
        mouse.click('left')


def MakeRedCoctail(pos):
    mouse.move(595, 1230, True, 0)
    mouse.click('left')
    if pos == 1:
        mouse.move(855, 800, True, 0)
        mouse.click('left')
        mouse.move(705, 900, True, 0)
        mouse.click('left')
        mouse.move(715, 722, True, 0)
        mouse.click('left')
    elif pos == 2:
        mouse.move(1350, 760, True, 0)
        mouse.click('left')
        mouse.move(705, 900, True, 0)
        mouse.click('left')
        mouse.move(1210, 690, True, 0)
        mouse.click('left')
    else:
        mouse.move(1860, 777, True, 0)
        mouse.click('left')
        mouse.move(705, 900, True, 0)
        mouse.click('left')
        mouse.move(1720, 716, True, 0)
        mouse.click('left')


def MakeOrangeCoctail(pos):
    mouse.move(595, 1230, True, 0)
    mouse.click('left')
    if pos == 1:
        mouse.move(855, 800, True, 0)
        mouse.click('left')
        mouse.move(510, 950, True, 0)
        mouse.click('left')
        mouse.move(715, 722, True, 0)
        mouse.click('left')
    elif pos == 2:
        mouse.move(1350, 760, True, 0)
        mouse.click('left')
        mouse.move(510, 950, True, 0)
        mouse.click('left')
        mouse.move(1210, 690, True, 0)
        mouse.click('left')
    else:
        mouse.move(1860, 777, True, 0)
        mouse.click('left')
        mouse.move(510, 950, True, 0)
        mouse.click('left')
        mouse.move(1720, 716, True, 0)
        mouse.click('left')


def MakeWhiteCoctail(pos):
    mouse.move(595, 1230, True, 0)
    mouse.click('left')
    if pos == 1:
        mouse.move(855, 800, True, 0)
        mouse.click('left')
        mouse.move(575, 900, True, 0)
        mouse.click('left')
        mouse.move(715, 722, True, 0)
        mouse.click('left')
    elif pos == 2:
        mouse.move(1350, 760, True, 0)
        mouse.click('left')
        mouse.move(575, 900, True, 0)
        mouse.click('left')
        mouse.move(1210, 690, True, 0)
        mouse.click('left')
    else:
        mouse.move(1860, 777, True, 0)
        mouse.click('left')
        mouse.move(575, 900, True, 0)
        mouse.click('left')
        mouse.move(1720, 716, True, 0)
        mouse.click('left')


def makeIceCream(pos, iceCream):
    mouse.move(1730, 1080, True, 0)
    mouse.click('left')
    if iceCream == "Pink":
        if pos == 1:
            mouse.move(1018, 786, True, 0)
            mouse.click('left')
            mouse.move(2010, 1130, True, 0)
            mouse.click('left')
            mouse.move(1018, 786, True, 0)
            mouse.click('left')
        elif pos == 2:
            mouse.move(1515, 747, True, 0)
            mouse.click('left')
            mouse.move(2010, 1130, True, 0)
            mouse.click('left')
            mouse.move(1515, 747, True, 0)
            mouse.click('left')
        else:
            mouse.move(2021, 767, True, 0)
            mouse.click('left')
            mouse.move(2010, 1130, True, 0)
            mouse.click('left')
            mouse.move(2021, 767, True, 0)
            mouse.click('left')
    elif iceCream == "Brown":
        if pos == 1:
            mouse.move(1018, 786, True, 0)
            mouse.click('left')
            mouse.move(1945, 1050, True, 0)
            mouse.click('left')
            mouse.move(1018, 786, True, 0)
            mouse.click('left')
        elif pos == 2:
            mouse.move(1515, 747, True, 0)
            mouse.click('left')
            mouse.move(1945, 1050, True, 0)
            mouse.click('left')
            mouse.move(1515, 747, True, 0)
            mouse.click('left')
        else:
            mouse.move(2021, 767, True, 0)
            mouse.click('left')
            mouse.move(1945, 1050, True, 0)
            mouse.click('left')
            mouse.move(2021, 767, True, 0)
            mouse.click('left')
    else:
        if pos == 1:
            mouse.move(1018, 786, True, 0)
            mouse.click('left')
            mouse.move(1830, 1080, True, 0)
            mouse.click('left')
            mouse.move(1018, 786, True, 0)
            mouse.click('left')
        elif pos == 2:
            mouse.move(1515, 747, True, 0)
            mouse.click('left')
            mouse.move(1830, 1080, True, 0)
            mouse.click('left')
            mouse.move(1515, 747, True, 0)
            mouse.click('left')
        else:
            mouse.move(2021, 767, True, 0)
            mouse.click('left')
            mouse.move(1830, 1080, True, 0)
            mouse.click('left')
            mouse.move(2021, 767, True, 0)
            mouse.click('left')


def CheckCoctailPos1():
    coctail = cv2.cvtColor(
        cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\coctailOrder1.png'),
        cv2.COLOR_BGR2RGB)
    pos = 1
    flag = True
    for i in range(0, coctail.size // coctail[0].size):
        for j in range(0, coctail[0].size // coctail[0][0].size):
            for k in range(0, 3):
                if greenRGB[i][j][k] != coctail[i][j][k]:
                    flag = False
    if flag:
        MakeGreenCoctail(pos)
    else:
        flag = True
        for i in range(0, coctail.size // coctail[0].size):
            for j in range(0, coctail[0].size // coctail[0][0].size):
                for k in range(0, 3):
                    if redRGB[i][j][k] != coctail[i][j][k]:
                        flag = False
        if flag:
            MakeRedCoctail(pos)
        else:
            flag = True
            for i in range(0, coctail.size // coctail[0].size):
                for j in range(0, coctail[0].size // coctail[0][0].size):
                    for k in range(0, 3):
                        if orangeRGB[i][j][k] != coctail[i][j][k]:
                            flag = False
            if flag:
                MakeOrangeCoctail(pos)
            else:
                flag = True
                for i in range(0, coctail.size // coctail[0].size):
                    for j in range(0, coctail[0].size // coctail[0][0].size):
                        for k in range(0, 3):
                            if whiteRGB[i][j][k] != coctail[i][j][k]:
                                flag = False
                if flag:
                    MakeWhiteCoctail(pos)
                else:
                    time.sleep(0.15)


def CheckIceCreamPos1():
    iceCream = cv2.cvtColor(
        cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\iceCreamOrder1.png'),
        cv2.COLOR_BGR2RGB)
    pos = 1
    flag = True
    for i in range(0, iceCream.size // iceCream[0].size):
        for j in range(0, iceCream[0].size // iceCream[0][0].size):
            for k in range(0, 3):
                if whiteIceCreamRGB[i][j][k] != iceCream[i][j][k]:
                    flag = False
    if flag:
        makeIceCream(pos, "White")
        print("Making White IceCream pos1")
    else:
        flag = True
        for i in range(0, iceCream.size // iceCream[0].size):
            for j in range(0, iceCream[0].size // iceCream[0][0].size):
                for k in range(0, 3):
                    if brownIceCreamRGB[i][j][k] != iceCream[i][j][k]:
                        flag = False
        if flag:
            makeIceCream(pos, "Brown")
            print("Making Broown IceCream pos1")
        else:
            flag = True
            for i in range(0, iceCream.size // iceCream[0].size):
                for j in range(0, iceCream[0].size // iceCream[0][0].size):
                    for k in range(0, 3):
                        if pinkIceCreamRGB[i][j][k] != iceCream[i][j][k]:
                            flag = False
            if flag:
                makeIceCream(pos, "Pink")
                print("Making Pink IceCream pos1")
            else:
                flag = True
                for i in range(0, iceCream.size // iceCream[0].size):
                    for j in range(0, iceCream[0].size // iceCream[0][0].size):
                        for k in range(0, 3):
                            if brownIceCreamRGB1[i][j][k] != iceCream[i][j][k]:
                                flag = False
                if flag:
                    makeIceCream(pos, "Brown")
                    print("Making Broown2 IceCream pos1")
                else:
                    flag = True
                    for i in range(0, iceCream.size // iceCream[0].size):
                        for j in range(0, iceCream[0].size // iceCream[0][0].size):
                            for k in range(0, 3):
                                if whiteIceCreamRGB1[i][j][k] != iceCream[i][j][k]:
                                    flag = False
                    if flag:
                        makeIceCream(pos, "White")
                        print("Making White2 IceCream pos1")
                    else:
                        flag = True
                        for i in range(0, iceCream.size // iceCream[0].size):
                            for j in range(0, iceCream[0].size // iceCream[0][0].size):
                                for k in range(0, 3):
                                    if whiteIceCreamRGB2[i][j][k] != iceCream[i][j][k]:
                                        flag = False
                        if flag:
                            makeIceCream(pos, "White")
                            print("Making White3 IceCream pos1")
                        else:
                            print("No IceCream pos1")
                            time.sleep(0.15)


def CheckCoctailPos2():
    coctail = cv2.cvtColor(
        cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\coctailOrder2.png'),
        cv2.COLOR_BGR2RGB)
    pos = 2
    flag = True
    for i in range(0, coctail.size // coctail[0].size):
        for j in range(0, coctail[0].size // coctail[0][0].size):
            for k in range(0, 3):
                if greenRGB[i][j][k] != coctail[i][j][k]:
                    flag = False
    if flag:
        MakeGreenCoctail(pos)
    else:
        flag = True
        for i in range(0, coctail.size // coctail[0].size):
            for j in range(0, coctail[0].size // coctail[0][0].size):
                for k in range(0, 3):
                    if redRGB[i][j][k] != coctail[i][j][k]:
                        flag = False
        if flag:
            MakeRedCoctail(pos)
        else:
            flag = True
            for i in range(0, coctail.size // coctail[0].size):
                for j in range(0, coctail[0].size // coctail[0][0].size):
                    for k in range(0, 3):
                        if orangeRGB[i][j][k] != coctail[i][j][k]:
                            flag = False
            if flag:
                MakeOrangeCoctail(pos)
            else:
                flag = True
                for i in range(0, coctail.size // coctail[0].size):
                    for j in range(0, coctail[0].size // coctail[0][0].size):
                        for k in range(0, 3):
                            if whiteRGB[i][j][k] != coctail[i][j][k]:
                                flag = False
                if flag:
                    MakeWhiteCoctail(pos)
                else:
                    time.sleep(0.15)


def CheckiceCreamPos2():
    iceCream = cv2.cvtColor(
        cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\iceCreamOrder2.png'),
        cv2.COLOR_BGR2RGB)
    pos = 2
    flag = True
    for i in range(0, iceCream.size // iceCream[0].size):
        for j in range(0, iceCream[0].size // iceCream[0][0].size):
            for k in range(0, 3):
                if whiteIceCreamRGB[i][j][k] != iceCream[i][j][k]:
                    flag = False
    if flag:
        makeIceCream(pos, "White")
        print("Making White IceCream pos2")
    else:
        flag = True
        for i in range(0, iceCream.size // iceCream[0].size):
            for j in range(0, iceCream[0].size // iceCream[0][0].size):
                for k in range(0, 3):
                    if brownIceCreamRGB[i][j][k] != iceCream[i][j][k]:
                        flag = False
        if flag:
            makeIceCream(pos, "Brown")
            print("Making Broown IceCream pos2")
        else:
            flag = True
            for i in range(0, iceCream.size // iceCream[0].size):
                for j in range(0, iceCream[0].size // iceCream[0][0].size):
                    for k in range(0, 3):
                        if pinkIceCreamRGB[i][j][k] != iceCream[i][j][k]:
                            flag = False
            if flag:
                makeIceCream(pos, "Pink")
                print("Making Pink IceCream pos2")
            else:
                flag = True
                for i in range(0, iceCream.size // iceCream[0].size):
                    for j in range(0, iceCream[0].size // iceCream[0][0].size):
                        for k in range(0, 3):
                            if brownIceCreamRGB1[i][j][k] != iceCream[i][j][k]:
                                flag = False
                if flag:
                    makeIceCream(pos, "Brown")
                    print("Making Broown2 IceCream pos2")
                else:
                    flag = True
                    for i in range(0, iceCream.size // iceCream[0].size):
                        for j in range(0, iceCream[0].size // iceCream[0][0].size):
                            for k in range(0, 3):
                                if whiteIceCreamRGB1[i][j][k] != iceCream[i][j][k]:
                                    flag = False
                    if flag:
                        makeIceCream(pos, "White")
                        print("Making White2 IceCream pos2")
                    else:
                        flag = True
                        for i in range(0, iceCream.size // iceCream[0].size):
                            for j in range(0, iceCream[0].size // iceCream[0][0].size):
                                for k in range(0, 3):
                                    if whiteIceCreamRGB2[i][j][k] != iceCream[i][j][k]:
                                        flag = False
                        if flag:
                            makeIceCream(pos, "White")
                            print("Making White3 IceCream pos2")
                        else:
                            print("No IceCream pos2")
                            time.sleep(0.15)


def CheckCoctailPos3():
    coctail = cv2.cvtColor(
        cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\coctailOrder3.png'),
        cv2.COLOR_BGR2RGB)
    pos = 3
    flag = True
    for i in range(0, coctail.size // coctail[0].size):
        for j in range(0, coctail[0].size // coctail[0][0].size):
            for k in range(0, 3):
                if greenRGB[i][j][k] != coctail[i][j][k]:
                    flag = False
    if flag:
        MakeGreenCoctail(pos)
    else:
        flag = True
        for i in range(0, coctail.size // coctail[0].size):
            for j in range(0, coctail[0].size // coctail[0][0].size):
                for k in range(0, 3):
                    if redRGB[i][j][k] != coctail[i][j][k]:
                        flag = False
        if flag:
            MakeRedCoctail(pos)
        else:
            flag = True
            for i in range(0, coctail.size // coctail[0].size):
                for j in range(0, coctail[0].size // coctail[0][0].size):
                    for k in range(0, 3):
                        if orangeRGB[i][j][k] != coctail[i][j][k]:
                            flag = False
            if flag:
                MakeOrangeCoctail(pos)
            else:
                flag = True
                for i in range(0, coctail.size // coctail[0].size):
                    for j in range(0, coctail[0].size // coctail[0][0].size):
                        for k in range(0, 3):
                            if whiteRGB[i][j][k] != coctail[i][j][k]:
                                flag = False
                if flag:
                    MakeWhiteCoctail(pos)
                else:
                    time.sleep(0.15)


def CheckIceCreamPos3():
    iceCream = cv2.cvtColor(
        cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\iceCreamOrder3.png'),
        cv2.COLOR_BGR2RGB)
    pos = 3
    flag = True
    for i in range(0, iceCream.size // iceCream[0].size):
        for j in range(0, iceCream[0].size // iceCream[0][0].size):
            for k in range(0, 3):
                if whiteIceCreamRGB[i][j][k] != iceCream[i][j][k]:
                    flag = False
    if flag:
        makeIceCream(pos, "White")
        print("Making White IceCream pos3")
    else:
        flag = True
        for i in range(0, iceCream.size // iceCream[0].size):
            for j in range(0, iceCream[0].size // iceCream[0][0].size):
                for k in range(0, 3):
                    if brownIceCreamRGB[i][j][k] != iceCream[i][j][k]:
                        flag = False
        if flag:
            makeIceCream(pos, "Brown")
            print("Making Broown IceCream pos3")
        else:
            flag = True
            for i in range(0, iceCream.size // iceCream[0].size):
                for j in range(0, iceCream[0].size // iceCream[0][0].size):
                    for k in range(0, 3):
                        if pinkIceCreamRGB[i][j][k] != iceCream[i][j][k]:
                            flag = False
            if flag:
                makeIceCream(pos, "Pink")
                print("Making Pink IceCream pos3")
            else:
                flag = True
                for i in range(0, iceCream.size // iceCream[0].size):
                    for j in range(0, iceCream[0].size // iceCream[0][0].size):
                        for k in range(0, 3):
                            if brownIceCreamRGB1[i][j][k] != iceCream[i][j][k]:
                                flag = False
                if flag:
                    makeIceCream(pos, "Brown")
                    print("Making Broown2 IceCream pos3")
                else:
                    flag = True
                    for i in range(0, iceCream.size // iceCream[0].size):
                        for j in range(0, iceCream[0].size // iceCream[0][0].size):
                            for k in range(0, 3):
                                if whiteIceCreamRGB1[i][j][k] != iceCream[i][j][k]:
                                    flag = False
                    if flag:
                        makeIceCream(pos, "White")
                        print("Making White2 IceCream pos3")
                    else:
                        flag = True
                        for i in range(0, iceCream.size // iceCream[0].size):
                            for j in range(0, iceCream[0].size // iceCream[0][0].size):
                                for k in range(0, 3):
                                    if whiteIceCreamRGB2[i][j][k] != iceCream[i][j][k]:
                                        flag = False
                        if flag:
                            makeIceCream(pos, "White")
                            print("Making White3 IceCream pos3")
                        else:
                            print("No IceCream pos3")
                            time.sleep(0.15)


def restart():
    # mouse.move(1400, 930, True, 0)
    # mouse.click('left')
    # time.sleep(1)
    mouse.move(2316, 194, True, 0)
    mouse.click('left')
    time.sleep(1)
    mouse.move(1400, 1160, True, 0)
    mouse.click('left')
    time.sleep(4)
    mouse.move(1400, 1140, True, 0)
    mouse.click('left')
    time.sleep(0.5)
    mouse.move(2293, 262, True, 0)
    mouse.click('left')
    time.sleep(0.5)
    mouse.move(2000, 310, True, 0)
    mouse.click('left')
    time.sleep(0.75)
    mouse.move(1260, 860, True, 0)
    mouse.click('left')
    time.sleep(4)
    mouse.move(1330, 1060, True, 0)
    mouse.click('left')
    time.sleep(1)
    mouse.move(1450, 617, True, 0)
    mouse.click('left')
    runBar()


def runBar():
    # ДЛЯ ТЕСТОВ:
    # iceCream = cv2.cvtColor(
    #     cv2.imread(r'C:\Users\stena\PycharmProjects\learningPython\venv\tempScreenshot\iceCreamOrder3.png'),
    #     cv2.COLOR_BGR2RGB)
    # print(iceCream)
    # print(whiteIceCreamRGB1)

    time.sleep(8)
    count = 0
    timeCount = 0
    while count <= 2:
        TakeAScreenShot()
        ServeCart(1)
        ServeCart(2)
        ServeCart(3)
        CheckIceCreamPos1()
        CheckiceCreamPos2()
        CheckIceCreamPos3()
        CheckCoctailPos1()
        CheckCoctailPos2()
        CheckCoctailPos3()
        count += 1
        timeCount += 1
        if timeCount <= 2:
            time.sleep(8.5)
        else:
            time.sleep(0)
    restart()

    # coctail, pos = CheckCoctails(template)
    # if coctail == 'none':
    #     run()
    # else:
    #     MakeCoctails(coctail, pos)

    # while win32con.MOUSEEVENTF_LEFTDOWN:
    #     x, y = win32api.GetCursorPos()
    #     print(x, y)


def runKrosh():
    keyboard = Controller()
    keyboard.press(Key.right)
    time.sleep(0.22)
    keyboard.release(Key.right)
    time.sleep(0.05)
    keyboard.press(Key.up)
    time.sleep(0.2)
    keyboard.press(Key.left)
    time.sleep(0.6)
    keyboard.release(Key.up)
    keyboard.release(Key.left)


if __name__ == "__main__":
    time.sleep(3)
    runBar()
