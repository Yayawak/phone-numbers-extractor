import numpy as np
import random
random.seed(0)

def get_one_random_number():
    ret = []
    # for d in range(10):
    for d in range(6):
        r = random.randint(0, 9)
        if d == 0:
            # while r == 0:
            while r < 7 or r == 9:
                r = random.randint(0, 9)
        ret += [r]
    return ret

        
def gen_unique_random_numbers(N):
    # N = 40
    # N = 40
    ret = []
    for i in range(N):
        # if get_one_random_number() in ret:
        r = get_one_random_number()
        while r in ret:
            r = get_one_random_number()
        ret += [r]

    return ret
    # print(get_one_random_number())


def sort_numbers(numbs):
    X = []
    for i in range(len(numbs)):

        # for d in numbs[i]:
        sumsum = 0
        nn = len(numbs[0])
        for j in range(nn):
            t = numbs[i][j] + 1 # prevent value mul 0 causes nothing
            # t = t * (10 ** j)
            t = t * (10 ** (nn - j - 1))
            sumsum += t
        
        X += [(numbs[i], sumsum)]
    # print(X)
    X.sort(key=lambda duo: duo[1])
    # sorted()
    # for i in range(len(X)):
    #     print(X[i][0])
    # # print(x)

    ret = []
    for duo in X:
        ret += [duo[0]]
    return ret

def pretty_print(numbs):
    n = len(numbs)
    if n == 0:
        print("numbers length = ", 0)
        return
    for i in range(n):
        print(numbs[i])
        # print(numbs[i], end)
    # print(numbs)

x = gen_unique_random_numbers(40)

# pretty_print(x)

x = sort_numbers(x)

# pretty_print(x)
    