from random import*

flag=0
while flag ==0:
     n=int(input("enter the length of the array"))
     if n<50:
        flag=1
     else:
         flag=0

random_int_list =[]
random_int_list=sample(range(50),n)


print(random_int_list)
