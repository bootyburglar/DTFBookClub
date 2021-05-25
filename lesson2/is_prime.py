from math import sqrt
import sys
def is_prime(num):
    if num <=1: return False
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0: return False
    return True
def prime_in_range(num):
    for i in range(num):
        if is_prime(i):
            print(i,end=' ')




def run(num:int):
    prime_in_range(num)

if __name__ == '__main__':
    num = int(sys.argv[1])
    run(num)