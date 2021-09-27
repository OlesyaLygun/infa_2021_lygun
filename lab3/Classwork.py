from graph import *
from math import *


def ellipse(x0, y0, r, h=1.0, rot=0):
    #рисует повернутый овал
    points = []
    nPoints = int(max(r, r * h))
    rot = rot * pi / 180
    k = 2 * pi / nPoints
    for i in range(0, nPoints):
        alfa = i * k
        x = r * cos(alfa)
        y = r * sin(alfa) * h
        if rot != 0:
            x, y = x * cos(rot) - y * sin(rot), x * sin(rot) + y * cos(rot)
        x += x0
        y += y0
        points.append([x, y])
    return polygon(points)


windowSize(1000, 600)
canvasSize(800, 550)
brushColor(255, 176, 129)
circle(0, 0, 1000)

# третий бамбук
brushColor(0, 104, 52)
penColor(0, 104, 52)
rectangle(396, 277, 420, 370)
rectangle(396, 167, 420, 260)
penSize(20)
line(417, 90, 400, 154)
penSize(10)
line(434, 11, 409, 84)
penSize(1.5)
arc(400, 1, 800, 400, 90, 145, ARC)
ellipse(495, 65, 25, 0.15, 75)
ellipse(530, 50, 25, 0.15, 75)
ellipse(550, 45, 25, 0.15, 75)
ellipse(570, 30, 25, 0.15, 75)
ellipse(590, 30, 25, 0.15, 75)
arc(410, 130, 600, 380, 70, 145, ARC)
ellipse(480, 160, 25, 0.15, 75)
ellipse(500, 155, 25, 0.15, 75)
ellipse(520, 155, 25, 0.15, 75)
arc(150, 180, 450, 700, 55, 110, ARC)
ellipse(280, 210, 25, 0.15, 110)
ellipse(300, 210, 25, 0.15, 110)
ellipse(320, 215, 25, 0.15, 110)
arc(-100, 50, 450, 450, 40, 90, ARC)
ellipse(190, 80, 25, 0.15, 110)
ellipse(210, 80, 25, 0.15, 110)
ellipse(230, 90, 25, 0.15, 110)
ellipse(250, 95, 25, 0.15, 110)
ellipse(280, 100, 25, 0.15, 110)

# второй бамбук
rectangle(260, 330, 270, 400)
rectangle(260, 260, 270, 320)
penSize(7)
line(265, 250, 270, 200)
penSize(6)
line(267, 195, 275, 135)
penSize(1.5)
arc(270, 130, 440, 470, 100, 145, ARC)
ellipse(315, 175, 20, 0.08, 80)
ellipse(325, 165, 20, 0.08, 80)
ellipse(330, 160, 20, 0.08, 80)
ellipse(335, 155, 20, 0.08, 80)
ellipse(341, 155, 20, 0.08, 80)
arc(270, 230, 370, 390, 70, 160, ARC)
ellipse(320, 250, 20, 0.08, 80)
ellipse(330, 250, 20, 0.08, 80)
ellipse(310, 255, 20, 0.08, 80)
arc(130, 250, 300, 750, 50, 100, ARC)
ellipse(220, 270, 20, 0.08, 110)
ellipse(230, 280, 20, 0.08, 110)
ellipse(210, 270, 20, 0.08, 110)
arc(100, 170, 285, 520, 40, 100, ARC)
ellipse(190, 193, 20, 0.08, 110)
ellipse(180, 190, 20, 0.08, 110)
ellipse(200, 198, 20, 0.08, 110)
ellipse(210, 203, 20, 0.08, 110)
ellipse(230, 213, 20, 0.08, 110)

# четвертый бамбук
rectangle(700, 260, 715, 350)
rectangle(700, 165, 715, 250)
penSize(10)
line(705, 160, 712, 100)
penSize(5)
line(713, 95, 720, 30)
penSize(2)
arc(700, 20, 870, 525, 85, 137, ARC)
ellipse(750, 75, 20, 0.1, 80)
ellipse(762, 55, 20, 0.1, 80)
ellipse(770, 50, 20, 0.1, 80)
ellipse(778, 42, 20, 0.1, 80)
ellipse(789, 43, 20, 0.1, 80)
arc(715, 130, 780, 290, 70, 160, ARC)
ellipse(740, 155, 20, 0.1, 80)
ellipse(750, 150, 20, 0.1, 80)
ellipse(760, 155, 20, 0.1, 80)
arc(715, 155, 600, 645, 45, 105, ARC)
ellipse(660, 180, 20, 0.1, 100)
ellipse(670, 185, 20, 0.1, 100)
ellipse(650, 175, 20, 0.1, 100)
arc(700, 60, 480, 230, 0, 70, ARC)
ellipse(655, 100, 20, 0.1, 100)
ellipse(670, 110, 20, 0.1, 100)
ellipse(648, 94, 20, 0.1, 100)
ellipse(640, 90, 20, 0.1, 100)
ellipse(632, 87, 20, 0.1, 100)

