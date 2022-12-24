'''
Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)
'''
list = ['Hi', 456, 4.5, [2, 4, 1,] ]
print(list)

import random
i1 = random.randint(0,3)
i2 = random.randint(0,3)
print(f"{i1} позицию меняем с позицией {i2}: Получаем")

for i in range(len(list)):
    if i == i1:
        temp=list[i1]
        list[i1]=list[i2]
        list[i2]=temp
print(list)