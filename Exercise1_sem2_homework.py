'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
'''
'''
#Variant1
m = float(input("Enter the float number m= "))

while m%10>0:
    m=round(m*10, 10)

sumNum=0
while m/10>0:
    sumNum = int(sumNum+m%10)
    m=m//10
print("-> ", sumNum)
'''
#variant2
m = input("Enter the number m= ")

sumNum=0
for x in m:
    if x !=".":
        sumNum = sumNum+int(x)
print("-> ", sumNum)