# первый бамбук
rectangle(80, 340, 93, 400)
rectangle(80, 270, 93, 330)
penSize(9)
line(85, 259, 90, 215)
penSize(6)
line(90, 210, 97, 155)
penSize(2)
arc(80, 160, 275, 420, 100, 145, ARC)
ellipse(125, 200, 15, 0.1, 80)
ellipse(138, 190, 15, 0.1, 80)
ellipse(145, 185, 15, 0.1, 80)
ellipse(153, 180, 15, 0.1, 80)
ellipse(160, 180, 15, 0.1, 80)
arc(85, 250, 175, 490, 70, 140, ARC)
ellipse(120, 270, 15, 0.1, 80)
ellipse(128, 265, 15, 0.1, 80)
ellipse(136, 265, 15, 0.1, 80)
arc(85, 180, -105, 380, 20, 80, ARC)
ellipse(20, 200, 15, 0.1, 100)
ellipse(28, 205, 15, 0.1, 100)
ellipse(36, 210, 15, 0.1, 100)
ellipse(44, 213, 15, 0.1, 100)
ellipse(55, 225, 15, 0.1, 100)
arc(85, 280, 0, 430, 35, 110, ARC)
ellipse(50, 300, 15, 0.1, 100)
ellipse(40, 295, 15, 0.1, 100)
ellipse(30, 300, 15, 0.1, 100)

# панда болбшая.......
penColor('white')
brushColor('white')
oval(470, 270, 670, 380)
penColor('black')
brushColor('black')
polygon([(600, 270), (600, 395), (590, 460), (560, 480), (540, 440), (590, 275)])
arc(500, 430, 580, 483, 0, 350, PIESLICE)
arc(460, 290, 520, 510, -10, 200, CHORD)
arc(460, 415, 535, 450, 55, 250, CHORD)
ellipse(640, 380, 80, 0.3, 105)
arc(580, 395, 780, 463, 120, 235, CHORD)
polygon([(617, 375), (597, 420), (630, 375)])
penColor('white')
brushColor('white')
ellipse(535, 320, 60, 0.8, 165)
polygon([(560, 360), (593, 335), (593, 260), (540, 270)])
ellipse(515, 300, 60, 0.75, 90)
ellipse(530, 290, 65, 0.5, 100)
polygon([(500, 243), (535, 224), (520, 250)])
polygon([(547, 227), (593, 263), (560, 270)])
penColor('black')
brushColor('black')
ellipse(490, 355, 20, 0.5)
ellipse(480, 310, 18, 0.7, 90)
ellipse(525, 315, 18)
arc(550, 220, 600, 290, -60, 145, CHORD)
ellipse(480, 250, 30, 0.5, 130)
polygon([(460, 273), (475, 280), (490, 260)])

# панда поменьбше
penColor('white')
brushColor('white')
oval(320, 410, 420, 470)
penColor('black')
brushColor('black')
arc(355, 440, 435, 485, -90, 50, PIESLICE)
arc(370, 420, 395, 492, -10, 180, PIESLICE)
polygon([(395, 461), (365, 485), (355, 460), (377, 435)])
arc(338, 460, 363, 515, 5, 180, CHORD)
arc(310, 420, 330, 485, 190, 330, CHORD)
polygon([(310, 460), (325, 410), (320, 470)])
penColor('white')
brushColor('white')
ellipse(340, 435, 30, 0.5, 110)
polygon([(323, 450), (323, 420), (350, 405)])
polygon([(340, 465), (345, 465), (370, 450), (370, 435)])
penColor('black')
brushColor('black')
ellipse(330, 415, 13, 0.6, 130)
ellipse(365, 420, 13, 0.6, 80)
ellipse(325, 440, 8, 0.6, 80)
circle(345, 443, 7)
ellipse(325, 460, 8, 0.6)
run()
