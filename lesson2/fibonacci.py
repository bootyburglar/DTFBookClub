import sys

def fibonacci(n):
    fib = [1,1]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n-1]

def run():
    
    ret = fibonacci(int(sys.argv[1]))
    print(ret)

if __name__ == '__main__':
    run()