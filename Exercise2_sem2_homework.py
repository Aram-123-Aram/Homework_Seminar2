'''
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''
'''#variant1:
N = int(input("Enter the number N= "))

result = 1
i=1
while i<=N:
    result=result*i
    i+=1
    print(result,end=", ")
'''
'''#variant2:
N = int(input("Enter the number N= "))

result = 1
for i in range(N):
    i+=1
    result=result*i
    print(result, end=", ")
'''
#variant3-recursion
N = int(input("Enter the number N= "))
        
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

i=1
while i<=N:
    print(fact(i), end=", ")
    i+=1
