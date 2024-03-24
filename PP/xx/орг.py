from tkinter import *
from math import *
import random
import matplotlib.pyplot as plt
import time

t_start = time.perf_counter()
k_px = 4  # коэффициент подобия мм -> пиксель
diam_cam = 200 * k_px  # 200 мм
height_cam = 250 * k_px  # 250 мм

fig, ax = plt.subplots()
ax.minorticks_on()
ax.grid(which='major', color='k', linewidth=2)
ax.grid(which='minor', color='k', linestyle=':')

def fp_length(average_length):  # вычисление длины свободного пробега исходя из ФР
    rng = random.uniform(0, 1)
    length = -average_length * log(rng)
    return length

def draw_target(x_left, x_right, y, width):
    canvas.create_rectangle(x_left, y, x_right, y + width, fill="black")

def area(x, y, from_x, to_x):
    i = 2
    s = 0
    for i in range(1, len(x)):
        if x[i - 1] >= from_x and x[i - 1] <= to_x:
            s = s + y[i]
    s = s / k_max
    return s

# ------------------------------- исходные данные -------------------------------
k_max = 500  # количество частиц
n_int = 500  # количество интервалов
scattering = 1  # 1 - включить рассеяние; 0 - нет рассеяния
wall_on = 0  # В режиме - только рисование => 1 - включает стенки, 0 - выключает стенки
average_lambda = 5 * k_px
z_collector = 230 * k_px  # положение коллектора
diametr_tube = 15  # в мм
x_wall_left = diam_cam / 2 - diametr_tube / 2 * k_px
x_wall_right = diam_cam / 2 + diametr_tube / 2 * k_px  # положение стенок
target_left = x_wall_left  # координаты коллектора
target_right = x_wall_right
apertura = (diametr_tube - 8) * k_px  # abs(x_wall_right-x_wall_left) #- 10*k_px
# тип решаемой задачи 0 - только рисование распространения, 1 - ток с трубой и свободно, 2 - расчет распределения тока по секциям
type_task = 0
illustration = 1  # 1 - рисование распространения
# ------------------------------- END -------------------------------

if illustration == 1:
    tk = Tk()
    canvas = Canvas(tk, height=height_cam + 20 * k_px, width=diam_cam)
    canvas.pack()

def focusing(z_cross, dist_from_axis):
    temp = 0
    if dist_from_axis != (diam_cam / 2 - apertura / 2):
        temp = -atan(dist_from_axis / z_cross)
    else:
        temp = 0
    return temp

class particle_class:
    x0 = diam_cam / 2 - apertura / 2
    x1 = diam_cam / 2
    y0 = 0
    y1 = 0
    alfa = 0

particle = particle_class()
sect_current = 0  # суммарный ток на трубу
array_sect_current = [0] * 10  # ток по секциям
lines_drawn = 0  # счетчик нарисованных линий

# расчет тока на секцию или трубку
def count_sect_current():
    global sect_current
    global array_sect_current
    global lines_drawn
    sect_current += 1
    lines_drawn += 1

# ------------------------  расчет тока на мишень  ------------------------
def count_target_current():
    global target_current
    global lines_drawn
    target_current += 1
    lines_drawn += 1

# -----------------------------  END  ----------------------------------

