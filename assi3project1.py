from random import*


list_words = ['eagle','fox','elephant','donkey','monkey','zebra','wolf','dolphin']


rand_word=choice(list_words)
rand_word_blanks = "_"*len(rand_word)
picked_list = []


print("guess the animal ")
print("_" * len(rand_word))
lives = 5
flag=False
user_guessed_letters = []
user_guessed_words = []

while not flag and lives >0: #mitonestam hameie inaro to fucntion bezaran

    user_guess = input("please enter your first letter\n").lower()


    if len(user_guess)==1 and user_guess.isalpha():
        if user_guess in user_guessed_letters:
            print("already picked letter")
        elif user_guess not in rand_word:
            lives-=1
            print("Wrong guess you lost a life current lives are =",lives)
        else:
            print("you got it right")
            user_guessed_letters.append(user_guess)
            list_rand_word_blanks = list(rand_word_blanks)
            indices = [i for i,letter in enumerate(rand_word) if letter == user_guess]
            for index in indices:
                list_rand_word_blanks[index]=user_guess
            rand_word_blanks = "".join(list_rand_word_blanks)
            if "_" not in rand_word_blanks:
                flag=True

    elif len(user_guess) == len(rand_word) and user_guess.isalpha():
        if user_guess in user_guessed_letters:
            print("You already tried ")
        elif user_guess != rand_word:
            print(user_guess, " This is not the word buddy")
            lives -= 1
            user_guessed_letters.append(user_guess)
        else:
            flag = True
            rand_word_blanks = rand_word
    else:
        print("invalid input")
    #
    print(rand_word_blanks)

if flag:
        print("YOU DID ITTTTT!")
else:
        print("Thats big L in my book you ran out of lives and the correct the word is ",rand_word )











