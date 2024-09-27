#1
try:
    num = int(input('введите число'))
    if num > 0:
        print('число положительное')
except(ValueError):
    print('пиши цифру')
#2
try:
    num = int(input('введите число'))
    if num % 2 == 0:
        print('чётное')
    else:
        print('не чётное')
except(ValueError):
    print('пиши цифру')
#3
try:
    num = int(input('введите число'))
    if num > 9 and num < 21:
        print('true')
    else:
        print('false')
except(ValueError):
    print('пиши цифру')
#4
try:
    num = int(input('введите число'))
    num_2 = int(input('введите число'))
    if num > 9 and num_2 > 9:
        print('true')
    else:
        print('false')
except(ValueError):
    print('пиши цифру')
#5
try:
    num = int(input('введите число'))
    if num == 0:
        print('0')
    else:
        if num < 0:
            print('отрицательное')
        else:
            print('положительное')
except(ValueError):
    print('пиши цифру')
#6
try:
    num = int(input('введите число'))
    num_2 = int(input('введите число'))
    num_3 = int(input('введите число'))
    if num % 2 == 0 or num_2 % 2 == 0 or num_3 % 2 == 0:
        print("Есть четное число")
except(ValueError):
    print('пиши цифру')