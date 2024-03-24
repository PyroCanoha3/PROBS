from tkinter import *
from math import *
import random
import matplotlib.pyplot as plt
import time

t_start = time.perf_counter()
k_px = 4  # коэффициент подобия мм -> пиксель
diam_cam = 200 * k_px  # 200 мм
height_cam = 200 * k_px  # 200 мм
fig, ax = plt.subplots()
ax.minorticks_on()
ax.grid(which='major', color='k', linewidth=2)
ax.grid(which='minor', color='k', linestyle=':')


def fp_length(average_length):  # вычисление длины свободного пробега исходя из ФР
    rng = random.uniform(0, 1)
    length = -average_length * log(rng, e)
    return length


def area(x, y, from_x, to_x):
    s = 0
    for i in range(len(x)):
        if from_x <= x[i - 1] <= to_x:
            s = s + y[i]
    s = s / k_max
    return s


# ------------------------------- исходные данные -------------------------------
k_max = 200  # количество частиц
n_int = 250  # количество интервалов
scattering = 1  # 1 - включить рассеяние; 0 - нет рассеяния
wall_on = 0  # В режиме - только рисование => 1 - включает стенки, 0 - выключает стенки
average_lambda = 200  # ПАРАМЕТР ДЛЯ ИЗМЕНЕНИЯ РАЗБРОСА ЧАСТИЦ
z_collector = 230 * k_px  # положение коллектора
diametr_tube = 14  # в мм
x_wall_left = diam_cam / 2 - diametr_tube / 2 * k_px
x_wall_right = diam_cam / 2 + diametr_tube / 2 * k_px  # положение стенок
target_left = x_wall_left  # координаты колектора
target_right = x_wall_right
apertura = (diametr_tube - 8) * k_px  # abs(x_wall_right-x_wall_left) #- 10*k_px
# тип решаемой задачи 0 - только рисование распространия, 1 - ток с трубой и свободно, 2 - расчет распределения тока по секциям
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
    # print(degrees(temp))
    return 0  # temp


class particle_class:
    x0 = diam_cam / 2 - apertura / 2
    x1 = diam_cam / 2
    y0 = 0
    y1 = 0
    alfa = 0


particle = particle_class()
sect_current = 0  # суммарный ток на трубу
array_sect_current = [0] * 10  # ток по секциям


# расчет тока на секцию или трубку
def count_sect_current():
    global sect_current
    global array_sect_current
    h_sect = 19 * k_px
    y_1sect = 30 * k_px  # еще используется в ф-ии draw_sections()
    gap = 1 * k_px
    for i in range(10):
        y0_sect = y_1sect + i * h_sect + i * gap
        y1_sect = y_1sect + (i + 1) * h_sect + i * gap
        if particle.x1 - particle.x0 == 0:
            particle.x0 = particle.x0 - 1
        temp1 = (particle.y1 - particle.y0) / (particle.x1 - particle.x0) * (x_wall_left - particle.x0) + particle.y0
        temp2 = (particle.y1 - particle.y0) / (particle.x1 - particle.x0) * (x_wall_right - particle.x0) + particle.y0
        # st = str(round(particle.x0))+"-"+str(round(particle.y0))+"-"+str(round(particle.x1))+"-"+str(round(particle.y1))+"-"+str(round(x_wall_left))
        st = str(round(temp1)) + " - " + str(round(y1_sect)) + " - " + str(round(temp2))
        # if ((temp1 >= y0_sect and temp1 <= y1_sect) or (temp2 >= y0_sect and temp2 <= y1_sect)) and ((x_wall_left < particle.x0 and particle.x1 <= x_wall_left) or (x_wall_right > particle.x0 and particle.x1 >= x_wall_right)):
        if ((temp1 >= y0_sect and temp1 <= y1_sect) and (
                x_wall_left < particle.x0 and particle.x1 <= x_wall_left)) or (
                (temp2 >= y0_sect and temp2 <= y1_sect) and (
                x_wall_right > particle.x0 and particle.x1 >= x_wall_right)):
            sect_current = sect_current + 1
            array_sect_current[i] = array_sect_current[i] + 1
            # canvas.create_text(particle.x1, particle.y1, text=sect_current, justify=CENTER, font="Verdana 12")
            break


target_current = 0


# ------------------------  расчет тока на мишень  ------------------------
def count_target_current():
    global target_current
    if particle.y1 - particle.y0 == 0:
        particle.y0 = particle.y0 - 1
    temp1 = (particle.x1 - particle.x0) / (particle.y1 - particle.y0) * (z_collector - particle.y0) + particle.x0
    if (target_left <= temp1 <= target_right) and (particle.y0 < z_collector < particle.y1):
        target_current = target_current + 1
        print(f"Ток на мишени: {target_current}")


def count_target_current_new():
    global target_current
    if particle.y1 - particle.y0 == 0:
        particle.y0 = particle.y0 - 1
    temp1 = (particle.x1 - particle.x0) / (particle.y1 - particle.y0) * (z_collector - particle.y0) + particle.x0
    if (target_left <= temp1 <= target_right) and (particle.y0 < z_collector < particle.y1):
        target_current = target_current + 1
        print(f"Ток на мишени: {target_current}")


# Другой код здесь...

# Вызываем функцию count_target_current()
count_target_current()

