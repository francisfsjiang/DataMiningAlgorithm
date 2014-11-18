# encoding: utf-8
import csv
from random import randint
from math import sqrt
import multiprocessing as mp
from multiprocessing import queues, pool
from multiprocessing.queues import Empty
import pickle
import copy


def map_split(s):
    return list(s.split())


def calc_dist(a: list, b: list):
    # print(a,b)
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i]) ** 2
    return sqrt(sum)


def kmeans(x):
    kernel_pos = [copy.deepcopy(x[randint(0, 149)]) for i in range(3)]

    for i in range(100):
        last_kernel_pos = [[j for j in i] for i in kernel_pos]
        kernel_sum = [[0 for i in range(4)] for i in range(3)]
        kernel_num = [0 for i in range(3)]

        for j in range(len(x)):
            min_k, min_dist = 0, 0xFFFFFFFF
            for k in range(len(kernel_pos)):
                dist = calc_dist(x[j], kernel_pos[k])
                if dist < min_dist:
                    min_k, min_dist = k, dist
            # x[j][4] = min_k

            for t in range(4):
                kernel_sum[min_k][t] += x[j][t]
            kernel_num[min_k] += 1

        for k in range(len(kernel_pos)):
            for t in range(4):
                if kernel_num[k] != 0:
                    kernel_pos[k][t] = kernel_sum[k][t]/kernel_num[k]
            break

        if kernel_pos == last_kernel_pos:
            return kernel_pos


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


def cal_kmeans_loop(x, times, process_queue):
    min_dist = 0xFFFFFFFF
    best_kernel_pos = []
    for i in range(times):
        kernel_pos = kmeans(x)
        dist = cal_dist_sum(kernel_pos, x)
        if dist < min_dist:
            min_dist = dist
            best_kernel_pos = [[j for j in i] for i in kernel_pos]

        if i % 1000 == 0:
            # print(min_dist)
            process_queue.put((min_dist, [[j for j in i] for i in best_kernel_pos]))


if __name__ == '__main__':
    origin_file = open('iris.txt', mode='r')
    origin_data = list(map(map_split, origin_file.readlines()))
    x = []
    y = []
    for i in origin_data:
        x.append(list(map(float, i[0:4])))
        y.append(i[4:5])

    kernel_pos = kmeans(x)
    print(kernel_pos)

    # print('best')
    # print(min_dist)
    # print(best_kernel_pos)
    # flag = cal_flag(best_kernel_pos, x)
    # print(flag)

    context = mp.get_context('fork')

    process_queue = context.Queue(maxsize=5000)
    process_pool = context.Pool(initializer=cal_kmeans_loop, initargs=(x, 10000, process_queue))
    process_pool.close()
    process_pool.join()
    # process_queue.close()
    print('-----------')
    best_item = (0xFFFFFFF, 0)
    try:
        while True:
            item = process_queue.get(timeout=5)
            if item[0] < best_item[0]:
                best_item = item
            print(best_item)
    except Empty as e:
        print(best_item)
    except Exception as e:
        print(e)
        print(best_item)

    record_file = open("record-" + str(best_item[0]) + ".dump", mode='wb')
    #pickle.dump((RECORD_DATA, RECORD_SUPPORT), record_file)
    pickle.Pickler(record_file).dump(best_item)
    record_file.close()
