# encoding: utf-8
import pickle


def get_set_support(record_data:list, record_support:list, target:set):
    for i in range(len(record_data)):
        for j in range(len(record_data[i])):
            if record_data[i][j] == target:
                return record_support[i][j]


if __name__ == '__main__':
    record_file = open("record.dump", mode="rb")
    record_data, record_support = pickle.Unpickler(record_file).load()
    record_file.close()
    # for i in record_data:
    #     print(len(i))
    # for i in record_support:
    #     print(len(i))
    while True:
        s = input("--------------------------------------------\nsup 支持度\nconf 置信度\n-->")
        if s == 'sup':
            x = input("target set split by space\n-->")
            x = set(x.split())
            print("sup = ", get_set_support(record_data, record_support, x))
        elif s == 'conf':
            x = input("X set split by space\n-->")
            y = input("Y set split by space\n-->")
            x = set(x.split())
            y = set(y.split())

            sup_x_union_y = get_set_support(record_data, record_support, x.union(y))
            sup_x = get_set_support(record_data, record_support, x)
            print("x∩y sup = ", sup_x_union_y)
            print("x sup = ", sup_x)
            print("conf = ", sup_x_union_y/sup_x)
        else:
            continue
