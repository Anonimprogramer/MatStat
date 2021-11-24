import math
from math import erf

import numpy as np
from numpy import sqrt
import matplotlib.pyplot as plt


def Laplas_function(x):
    return erf(sqrt(2) * x / 2) / 2


def load(filename):
    univariate_sample = []
    with open(filename, "r") as file:
        for line in file:
            univariate_sample.extend(list(map(float, line.split())))
    return univariate_sample


def variation_range_of_univariate_sample(univariate_sample):
    variation_range_of_univariate_sample = univariate_sample
    variation_range_of_univariate_sample.sort()
    return variation_range_of_univariate_sample


def distribution_function_grapic(variation_range):
    unique_elements = variation_range
    unique_elements = set(unique_elements)
    current = 0
    common_count = len(variation_range)

    y = []
    x = []
    for k in unique_elements:
        x.append(k)
        x.append(k)
        y.append(current / common_count)
        current += variation_range.count(k)
        y.append(current / common_count)

    x.extend([0, 5])
    y.extend([0, 1])
    x.sort()
    y.sort()

    plt.plot(x, y, lw=1)
    plt.grid()
    ax = plt.gca()
    plt.xlim([0, 5])
    plt.ylim([0, 1.2])
    plt.show()


def hypotize_of_normal_law(variation_range):
    n = int(sqrt(len(variation_range)))
    delta = (variation_range[len(variation_range) - 1] - variation_range[0]) / n
    delta_lists = []
    exp = expectation(variation_range)
    dis = dispersion(variation_range)
    avg = sqrt(dis)
    another = []

    print("Таблица значений для проверки гипотезы о нормальном законе с помощью критерия χ 2 .")
    print("----------------------------------------------------------------------------------")
    print("|  j  |  Aj  |  Bj  |  F0(Aj)  |  F0(Bj)  |    pj     |   pj*  |  (pj*-pj)^2/2pj")
    print("----------------------------------------------------------------------------------")

    sum = 0
    sum1 = 0
    interval_teoretic_propabilities = []
    for i in range(1, 11):
        delta_lists.append([])
        for value in variation_range:
            if delta * (i - 1) + variation_range[0] <= value <= delta * i + variation_range[0]:
                delta_lists[i - 1].append(value)
        if i != 1 and i != 10:
            interval_teoretic_propabilities.append(
                Laplas_function((delta * i - exp+variation_range[0]) / avg) - Laplas_function((delta * (i - 1) - exp+variation_range[0]) / avg))
            print(i, " | ", round(delta * (i - 1) + variation_range[0], 3), " | ",
                  round(delta * i + variation_range[0], 3), " | ",
                  round(Laplas_function((delta * (i - 1) - exp+variation_range[0]) / avg), 3), " | ",
                  round(Laplas_function((delta * i - exp+variation_range[0]) / avg), 3), " | ",
                  round(Laplas_function((delta * i - exp+variation_range[0]) / avg) - Laplas_function((delta * (i - 1) - exp+variation_range[0]) / avg), 3),
                  " | ", round(len(delta_lists[i - 1]) / n / n, 3)," | ",round(pow((len(delta_lists[i-1]) / n / n - interval_teoretic_propabilities[i-1]), 2) /
                       interval_teoretic_propabilities[i-1]/2,3))
        elif i == 1:
            interval_teoretic_propabilities.append(Laplas_function((delta * i - exp+variation_range[0]) / avg) + 0.5)
            print(i, " | ", "-∞   ", " | ",
                  round(delta * i + variation_range[0], 3), " | ",
                  -0.5, " | ",
                  round(Laplas_function((delta * i - exp+variation_range[0]) / avg), 3), " | ",
                  round(Laplas_function((delta * i - exp+variation_range[0]) / avg) + 0.5, 3), " | ",
                  round(len(delta_lists[i - 1]) / n / n, 3)," | ",round(pow((len(delta_lists[i-1]) / n / n - interval_teoretic_propabilities[i-1]), 2) /
                       interval_teoretic_propabilities[i-1]/2,3))

        elif i == 10:
            interval_teoretic_propabilities.append(0.5 - Laplas_function((delta * (i - 1) - exp+variation_range[0]) / avg))
            print(i, " | ", round(delta * (i - 1) + variation_range[0], 3), " | ",
                  "+∞   ", " | ",
                  round(Laplas_function((delta * (i-1)+variation_range[0] - exp) / avg+variation_range[0]), 3), " | ",
                  0.5, " | ",
                  round(0.5 - Laplas_function((delta * (i - 1) - exp+variation_range[0]) / avg), 3), " | ",
                  round(len(delta_lists[i - 1]) / n / n, 3)," | ",round(pow((len(delta_lists[i-1]) / n / n - interval_teoretic_propabilities[i-1]), 2) /
                       interval_teoretic_propabilities[i-1]/2,3))
    for i in range(0, 10):
        another.append(pow((len(delta_lists[i]) / n / n - interval_teoretic_propabilities[i]), 2) /
                       interval_teoretic_propabilities[i]/2)
        sum += interval_teoretic_propabilities[i]
        sum1 += another[i]
    if sum==1:
        print(sum,"- контрольная сумма выполняется")
    else:
        print(sum,"контрольная сумма не выполняется")
    print("χ 2=", sum1 * len(variation_range))
    if sum1*len(variation_range)<14.07:
        print("Отклонять гипотезу нет оснований")
    else:
        print("есть основания отклонить гипотезу")


