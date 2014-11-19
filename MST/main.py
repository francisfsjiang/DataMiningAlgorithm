# encoding: utf-8
import csv
import math
from copy import deepcopy
import pickle
from array import array


def cal_sigal_dist(a: tuple, b: tuple):
    result = 0
    for i in range(len(a)-1):
        result += (a[i] - b[i]) ** 2
    return math.sqrt(result)


def cal_dist_from_mat(mat: list, a: tuple, b: tuple):
    return mat[
        a[-1]
    ][
        b[-1]
    ]


def MST(x, mat):
    in_set = {x[0]}
    out_set = set(x[1:len(x)])
    print(len(in_set))
    print(len(out_set))

    edge = []

    for t in range(len(x)-1):
        min_dist = 0xFFFFFFF
        for i in in_set:
            for j in out_set:
                dist = cal_dist_from_mat(mat, i, j)
                if dist < min_dist:
                    min_from = i
                    min_to = j
                    min_dist = dist
        in_set.add(min_to)
        out_set.remove(min_to)
        edge.append((min_from[-1], min_to[-1], min_dist))
        print(len(in_set))
        print(len(out_set))

    return edge


def init():
    file = open('iris.txt', mode='r')
    data = csv.reader(file)
    x = []
    y = []
    num = 0
    for i in data:
        tmp = list(map(float, i[0:4]))
        tmp.append(num)
        x.append(
            tuple(
                tmp
            )
        )
        y.append(i[4])
        num += 1
    return x, y


def cal_dist_matrix(x):
    mat = [[0 for i in range(len(x))] for j in range(len(x))]

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i == j:
                mat[i][j] = 0
            else:
                mat[i][j] = cal_sigal_dist(x[i], x[j])

    return mat


def cmp_fun(a):
    return a[-1]


if __name__ == '__main__':
    x, y = init()
    print(x)
    print(y)

    mat = cal_dist_matrix(x)
    for i in mat:
        print(i)

    dist = cal_dist_from_mat(mat, x[1], x[0])
    print(dist)
    edge = MST(x, mat)
    print(edge)

    edge.sort(key=cmp_fun, reverse=True)
    print(edge)
    edge.remove(edge[0])
    edge.remove(edge[0])
    print(edge)
    #
    # record_file = open('record.dump', 'wb')
    # pk = pickle.Pickler(record_file).dump(new_x)
    # record_file.close()
    #
    # for i in new_x:
    #     print(i)
