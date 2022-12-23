'''
Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
list = [2,(1.5)**2,...(1+1/n)**n]
''' 
n = int(input("Enter the n= "))

list = []
sum_elem = 0
i=0
while i<n:
    k=round((1+1/(i+1))**(i+1), 2)
    list=list + [k]
    sum_elem+=list[i] #or +=k
    i+=1
print(f"list={list} -> sum_elem={sum_elem}")