def f_0(x, exp, dis):
    return 1-pow(math.e,-exp*x)


def distribution_function_grapic_and_other_function(variation_range):
    unique_elements = variation_range
    unique_elements = set(unique_elements)
    current = 0
    common_count = len(variation_range)

    y = []
    x = []
    for k in unique_elements:
        x.append(k)
        x.append(k)
        y.append(current / common_count)
        current += variation_range.count(k)
        y.append(current / common_count)

    x.extend([0, 5])
    y.extend([0, 1])
    x.sort()
    y.sort()
    x_e = np.arange(variation_range[0], variation_range[len(variation_range) - 1], 0.01)
    y_e = []
    for z in x_e:
        y_e.append(f_0(z, expectation(variation_range), dispersion(variation_range)))

    max = -100
    x_max = [1, 2]
    y_max = [0, 0]
    for i, j in zip(x, y):
        if abs(f_0(i, expectation(variation_range), dispersion(variation_range)) - j) > max:
            max = abs(f_0(i, expectation(variation_range), dispersion(variation_range)) - j)
            x_max[0] = i
            x_max[1] = i
            y_max[0] = f_0(i, expectation(variation_range), dispersion(variation_range))
            y_max[1] = j

    print(max, "Z для Колмогорова")
    print(max * sqrt(len(variation_range)), "лябда для Колмогорова")
    if (max* sqrt(len(variation_range)) > 1.36):
        print("Гипотезу о экпотенциальном распределении есть основания отвергать")
    else:
        print("Гипотезу о экспонтецинциальном распределении нет основания отвергать")
    plt.plot(x_e, y_e)
    plt.plot(x_max, y_max)
    plt.plot(x, y, lw=1)
    plt.grid()
    ax = plt.gca()
    plt.xlim([0, 14])
    plt.ylim([-2, 1.2])
    plt.title("Функция распределения и экпонтенциальное распределение")
    plt.show()


def distribution_function_grapic_and_even_distributin_function(variation_range):
    unique_elements = variation_range
    unique_elements = set(unique_elements)
    current = 0
    common_count = len(variation_range)

    y = []
    x = []
    for k in unique_elements:
        x.append(k)
        x.append(k)
        y.append(current / common_count)
        current += variation_range.count(k)
        y.append(current / common_count)

    x.extend([0, 5])
    y.extend([0, 1])
    x.sort()
    y.sort()

    x_e = [variation_range[0], variation_range[len(variation_range) - 1]]
    y_e = [0, 1]

    max = -100
    x_max = [1, 2]
    y_max = [0, 0]
    for i, j in zip(x, y):
        if abs(i * (variation_range[len(variation_range) - 1] / variation_range[0]) - j) > max:
            max = abs(i * (variation_range[len(variation_range) - 1] / variation_range[0]) - j)
            x_max[0] = i
            x_max[1] = i
            y_max[0] = (i - variation_range[0]) / (variation_range[len(variation_range) - 1] - variation_range[0])
            y_max[1] = j

    plt.plot(x_e, y_e)
    plt.plot(x_max, y_max)
    plt.plot(x, y, lw=1)
    plt.grid()
    ax = plt.gca()
    plt.xlim([0, 15])
    plt.ylim([-0.1, 1.2])
    plt.show()


