import math
import numpy as np
from math import sqrt, log1p

from matplotlib import pyplot as plt

import univariate_sample as us


def load(x, y, filename):
    with open(filename, "r") as file:
        for line in file:
            a, b = map(float, line.split())
            x.append(a)
            y.append(b)


def correlation_moment(x, y):
    n = len(x) - 1
    exp_x = us.expectation(x)
    exp_y = us.expectation(y)
    sum = 0
    for i in range(n + 1):
        sum += (x[i] - exp_x) * (y[i] - exp_y)
    correlation_moment_mark = sum / n
    # Кто нашёл Марка?
    return correlation_moment_mark


def correlation_coefficent(x, y):
    correlation_moment_mark = correlation_moment(x, y)
    dis_x = us.dispersion(x)
    dis_y = us.dispersion(y)
    return correlation_moment_mark / sqrt((dis_y * dis_x))


def interval_correlation_mark(x, y):
    Y = 0.95
    R = correlation_coefficent(x, y)
    z = 1.96
    # я найду как находить аргументы Лапласа чесна-чесна
    n = len(x)
    a = 0.5 * math.log((1 + R) / (1 - R)) - z / (sqrt(n - 3))
    b = 0.5 * math.log((1 + R) / (1 - R)) + z / (sqrt(n - 3))
    return a, b

def hypotize_of_lack_correlation(x,y):
    z=1.96
    n=len(x)
    R=correlation_coefficent(x,y)
    Z=(abs(R)*sqrt(n))/(1-pow(R,2))
    print(Z)
    if(Z>z):
        print("Корреляция есть")
    else:
        print("Величины некореллированны")

def dispersion_diargram_and_regression_line(x,y):
    X=np.arange(min(x)-1,max(x)+1,0.1)
    a=correlation_moment(x,y)/us.dispersion(x)
    b=us.expectation(y)-a*us.expectation(x)
    Y=X*a+b
    print(a,"-a1*")
    print(b,"-a0*")
    plt.plot(x, y,'ro')
    plt.plot(X,Y)
    plt.show()
