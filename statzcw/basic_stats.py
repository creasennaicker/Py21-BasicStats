import math
import pandas as pd
import csv
from typing import List

db_zero = pd.read_csv('/Users/naickercreason/dev/Py21-BasicStats/dataZero.csv')
#print(db_zero)

column_x = db_zero['x']
column_y = db_zero['y']




def zcount(list: List[float]) -> float:
    count = len(list)
    return count

# print(zcount(column_x))
# print(zcount(column_y))


def zmean(list: List[float]) -> float:
    mean = sum(list) / zcount(list)
    return mean

# print(zmean(column_x))
# print(zmean(column_y))



def zmode(list: List[float]) -> float:
    mode = max(set(list), key=list.count)
    return mode

# print(zmode(column_x))
# print(zmode(column_y))


def zmedian(list: List[float]) -> float:
    num_sort = sorted(list)
    list_len = len(list)
    index = (list_len - 1) // 2

    if (list_len % 2):
        return num_sort[index]
    else:
        return (num_sort[index] + num_sort[index + 1] / 2.0)

# print(zmedian(column_x))
# print(zmedian(column_y))


def zvariance(list: List[float]) -> float:
    n = len(list)
    mean = sum(list) / n
    deviations = [(x - mean) ** 2 for x in list]
    variance = sum(deviations) / n
    return variance

# print(zvariance(column_x))
# print(zvariance(column_y))


def zstddev(list: List[float]) -> float:
    var = zvariance(list)
    std_dev = math.sqrt(var)
    return std_dev

# print(zstddev(column_x))
# print(zstddev(column_y))


def zstderr(list: List[float]) -> float:
    se = zstddev(list)
    n = zcount(list)
    return se / math.sqrt(n)

# print(zstddev(column_x))
# print(zstderr(column_y))



def zcorr(listx, listy) -> float:
    n = len(listx)
    sum_x = float(sum(listx))
    sum_y = float(sum(listy))
    sum_x_sq = sum(xi * xi for xi in listx)
    sum_y_sq = sum(xi * xi for xi in listy)
    psum = sum(xi * yi for xi, yi, in zip(listx, listy))
    num = psum - ((sum_x * sum_y) / n)
    den = pow((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y, 2) / n), 0.5)
    if den == 0:
        return 0
    else:
        return round((num / den), 3)


print(zcorr(column_x, column_y))
