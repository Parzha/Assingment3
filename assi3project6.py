
flag=True
number_list = []

while flag:
    user_input=int(input("Please enter the numbers you want? "))
    number_list.append(user_input)
    user_input_2=input("If you wanna continue type yes or 1 if you want to stop type anything= ").lower()
    if user_input_2=="1" or user_input_2=="yes":
        flag=True
    else:
        print("created list is ",number_list)
        flag=False
sorted_list = sorted(number_list)


if sorted_list == number_list:
    print("This list array is sorted ",number_list)
else:
    print("This array is not sorted ",number_list)