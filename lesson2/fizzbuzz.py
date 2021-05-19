
MultiOfThree='Fizz'
MultiOfFive='Buzz'
MultiOfTF=MultiOfThree+MultiOfFive
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(MultiOfTF)
    elif i%3==0:
        print(MultiOfThree)
    elif i%5==0:
        print(MultiOfFive)
    else:
        print(i)
