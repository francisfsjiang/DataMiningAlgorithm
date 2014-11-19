# encoding: utf-8
import pickle
from math import sqrt


def calc_dist(a: list, b: list):
    # print(a,b)
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i]) ** 2
    return sqrt(sum)


def cal_dist_sum(kernel_pos, x):
    result = 0
    for j in range(len(x)):
        min_k, min_dist = 0, 0xFFFFFFFF
        for k in range(len(kernel_pos)):
            dist = calc_dist(x[j], kernel_pos[k])
            if dist < min_dist:
                min_k, min_dist = k, dist
        result += min_dist
    return result


def map_split(s):
    return list(s.split())


def cal_flag(kernel_pos, x):
    result = []
    for j in range(len(x)):
        min_k, min_dist = 0, 0xFFFFFFFF
        for k in range(len(kernel_pos)):
            dist = calc_dist(x[j], kernel_pos[k])
            if dist < min_dist:
                min_k, min_dist = k, dist
        result.append(min_k)
    return result


if __name__ == '__main__':
    origin_file = open('iris.txt', mode='r')
    origin_data = list(map(map_split, origin_file.readlines()))
    x = []
    y = []
    for i in origin_data:
        x.append(list(map(float, i[0:4])))
        y.append(i[4:5])

    file = open('record-97.49269085653448.dump', mode='rb')
    dist, kernel_pos = pickle.load(file)
    print(dist)
    print(kernel_pos)

    flag = cal_flag(kernel_pos, x)
    print(flag)
    counter = {}
    for i in flag:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1
    print(counter)