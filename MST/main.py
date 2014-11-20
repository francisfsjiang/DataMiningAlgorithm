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


def MST(origin_edge, node_num):
    in_set = {0}
    out_set = set(range(1, node_num))
    print(in_set)
    print(out_set)
    print(len(in_set))
    print(len(out_set))

    for t in range(node_num):
        min_dist = 0xFFFFFFF
        for i in in_set:
            for j in out_set:

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
    file = open('football1.txt', mode='r')
    data = list(file.readlines())
    print(data)
    node_num = int(data[0])
    edge_num = int(data[1])
    edge_name = {}
    for i in range(2, node_num+2):
        num, name = data[i].split()
        num = int(num)
        edge_name[num] = name

    origin_edge = {}
    for i in range(node_num+2, node_num+2+edge_num):
        tmp = list(map(int, data[i].split()))
        tmp[2] = 0
        origin_edge[tuple(tmp[0:2])] = 0
    return edge_name, origin_edge, node_num


def cal_dist_matrix(origin_edge, node_num):
    mat = [[0 for i in range(node_num+1)] for j in range(node_num+1)]

    for i, j in origin_edge.items():
        print(i)
        mat[i[0]][i[1]] = 1

    return mat


def cmp_fun(a):
    return a[-1]


if __name__ == '__main__':
    node_name, origin_edge, node_num = init()
    print(origin_edge)
    print(node_name)


    mat = cal_dist_matrix(origin_edge, node_num)



    edge = MST(origin_edge, node_num)
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

    #init color
    color = {}
    for i in range(len(origin_edge)):
        color[i] = i

    for i in edge:
        a = i[0]
        b = i[1]
        print(a, b)
        b_color = color[b]
        for j in color.keys():
            if color[j] == b_color:
                color[j] = color[a]
    print(list(color.items()))

    counter = {}
    for i, j in color.items():
        if not j in counter:
            counter[j] = 1
        else:
            counter[j] += 1
    print(counter)