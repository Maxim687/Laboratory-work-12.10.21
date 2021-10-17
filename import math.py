import math
x =int(input("x:"))
a =int(input("a:"))
b =int(input("b:"))
e = a * b
z = e ** x + math.sin(x) - math.cos(x) * 2
print (str(z))
n = int(input("Введіть ціле число:"))
print("Результат:", end = " ")
for i in range(n - 1,1,-1):
    if(n % i ==0):
        print(i,end = " ")
N = [-7,-5,-3,-2,1,3,5,7]
print("Найменше число N:" + str(min(N)))
F = [-7,-5,-3,-2]
print(str(sum (F)))    
