import sys
from math import sqrt
def eroatosthenes(num:int):
    if num <= 1: return False
    prime=[2]
    limit = int(sqrt(num))
    data = [i for i in range(3,num,2)]
    while limit >= data[0]:
        prime.append(data[0])
        data=[d for d in data if d % data[0]!=0 ]
    return prime+data

def run():
    ret = eroatosthenes(int(sys.argv[1]))
    print(ret)
    
if __name__ == "__main__":
    run()