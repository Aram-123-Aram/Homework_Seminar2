'''
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. Позиции хранятся в отдельном 
списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].
'''
N = int(input("Enter the number N= "))
list=[-N]

i=1
while i<2*N+1:
       list=list+[-N+i]
       i+=1
print(f"list = {list}")
print()
lst1 = [list[2], list[0], list[1], list[3]]
lst2=[list[2], list[0]]

def UmnFunc(lstnew):
       umn_elem=1
       for x in lstnew:
              umn_elem = umn_elem*x
       return umn_elem
print(f"lst1 = {lst1} \n->Произведение элементов на указанных позициях равно -> {UmnFunc(lst1)}")
print(f"lst2 = {lst2} \n->Произведение элементов на указанных позициях равно -> {UmnFunc(lst2)}")