# Вызываем функцию count_target_current_new()
count_target_current_new()


# -----------------------------  END  ----------------------------------
def dist(wall, lamda, x_plane):
    global target_current
    global sect_current
    sect_current = 0
    target_current = 0
    m = 0
    k = 1
    while k <= k_max:
        particle.x0 = diam_cam / 2 - random.uniform(-apertura / 2, apertura / 2)  # Исправлено
        particle.x1 = diam_cam / 2
        particle.y0 = 10 * k_px + 0 * random.uniform(-lamda, 0)  # Исправлено
        particle.y1 = 0
        particle.alfa = focusing(z_collector, -apertura / 2 + (k // (k_max / n_int)) * apertura / n_int)
        i = 1
        while i < 200:
            if scattering == 1:
                gamma = random.uniform(0, 1)  # Исправлено
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
            # если стенки присутствуют, то проверь - пересекает ли частица её границы. Если пересекает, то переходи к расчету следующей - без отрисовки
            if wall == 1:
                if particle.x1 <= x_wall_left or particle.x1 >= x_wall_right:
                    count_sect_current()
                    break
            if illustration == 1:
                if i % 2 == 0:
                    canvas.create_line(particle.x0, particle.y0, particle.x1, particle.y1, fill="Blue")
                else:
                    canvas.create_line(particle.x0, particle.y0, particle.x1, particle.y1, fill="Crimson")  # Crimson
            count_target_current()
            particle.x0 = particle.x1
            particle.y0 = particle.y1
            # x_plane = 270
            if particle.x1 < 0 or particle.x1 > diam_cam or particle.y1 > height_cam:
                break
            if particle.y1 >= x_plane:
                d = 0
                while d < N:
                    if particle.x1 >= (0 + d * dx) and particle.x1 <= (0 + (d + 1) * dx):
                        gr_x[d] = gr_x[d] + 1
                        m = m + 1
                    d = d + 1
                break
            i = i + 1
        k = k + 1
    # noinspection PyTypeChecker
    d = [0] * N


N = diam_cam
dx = (diam_cam - 0) / N
gr_x = [0] * N
temp_cur = 0


# ------------------------  Режим номер 1  ------------------------
def current_free_and_tube():  # Расчет тока на мишень при наличии ограничивающей трубки и в её отсутствии
    global illustration
    n_del = 9  # формально количество давлений для которых измеряем отношение токов
    relation = [0] * n_del
    x = [0] * n_del
    temp_lambda = 0

    # f - давление в Па
    for f in range(n_del):
        temp_lambda = 133 * 0.358 / (2 + f)
        dist(1, round(temp_lambda * k_px), z_collector)
        # noinspection PyTypeChecker
        x[f] = 133 * 0.358 / temp_lambda
        temp_cur = target_current  # через трубку
        illustration = 0
        dist(0, round(temp_lambda * k_px), z_collector)
        # noinspection PyTypeChecker
        relation[f] = temp_cur / target_current
        str_f = str(round(x[f], 3)) + " " + str(round(relation[f], 3))
        print(str_f)
        with open("data.txt", "a") as file:
            print(str_f, file=file, sep="\n")
        print("ток с трубой = " + str(temp_cur) + "  ток свободно = " + str(target_current))

    plt.plot(x, relation)
    plt.show()


# -----------------------------  END  ----------------------------------
# ------------------------  Режим номер 2  ------------------------
def longitudinal_distribution():  # распределение тока по секциям
    global array_sect_current, y
    n_sect = 10  # количество секций
    x = [0] * (n_sect + 1)  # добавляем коллектор
    n_del = 1
    for f in range(n_sect + 1):
        x[f] = f + 1
    for t in range(n_del):
        sum_cur = 0  # суммарный ток и на трубу и на мишень
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


# -----------------------------  END  -------------------------------
temp_ill = 0
if type_task > 0:
    wall_on = 1
if type_task == 0:
    if illustration != 1:
        illustration = 1
        tk = Tk()
        canvas = Canvas(tk, height=height_cam + 20 * k_px, width=diam_cam)
        canvas.pack()
    z_collector = height_cam
    dist(wall_on, average_lambda, z_collector)
elif type_task == 1:
    if illustration == 1:  # запоминаем, что иллюстрация была включена. Далее мы её отключим не надолго
        temp_ill = 1
    current_free_and_tube()
    if temp_ill == 1:  # вспоминаем, что иллюстрация была включена
        illustration = 1
elif type_task == 2:
    longitudinal_distribution()
print("")


def draw_sections():  # Рисуем секции
    h_sect = 19 * k_px
    y_1sect = 30 * k_px  # еще используется в ф-ии count_sect_current()
    gap = 1 * k_px
    if illustration == 1:
        for i in range(10):
            canvas.create_rectangle(x_wall_left, y_1sect + i * h_sect + i * gap, x_wall_left - 3,
                                    y_1sect + (i + 1) * h_sect + i * gap, outline="#000", fill="#000")
            canvas.create_rectangle(x_wall_right, y_1sect + i * h_sect + i * gap, x_wall_right + 3,
                                    y_1sect + (i + 1) * h_sect + i * gap, outline="#000", fill="#000")


draw_sections()

all_time = time.perf_counter() - t_start
print("Time elapsed: ", round(all_time))  # CPU seconds elapsed (floating point)


