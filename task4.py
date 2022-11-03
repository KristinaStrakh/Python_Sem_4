#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

#number=int(input("Введите число: "))
#for i in range(1, number +1 ):
#    if(number % i == 0):
#        print(i)


#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
#многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

#from random import randint

#cofs = []
#k = int(input('Введите степень многочлена: '))

#for i in range(k + 1):
#    num = randint(0, 100)
#    cofs.append(num)

#print(cofs)
#result = ''
#for i in range(len(cofs)):
#    if len(result) > 0 and cofs[i] > 0:
#        result = result + ' + ' 
#    if cofs[i] == 0:
#        continue
#    result = result + str(cofs[i]) + 'X^' + str(k - i)  

#if cofs[ -1 ] != 0:
#    result = result[:len(result) - 3]
#result = result + ' = 0'            
#print(result)

#with open ('file.txt', 'w') as f:
#    f.write(result)



#Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


a = [int(i) for i in input().split()]
for i in range(len(a)):
   flag = 1
   for j in range(len(a)):
      if a[i] == a[j] and i != j:
         flag = 0
         break
   if flag:
      print(a[i])