from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
color_square = ['purple']
colors_balls = ['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
                                            'pink', 'red', 'yellow', 'violet', 'indigo', 'chartreuse',
                                            'lime']
iterations_moves = 0
balls_left = 20


class Ball(object):
    # Класс цветных шариков.
    # X, y - координаты, r - радиус
    # Color - цвет
    # vel_x, vel_y - проекции скорости на x и на y соответственно

    def __init__(self, x, y, r, color, vel_x=3, vel_y=3):
        self.color = color
        self.x = x
        self.y = y
        self.r = r
        self.vel_x = vel_x
        self.vel_y = vel_y


class Square(object):
    # Класс квадратов, второй тип мишеней
    # X, y - координаты, a - сторона
    # Color - цвет

    def __init__(self, x, y, a, color):
        self.color = color
        self.x = x
        self.y = y
        self.a = a
        self.color = color


# Список фигур, которые существуют во время одной сессии игры
balls = []
for i in range(balls_left):
    balls.append(Ball(rnd(100, 700), rnd(100, 500), rnd(30, 50), choice(colors_balls)))
squares = []
for i in range(1):
    squares.append(Square(rnd(100, 700), rnd(100, 500), rnd(30, 50), choice(color_square)))


def new_figures():
    # Отрисовывает новые шары в начале игры
    # x, y - координаты (случайные в промежутке 100-700, 100-500
    # r - радиус
    # Отрисовывает новый квадрат, x1, y1 - координаты центра квадрата, a - сторона
    canv.delete(ALL)
    for i in range(balls_left):
        canv.create_oval(balls[i].x - balls[i].r, balls[i].y - balls[i].r, balls[i].x + balls[i].r,
                         balls[i].y + balls[i].r, fill=balls[i].color, width=0)
    for i in range(1):
        canv.create_rectangle(squares[i].x - squares[i].a, squares[i].y - squares[i].a,
                              squares[i].x + squares[i].a, squares[i].y + squares[i].a, fill=squares[i].color)
    root.after(1000, balls_movements)


def balls_movements():
    global iterations_moves
    # Передвигает каждый из 10 шаров на его vel_y по вертикали, vel_x - горизонтали
    # Рисует новый квадрат, присваивая ему случайные координаты раз в 100 миллисекунд
    # Из них 45 миллисекунд квадрат доступен
    # Заканчивает игру, если все шары лопнуты или очков больше сорока
    # В случае окончания игры выводит фон + надпись
    if balls_left > 0 and point <= 40:
        iterations_moves += 1
        for i in range(balls_left):
            balls[i].y += balls[i].vel_y
            balls[i].x += balls[i].vel_x
            if balls[i].x > 800 - balls[i].r or balls[i].x < 0 + balls[i].r:
                balls[i].vel_x *= -1
            if balls[i].y > 600 - balls[i].r or balls[i].y < 0 + balls[i].r:
                balls[i].vel_y *= -1
        if iterations_moves % 100 == 0:
            for i in range(1):
                squares[i].x = rnd(100, 700)
                squares[i].y = rnd(100, 500)
                squares[i].a = rnd(30, 50)
                squares[i].color = choice(color_square)
        canv.delete(ALL)
        for i in range(balls_left):
            canv.create_oval(balls[i].x - balls[i].r, balls[i].y - balls[i].r, balls[i].x + balls[i].r,
                             balls[i].y + balls[i].r, fill=balls[i].color,
                             width=0)
        if iterations_moves % 100 in [j for j in range(0, 100)]:
            for i in range(1):
                canv.create_rectangle(squares[i].x - squares[i].a, squares[i].y - squares[i].a,
                                      squares[i].x + squares[i].a, squares[i].y + squares[i].a, fill=squares[i].color)
        # просто пишем строку, чтобы она не исчезала после каждого del(ALL)
        canv.create_text(100, 100, text='your score: ' + str(point),
                         justify=CENTER, font="Verdana 14")
        root.after(10, balls_movements)
    else:
        canv.delete(ALL)
        for i in range(100):
            colors = choicecolors = choice(['aqua', 'green', 'maroon','yellow',
                                            'violet', 'indigo', 'chartreuse',
                                            'lime'])
            x0 = rnd(0, 600)
            y0 = rnd(0, 600)
            d = rnd(0, 600.0 / 5)
            canv.create_oval(x0, y0, x0 + d, y0 + d, fill=colors)
            root.update()
        canv.create_text(400, 250, text='YOU WON!',
                         justify=CENTER, font="Verdana 42")
        canv.create_text(400, 300, text='Well, congrats, I guess',
                         justify=CENTER, font="Verdana 20")
        canv.create_text(400, 340, text='Your score: ' + str(point),
                         justify=CENTER, font="Verdana 15")
        if point <= 30:
            canv.create_text(650, 490, text='Not much though',
                             justify=CENTER, font="Verdana 10")
        if point >= 42:
            canv.create_text(650, 510, text='Like, what are you spending your life at?',
                             justify=CENTER, font="Verdana 10")


def click(event):
    # Обрабатывает клик. Если игрок попадает в шар, то количество очков увеличивается
    # Также скорость нажатого шарика увеличивается на количество очков
    # После скорости, равной 20, шар лопается
    # При попадании на квадрат от 3 до 5 очков (чем меньше, тем больше очков)
    global point
    global balls_left
    canv.create_text(100, 100, text="",
                              justify=CENTER, font="Verdana 14")
    for i in range(20):
        if ((event.x - balls[i].x) ** 2 + (event.y - balls[i].y) ** 2) ** 0.5 <= balls[i].r:
            point += 1
            balls[i].vel_x += point
            balls[i].vel_y += point
            if balls[i].vel_x > 20:
                balls[i].vel_x = 0
                balls_left -= 1
    for i in range(1):
        if (((event.x - squares[i].x) ** 2 + (event.y - squares[i].y) ** 2) ** 0.5 <= squares[i].a * 2 ** 0.5) and \
                (iterations_moves % 100 in [j for j in range(0, 100)]):
            point += round(150 / squares[i].a)
point = 0
new_figures()
canv.bind('<Button-1>', click)
mainloop()
