flag=True
while flag:
    user_input=int(input("Enter the desired number\n"))
    if isinstance(user_input,int):
        s=0

        num=user_input
        while num>0:
            number_digit = num%10
            s+=number_digit**3
            num//=10


        if user_input==s:
            print("YES,This is an Armstrong Number")
            flag=False

        else:
            print("NO,This is not an Armstrong Number")
            print("If you wanna try again type YES if you dont wanna continue press any key")
            user_input_2= input().upper()
            if user_input_2 == "YES":
                flag=True
            else:
                flag=False
    else:
        print("invalid input try again")