def equiinterval_method_grapic(variation_range):
    n = int(sqrt(len(variation_range)))
    delta = (variation_range[len(variation_range) - 1] - variation_range[0]) / n
    delta_lists = []
    print("Таблица значений для равноинтервального способа")
    print("----------------------------------------------------")
    print("|  j  |  Aj  |  Bj  |  hj  |  vj  |  pj*  |   fj*  |")
    print("----------------------------------------------------")

    for i in range(1, 11):
        delta_lists.append([])
        for value in variation_range:
            if delta * (i - 1) + variation_range[0] <= value <= delta * i + variation_range[0]:
                delta_lists[i - 1].append(value)
        print(i, "|", round(delta * (i - 1) + variation_range[0], 5), "|", round(delta * i + variation_range[0], 5),
              "|", round(delta, 4), "|",
              len(delta_lists[i - 1]), "|", len(delta_lists[i - 1]) / len(variation_range), "|",
              round(len(delta_lists[i - 1]) / len(variation_range) / delta, 4), "|")
    x = [variation_range[0]]
    y = [0]
    i = 0
    for list in delta_lists:
        x.append(delta * i + variation_range[0])
        x.append(delta * (i + 1) + variation_range[0])
        y.append(len(list) / n / n / delta)
        y.append(len(list) / n / n / delta)
        i += 1
    y.append(0)
    x.append(delta * n + variation_range[0])

    plt.plot(x, y)
    plt.title("Гистограмма равноинтервального способа")
    plt.show()


def equipropable_method_grapic(variation_range):
    n = int(sqrt(len(variation_range)))
    list_a = [variation_range[0]]
    list_b = []
    list_v = []
    for i in range(1, 10):
        list_a.append((variation_range[i * n] + variation_range[i * n - 1]) / 2)
        list_b.append((variation_range[i * n] + variation_range[i * n - 1]) / 2)
    list_b.append(variation_range[len(variation_range) - 1])

    x = [variation_range[0]]
    y = [0]

    for i in range(n):
        x.append(list_a[i])
        x.append((list_b[i]))
        z = 10
        k = 1
        l = 1
        if (i < 9):
            while variation_range[i * 10 + 9 + k] == variation_range[i * 10 + 9]:
                k += 1
        if (i > 0):
            while variation_range[i * 10 - l] == variation_range[i * 10]:
                l += 1
        list_v.append(z + k - 2 + l)
        y.append((z + k - 2 + l) / (n * n * (list_b[i] - list_a[i])))
        y.append((z + k - 2 + l) / (n * n * (list_b[i] - list_a[i])))

    x.append(variation_range[len(variation_range) - 1])
    y.append(0)

    print("Таблица значений для равновероятностного способа")
    print("----------------------------------------------------")
    print("|  j  |  Aj  |  Bj  |    hj    |  vj  |  pj*  |   fj*  |")
    print("----------------------------------------------------")
    for i in range(1, 11):
        print(i, " | ", round(list_a[i - 1], 4), " | ", round(list_b[i - 1], 4), " | ",
              round(list_b[i - 1] - list_a[i - 1], 4), " | ", list_v[i - 1], " | ",
              list_v[i - 1] / len(variation_range), " | ",
              round(list_v[i - 1] / (list_b[i - 1] - list_a[i - 1]) / len(variation_range), 4))

    plt.plot(x, y)
    plt.title("Гистограмма равновероятностного способа")
    plt.show()


def expectation(variation_range):
    sum = 0
    for i in variation_range:
        sum += i
    return sum / len(variation_range)


def dispersion(variation_range):
    n = len(variation_range)
    exp = expectation(variation_range)
    cum = 0
    for i in variation_range:
        cum += i * i
    return cum / (n - 1) - n / (n - 1) * pow(exp, 2)


def confidence_interval_MAT(variation_range):
    laplas = 1.96
    exp = expectation(variation_range)
    interval = sqrt(dispersion(variation_range)) * laplas / sqrt(len(variation_range))
    print(exp - interval, "<=", exp, "<=", exp + interval,
          "доверительный интервал для матожидания с надежностью γ = 0,95")


def confidence_interval_DIS(variation_range):
    laplas = 1.96
    dis = dispersion(variation_range)
    interval = laplas * sqrt(2 / (len(variation_range) - 1)) * dis
    print(dis - interval, "<=", dis, "<=", dis + interval,
          "доверительный интервал для дисперсии с надежностью γ = 0,95")
