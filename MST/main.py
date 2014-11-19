# encoding: utf-8
import csv
import math
from copy import deepcopy
import pickle


def cal_sigal_dist(a: tuple, b: tuple):
    result = 0
    for i in range(len(a)-1):
        result += (a[i] - b[i]) ** 2
    return math.sqrt(result)


def cal_set_dist(a: set, b: set):
    num = len(a) * len(b)
    result = 0
    for i in a:
        for j in b:
            result += cal_sigal_dist(i, j)
    return result/num


def MST(x):
    new_x = deepcopy(x)
    for t in range(0, len(new_x)-3):
        min_dist = 0xFFFFFFFF
        min_set_a_num = -1
        min_set_b_num = -1
        for i in range(len(new_x)):
            for j in range(len(new_x)):
                if i == j:
                    continue
                dist = cal_set_dist(new_x[i], new_x[j])
                if dist < min_dist:
                    min_dist = dist
                    min_set_a_num = i
                    min_set_b_num = j
        print('--------------')
        print(min_dist)
        # new_set = [i for i in new_x[min_set_a_num]] + [j for j in new_x[min_set_b_num]]
        new_set = set.union(
            deepcopy(new_x[min_set_a_num]),
            deepcopy(new_x[min_set_b_num])
        )
        print(new_x[min_set_a_num])
        print(new_x[min_set_b_num])
        print(new_set)
        if min_set_a_num < min_set_b_num:
            new_x.remove(new_x[min_set_b_num])
            new_x.remove(new_x[min_set_a_num])
        else:
            new_x.remove(new_x[min_set_a_num])
            new_x.remove(new_x[min_set_b_num])
        new_x.append(new_set)

        print('x len ', len(new_x))
        print(new_x)
    return new_x


def init():
    file = open('iris.txt', mode='r')
    data = csv.reader(file)
    x = []
    y = []
    num = 0
    for i in data:
        tmp = list(map(float, i[0:4]))
        tmp.append(num)
        x.append({
            tuple(
                tmp
            )
        })
        y.append(i[4])
        num += 1
    return x, y


if __name__ == '__main__':
    x, y = init()
    print(x)
    print(y)

    new_x = MST(x)

    record_file = open('record.dump', 'wb')
    pk = pickle.Pickler(record_file).dump(new_x)
    record_file.close()

    for i in new_x:
        print(i)
