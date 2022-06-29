from methods import *  # импорт всего methods
from tkinter import *  # импорт всего tkinter
from random import choice  # импорт choice который рандомно выбирает элемент
from copy import deepcopy  # импорт deepcopy, который делает полную копию
from time import sleep  # импорт sleep, который создает задержку


def move_obj(event):  # метод, анализирующий нажатие стрелок
    global rotate, anim_limit, move_on_x_coord  # используем глобальные переменные
    if event.keysym == 'Up':  # если нажата стрелка вверх
        rotate = True  # хотим повернуть фигуру
    elif event.keysym == 'Down':  # если нажата стрелка вниз
        anim_limit = 100  # понижаем максимальный путь, чтобы в строке 93 сработала проверка, чтобы наша фигура упала вниз
    elif event.keysym == 'Left':  # если нажата стрелка влево
        move_on_x_coord = -1  # отнимаем из координаты икс 1
    elif event.keysym == 'Right':  # если нажата вправо
        move_on_x_coord = 1  # прибавляем к координате икс 1


W = 10  # количество клеток по ширине
H = 13  # количество клеток по высоте
cube_size = 45  # размер клетки
screen_size = 750, 650  # размер окна
game_screen_size = W * cube_size, H * cube_size  # размер клеточного поля
app_running = True  # отвечает за не проиграли ли мы пока
move_on_x_coord, rotate = 0, False

tk = Tk()  # создаем экземпляр tkinter
tk.title("Tetris")  # создаем название кона
tk.resizable(False, False)  # задаем, что нельзя изменить экран
tk.iconbitmap("img/tetris_icon.ico")  # задаем иконку окну
screen = Canvas(tk, width=screen_size[0], height=screen_size[1],
                highlightthickness=0)  # создаем экран в нашем экземпляре tk, с шириной screen_size[0], с высотой height=screen_size[1], без контура, то есть highlightthickness = 0
screen.pack()  # отрисовываем наш экран

game_screen = Canvas(tk, width=game_screen_size[0] + 1,
                     height=game_screen_size[1] + 1,
                     highlightthickness=0)  # так же как и экран создаем наше игровое поле
game_screen.place(x=20, y=20, anchor=NW)  # отрисовываем его, смещая по иксу на 20 и по игреку на 20, и выравниваем по верхнему левому углу, то есть anchor=NW

img1 = PhotoImage(file="img/backck.png")  # создаем экземпляр картинки нашего основного заднего фона
screen.create_image(0, 0, anchor=NW, image=img1)  # устанавливаем задний фон

img2 = PhotoImage(file="img/cube_back.png")  # создаем экземпляр картинки нашего игрового заднего фона
game_screen.create_image(0, 0, anchor=NW, image=img2)  # устанавливаем игровой задний фон

grid = []  # создаем сетку
for x in range(W):  # пробегаемся по столбцам
    for y in range(H):  # пробегаемся по каждой клетке
        grid.append(game_screen.create_rectangle(x * cube_size, y * cube_size,
                                                 # отрисовываем нашу клетку, где x * cube_size, y * cube_size координаты верхнего левого угла
                                                 x * cube_size + cube_size,
                                                 # x * cube_size + cube_size, y * cube_size + cube_size координаты нижнего правого угла
                                                 y * cube_size + cube_size))
figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],  # каждая строчка это фигура
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               # так как фигура состоит 4 квадратов(клеток)
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               # то в каждой строке записаны координаты верхнего левого угла каждого квадрата
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               # если рассматривать от начала координат(точки (0,0))
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]
figures = []  # создаем массив для позиций наших фигур на сетке
for position in figures_pos:  # берем каждую позицию
    a = []  # создаем массив для каждой фигуру
    for x, y in position:  # берем координаты угла каждого квадрата нашей фигуры
        a.append([x + W // 2, y + 1])  # добавляем в массив координаты угла на сетке
    figures.append(a.copy())  # добавляем координаты каждой фигуры в массив координат всех фигур
field = []  # создаем массив для логики нашего поля
for i in range(H):  # пробигаемся по строкам
    field.append([0] * W)  # заполняем каждую клетку нулями, так как в начале игры поле пустое
anim_count, anim_speed, anim_limit = 0, 60, 2000  # 1.наш пройденный путь, 2. скорость, 3. весь путь

score = 0  # количество набранных очков
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}  # словарь, где записано, сколько можно набарть, если заполнить за раз 0,1,2,3,4 строк
record = '0'  # наш рекорд

text_score, text_record = text_creation(screen, score, record)  # отрисовываем текст

figure, next_figure = deepcopy(choice(figures)), deepcopy(
    choice(figures))  # рандомно выбираем первую и следующую фигуру
color, next_color = get_color(), get_color()  # рандомно выбираем цвет для первой и следующей фигур

bind_buttons_arrows(game_screen, move_obj)  # биндим кнопки управления
while app_running:  # пока мы не проиграли
    if app_running:  # если мы не проиграли
        record = get_record()  # получаем из сохранения рекорд
        # движение вправо/влево
        figure_old = deepcopy(figure)  # делаем точку восстановления для нашей фигуры
        if move_on_x_coord != 0:  # если мы нажали правую/левую стрелочку
            for i in range(4):  # пробегаемся по каждому квадратуку
                figure[i][0] += move_on_x_coord  # передвигаем квадрат, в взависимости на какую стрелку мы нажали
                if not check_borders(figure, field, i):  # проверяем не выходил ли квадрат за границу
                    figure = deepcopy(figure_old)  # если выходит, то возращаемся на точку восстановления
                    break  # прекращаем пробегатся по квадратам
        # движение вниз
        anim_count += anim_speed  # преодолели одну клетку
        if anim_count > anim_limit:  # если наш пройденный путь больше максимального
            anim_count = 0  # обнуляем наш путь
            figure_old = deepcopy(figure)  # делаем точку восстановления для нашей фигуры
            for i in range(4):  # пробегаемся по каждому квадратуку
                figure[i][1] += 1  # опускаем каждый квадрат вниз
                if not check_borders(figure, field, i):  # если вниз больше не возможно опускаться
                    for j in range(4):
                        field[figure_old[j][1]][figure_old[j][0]] = color  # то на месте нашей фигуры фиксируем цвет
                    figure, color = next_figure, next_color  # следующая фигура становится нынешней, то же самое с цветом
                    next_figure, next_color = deepcopy(choice(figures)), get_color()  # выбираем следующую фигуруру и ее цвет
                    anim_limit = 2000  # восстанавлиаем макс путь
                    break  # перестаем пробигаться по квадратам
        # если хотим покрутить фигуру
        center = figure[0]  # фиксируем положение фигуры
        figure_old = deepcopy(figure)  # делаем точку восстановления для нашей фигуры
        if rotate:  # если нажали стрелочку вверх
            for i in range(4):  # пробигаемся по каждому квадрату
                x = figure[i][1] - center[1]
                y = figure[i][0] - center[0]
                figure[i][0] = center[0] - x
                figure[i][1] = center[1] + y  # эти 4 строки поворачивают квадрат по часовой
                if not check_borders(figure, field, i):  # если квадрат вышел за границу
                    figure = deepcopy(figure_old)  # возращаемся к точке восстановления
                    break  # перестаем пробигаться
        # проверяем заполнили ли строки
        line, lines = H - 1, 0  # количество всего строк, количество заполненных
        for row in range(H - 1, -1, -1):  # пробигаемся по строкам
            count = 0  # счетчик заполненных клеток
            for i in range(W):  # пробигаемся по каждой клетке
                if field[row][i]:  # если заполнено, то прибавляем к счетчик
                    count += 1
                field[line][i] = field[row][i]  # пада верхняя клетка, так как наша удаляется
            if count < W:  # количество заполненных клеток меньше ширины
                line -= 1  # отнимаем количество всех строк
            else:  # иначе
                anim_speed += 3  # увеличиваем скорость
                lines += 1  # количестов заполненных строк увеличиваем
        # прибавляем очки
        score += scores[lines]  # прибавляем количество заработанных очков

        fig = []  # создаем массив для отрисовки нашей фигуры
        # отрисовываем нашу фигуру
        for i in range(4):  # пробигаемся по каждому квадрату
            x = figure[i][0] * cube_size  # икс координата верхнего угла
            y = figure[i][1] * cube_size  # игрек координата верхнего угла
            fig.append(
                game_screen.create_rectangle(x, y,
                                             x + cube_size,
                                             y + cube_size,
                                             fill=rgb_to_hex(color)))  # отрисовывваем и закрашиваем нашу клетку

        # отрисовываем опустившуюся фигуру
        for y, raw in enumerate(field):  # пробигаемся по строкам благодаря enumerate получаем значения y и raw = field[x]
            for x, col in enumerate(raw):  # пробигаемся по клетке благодаря enumerate получаем значения x и col = raw[y](field[x][y])
                if col:
                    fx, fy = x * cube_size, y * cube_size
                    fig.append(
                        game_screen.create_rectangle(fx,
                                                     fy,
                                                     fx + cube_size,
                                                     fy + cube_size,
                                                     fill=rgb_to_hex(col)))

        nfigure = []  # создаем массив для отрисовки сл фигуры
        # отрисовываем сл фигуру справа
        for i in range(4):  # пробегаемся по каждому квадрату
            x = next_figure[i][0] * cube_size + 400  # получаемся икс координату верхнего левого угла
            y = next_figure[i][1] * cube_size + 200  # получаем игрек координату верхнего левого угла
            nfigure.append(screen.create_rectangle(x, y,
                                                   x + cube_size,
                                                   y + cube_size,
                                                   fill=rgb_to_hex(
                                                       next_color)))  # отрисовывваем и закрашиваем нашу клетку
        # обновляем текст
        screen.itemconfigure(text_score, text=str(score))  # обновляем на экране количество очков
        screen.itemconfigure(text_record, text=record)  # обновляем значение рекорда

        # проигрыш
        for i in range(W):  # пробигаемся по каждой клетке
            if field[0][i]:  # если в верхней строчке есть часть фигуры
                set_record(record, score)  # записываем в файл рекорж
                field = []  # опустошаем массив сетки для логики
                for j in range(H):
                    field.append([0] * W)
                anim_count, anim_speed, anim_limit = 0, 60, 2000  # возращаем исходные значения
                score = 0  # обнуляем счетчик очков
                break  # перестаем пробигаться
        move_on_x_coord, rotate = 0, False  # возращаем исходные значения
        tk.update_idletasks()  # обновляем экран
        tk.update()  # обновляем экран
        for el in fig: game_screen.delete(el)  # опустошаем массив отрисовки нашей фигуры
        for el in nfigure: screen.delete(el)  # опустошаем массив отрисовки следующей фигуры
    sleep(0.005)  # делаем задержку на 0.005 секунды

tk.destroy()  # закрываем программу
