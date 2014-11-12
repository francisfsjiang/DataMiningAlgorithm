# encoding: utf-8

Feature = 4
NumofFeatures = [3, 3, 2, 2]
NumofSample = 14

ProbofFeature = []
Trans = {
    "young": 0,
    "middle": 1,
    "old": 2,
    "low": 0,
    "medium": 1,
    "high": 2,
    "no": 0,
    "yes": 1,
    "fair": 0,
    "excellent": 1
}


def spl(s):
    return list(map(int, s.split()))


def calc_prob(x, y):
    for fea in range(Feature):
        now = [[0, 0] for i in range(NumofFeatures[fea])]
        print(now)
        stat = [0,0]
        for i in range(NumofSample):
            a = x[i][fea]
            b = y[i][0]
            now[a][b] += 1
            stat[b] += 1
        for i in range(NumofFeatures[fea]):
            now[i][0] /= stat[0]
            now[i][1] /= stat[1]
        print(now)
        ProbofFeature.append(now)

def parse_age(s):
    age = int(s)
    if age <= 30:
        return "young"
    elif age > 40:
        return "old"
    else:
        return "middle"


if __name__ == '__main__':
    m = map(spl, open("x.txt").readlines())
    x = list(m)
    print(x)
    m = map(spl, open("y.txt").readlines())
    y = list(m)
    print(y)
    calc_prob(x, y)

    print(ProbofFeature)

    while True:
        s = input('-->')
        request = s.split()
        request[0] = parse_age(request[0])
        print(request)
        result1 = 1
        result0 = 1
        for i in range(1, len(request)):
            result1 *= ProbofFeature[i][Trans[request[i]]][1]
            result0 *= ProbofFeature[i][Trans[request[i]]][0]
        print(result1, result0)
        if result1 > result0:
            print("Yes")
        else:
            print("No")