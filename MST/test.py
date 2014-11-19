# encoding: utf-8

import pickle

file = open('record.dump', mode='rb')
pk = pickle.load(file)
file.close()
print(pk)
for i in pk:
    print(i)
    print(len(i))