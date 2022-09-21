



def cutededler(x):
    if x % 2 == 0:
        return x
    else:
        None


## filter example:

def filtertest():
    eded = list(range(3,12))
    return list(filter(cutededler,eded))

print(filtertest())


#netice:
# [4, 6, 8, 10]