def dist(wall, lamda, x_plane):
    global target_current
    global sect_current
    global lines_drawn
    lines_drawn = 0
    m = 0
    k = 1
    while k <= k_max:
        particle.x0 = diam_cam / 2 - round(random.uniform(-apertura / 2, apertura / 2))
        particle.x1 = diam_cam / 2
        particle.y0 = 10 * k_px + 0 * round(random.uniform(-lamda, 0))
        particle.y1 = 0
        particle.alfa = focusing(z_collector, -apertura / 2 + (k // (k_max / n_int)) * apertura / n_int)
        i = 1
        while i < 200:
            if scattering == 1:
                gamma = random.uniform(0, 1)
                if gamma <= 1.99:
                    if random.randint(0, 1) == 1:
                        random_alfa = 2 * asin(
                            sqrt(pow(sin(0.017 / 2), 2) / (1 - gamma + 1 * gamma * pow(sin(0.017 / 2), 2))))
                    else:
                        random_alfa = -2 * asin(
                            sqrt(pow(sin(0.017 / 2), 2) / (1 - gamma + 1 * gamma * pow(sin(0.017 / 2), 2))))
                else:
                    random_alfa = 0
            else:
                random_alfa = 0
            particle.alfa = particle.alfa + random_alfa
            if scattering == 1:
                particle.x1 = particle.x0 + sin(particle.alfa) * fp_length(lamda)
                particle.y1 = particle.y0 + cos(particle.alfa) * fp_length(lamda)
            else:
                particle.x1 = particle.x0 + sin(particle.alfa) * lamda
                particle.y1 = particle.y0 + cos(particle.alfa) * lamda
            if wall == 1:
                if particle.x1 <= x_wall_left or particle.x1 >= x_wall_right:
                    count_sect_current()
                    break
            if illustration == 1:
                if i % 2 == 0:
                    canvas.create_line(particle.x0, particle.y0, particle.x1, particle.y1, fill="Blue")
                else:
                    canvas.create_line(particle.x0, particle.y0, particle.x1, particle.y1, fill="Crimson")
                lines_drawn += 1
            count_target_current()
            particle.x0 = particle.x1
            particle.y0 = particle.y1
            if particle.x1 < 0 or particle.x1 > diam_cam or particle.y1 > height_cam:
                break
            if particle.y1 >= x_plane:
                d = 0
                N = diam_cam
                dx = (diam_cam - 0) / N
                gr_x = [0] * N
                while d < N:
                    if particle.x1 >= (0 + d * dx) and particle.x1 <= (0 + (d + 1) * dx):
                        gr_x[d] = gr_x[d] + 1
                        m = m + 1
                    d = d + 1
                draw_target(target_left, target_right, target_y, 5)  # Изменяйте ширину палки здесь
                lines_drawn += 1
                break
            i = i + 1
        k = k + 1

    N = diam_cam
    dx = (diam_cam - 0) / N
    gr_x = [0] * N
    temp_cur = 0

    return lines_drawn

# ------------------------  Режим номер 1  ------------------------
def current_free_and_tube():
    global illustration
    global lines_drawn
    n_del = 9
    relation = [0] * n_del
    x = [0] * n_del
    temp_lambda = 0

    for f in range(n_del):
        temp_lambda = 133 * 0.358 / (2 + f)
        dist(1, round(temp_lambda * k_px), z_collector)
        x[f] = 133 * 0.358 / temp_lambda
        temp_cur = target_current
        illustration = 0
        dist(0, round(temp_lambda * k_px), z_collector)
        relation[f] = temp_cur / target_current
        str_f = str(round(x[f], 3)) + " " + str(round(relation[f], 3))
        print(str_f)
        with open("data.txt", "a") as file:
            print(str_f, file=file, sep="\n")
        print("ток с трубой = " + str(temp_cur) + "  ток свободно = " + str(target_current))
    plt.plot(x, relation)
    plt.show()
    print("Ток на мишени = " + str(target_current))
    print("Общее количество нарисованных линий: ", lines_drawn)

# -----------------------------  END  ----------------------------------

# ------------------------  Режим номер 2  ------------------------
def longitudinal_distribution():
    global array_sect_current
    global lines_drawn
    n_sect = 10
    x = [0] * (n_sect + 1)
    n_del = 1
    for f in range(n_sect + 1):
        x[f] = f + 1
    for t in range(n_del):
        sum_cur = 0
        array_sect_current = [0] * n_sect
        dist(1, average_lambda, z_collector)
        for f in range(n_sect):
            sum_cur = sum_cur + array_sect_current[f]
        sum_cur = sum_cur + target_current
        y = [0] * (n_sect + 1)
        for f in range(n_sect + 1):
            if f != n_sect:
                y[f] = array_sect_current[f] / sum_cur
            else:
                y[f] = target_current / sum_cur
            str_f = str(round(y[f], 3))
            print(str_f)
        with open("data.txt", "a") as file:
            print("-----" + str((average_lambda + t * t * average_lambda) / k_px), file=file, sep="\n")
    print("ток на трубу = " + str(sect_current) + "  на мишень = " + str(target_current))
    plt.plot(x, y)
    plt.show()
    print("Ток на мишени = " + str(target_current))
    print("Общее количество нарисованных линий: ", lines_drawn)

# -----------------------------  END  ----------------------------------

temp_ill = 0
target_current = 0
target_y = 50  # Пример положения мишени по оси Y

if type_task > 0:
    wall_on = 1

if type_task == 0:
    if illustration != 1:
        illustration = 1
        tk = Tk()
        canvas = Canvas(tk, height=height_cam + 20 * k_px, width=diam_cam)
        canvas.pack()
    z_collector = height_cam
    lines_drawn = dist(wall_on, average_lambda, z_collector)

elif type_task == 1:
    if illustration == 1:
        temp_ill = 1
    current_free_and_tube()
    if temp_ill == 1:
        illustration = 1

elif type_task == 2:
    longitudinal_distribution()

print("Ток на мишени = " + str(target_current))
print("Общее количество нарисованных линий: ", lines_drawn)

with open("output.txt", "w") as file:
    print("Ток на мишени = " + str(target_current), file=file)
    print("Общее количество нарисованных линий: ", lines_drawn, file=file)

all_time = time.perf_counter() - t_start

with open("output.txt", "w") as file:
    print("Время выполнения: ", round(all_time), file=file)
    print("Ток на мишени = " + str(target_current), file=file)
    print("Общее количество нарисованных линий: ", lines_drawn, file=file)

tk.mainloop()  # Добавляем эту строку для отображения окна Tkinter и его содержимого