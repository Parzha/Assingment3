input_string=input("please enter the sentence\n")

counter=0
for chars in input_string:
    if chars == " ":
        counter+=1


counter+=1
if counter>1:
    print("the number of words are ",counter)
elif counter==0:
    print("zero words")
else:
    print("one word only")