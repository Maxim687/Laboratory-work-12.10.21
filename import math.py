import math
x =int(input("x:"))
a =int(input("a:"))
b =int(input("b:"))
e = a * b
z = (int(e)** x + (math.sin(x)) - (math.cos(2 * x)))
print (str(z))
n = int(input("Введіть ціле число:"))
print("Прості дільники числа:", end = " ")
for i in range(n - 1,1,-1):
    is_simple = 0
    if (n % i ==0):
        for j in range(i -1,1,-1):
            if (i % j == 0):
                is_simple = is_simple + 1
        if (is_simple ==0):
            print(i, end = " ")       
N = [-7,-5,-3,-2,1,3,5,7]
print("Найменше число N:" + str(min(N)))
F = [-7,-5,-3,-2]
print("Сума від'ємних чисел:" + str(sum (F)))    
