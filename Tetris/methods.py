from tkinter import *
from random import randrange # берет рандомное число из полу интервало [)


W, H = 10, 13
cube_size = 45
screen_size = 750, 750


def get_record(): # получаем рекодр
    try: # пробуем просмотреть файл
        with open('record') as f: # если существует файл рекорд
            return f.readline() # то возращаем число из файл
    except FileNotFoundError: # если выдает ошибку, что такого файла нету
        with open('record', 'w') as f: # создаем файл рекорд
            f.write('0') # записываем туда 0
        return "0" # возращаем ноль


def set_record(record, score): # записываем рекорд когда проиграли
    with open('record', 'w') as f: # открываем файл record
        f.write(str(max(int(record), score))) # записываем туда максимум из уже существовашего рекорда или количества набранных очков


def rgb_to_hex(rgb): # метод для перевода название цвета из системы RGB в 8-ричную систему
    return '#%02x%02x%02x' % rgb


def get_color(): # получем рандомный цвет
    return randrange(30, 256), randrange(30, 256), randrange(30, 256)


def text_creation(screen, score, record): # отрисовываем название
    screen.create_text(505, 30, text="TETRIS", font=("WiGuru 2", 50),
                       fill="green",#(координата икс, координата игрек, текст,(шрифт, размер текста, выравнивание по левому верхнему углу)
                       anchor=NW) # слово тетрис
    screen.create_text(525, 400, text="score:", font=("WiGuru 2", 35),
                       fill="white",
                       anchor=NW)
    screen.create_text(525, 600, text="record:", font=("WiGuru 2", 35),
                       fill="blue",
                       anchor=NW)
    ts = screen.create_text(620, 450, text=str(score), font=("WiGuru 2", 35),
                            fill="white", anchor=NW)
    tr = screen.create_text(620, 660, text=record, font=("WiGuru 2", 35),
                            fill="gold", anchor=NW)
    return ts, tr


def check_borders(figure, field, i): # проверяем не вышли ли за границу
    if figure[i][0] < 0 or figure[i][0] > W - 1: # проверяем не вышли ли за границу справа или слева
        return False
    elif figure[i][1] > H - 1 or field[figure[i][1]][figure[i][0]]:# не вышли ли га зграницу по высоте и не находим ли мы на другую фигуру
        return False
    return True


def bind_buttons_arrows(gs, move_obj): # биндим стрелочки
    gs.bind_all("<KeyPress-Up>", move_obj)
    gs.bind_all("<KeyPress-Down>", move_obj)
    gs.bind_all("<KeyPress-Left>", move_obj)
    gs.bind_all("<KeyPress-Right>", move_obj)
