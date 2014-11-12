# encoding: utf-8


def map_split(s):
    return set(s.split())


def is_set_in_list(i_set: set, i_list: list):
    if i_set in i_list:
        return True
    return False


def count_set_appear_time_in_list(i_set: set, i_list: list):
    result = 0
    for i in i_list:
        if i_set.issubset(i):
            result += 1
    return result


def appriori(origin_data: list, item_list: list, now_data: list, time_boundary: int):
    #Select item which satisfy time_boundary
    appear_time = []
    new_data = []
    for i in now_data:
        count = count_set_appear_time_in_list(i, origin_data)
        if count > time_boundary:
            new_data.append(i)
            appear_time.append(count)
    print(new_data, appear_time)

    #Generate new data
    generated_data = []
    for i in new_data:
        for j in new_data:
            tmp = i.union(j)
            if len(tmp) == len(i)+1:
                #print(tmp)
                count = count_set_appear_time_in_list(tmp, origin_data)
                #print(count)
                if count > time_boundary and not is_set_in_list(tmp, generated_data):
                    generated_data.append(tmp)
    #print(generated_data)
    if generated_data != []:
        appriori(origin_data, item_list, generated_data, time_boundary)


if __name__ == '__main__':
    origin_data_file = open('data.txt', mode='r', encoding='utf-8')
    origin_data = list(map(map_split, origin_data_file.readlines()))
    print(origin_data)

    data = []
    appear_time = []
    for i in origin_data:
        for j in i:
            if {j} not in data:
                data.append({j})

    item_list = data

    print(data)
    print(count_set_appear_time_in_list(data[0], origin_data))

    appriori(origin_data, item_list, data, 2)