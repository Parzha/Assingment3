
factorial_list_cheating=[1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87178291200]
flag= True
while flag == True:

 user_input = int(input("enter your desired number"))
 if isinstance(user_input,int):

    if user_input in factorial_list_cheating:
        print("YES")
        input_index = factorial_list_cheating.index(user_input)
        print(user_input,"=",input_index+1,"!","=",end="")
        for i in range(1,input_index+2):
            print(i,end='')
            if i<input_index+1:
                print("*",end='')
        flag=False
    else:
        print("NO, if you wanna try again type YES if you dont press any key")
        user_second_input=input().upper()
        if user_second_input=="YES":
            flag=True
        else:
            flag=False



 else:
     print("invliad input Try again")