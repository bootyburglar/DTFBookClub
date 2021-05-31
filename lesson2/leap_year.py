
def check_leap_year(year:int):
    if (year%4 == 0):
        if ((year%100==0) and year%400!=0):
            return False
        else:
            return True
    return False
    
import sys
def run():
    for i in range(1950,2050+1):
        print(f'{i} -     leap year') if check_leap_year(i) else print(f'{i} - not leap year')
if __name__ == '__main__':
    run()