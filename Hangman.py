#Code for hangman game in ptyhon

import random
# randoom module  is used in order to select random word from list


def hangman( ):
    words = ['science', 'computer', 'ordinary', 'cricket',
             'assignment', 'beautiful', 'dance', 'friend', 'program', 'string']
    word= random.choice(words)
    #function will choose random word
    attempt=6
    guessmade=''
    valid_entry=set('abcdefghigklmnopqrstuvwxyz')
# to enter only valid char

    while (len(word)>0) is True:
        real_word=""


        for letter in word:
            # comparing that character with
            # the character   in guesses
            if letter in guessmade:
                real_word=real_word+letter
            else:
                real_word=real_word+"_"

        if real_word==word:
            # when guess is correct
            print(word, "is correct word")
            print("Congrats!!!",name," you won the game!!!")
            break

        print("Guess the word", real_word)
        guess = input()

        if guess in valid_entry:
            #to check the guess
            guessmade= guessmade+guess
        else:
            print("please enter lower case character")
            guess=input()
        if guess not in word:
            #if guess is not correct
            attempt = attempt-1

            if attempt==5:
                print("5 attempts are left!!!")
                print("   ______    \n"
                      "  |          \n"
                      "  |          \n"
                      "  |          \n"
                      "  |          \n")


            elif attempt==4:
                print("4 attempts are left!!!")
                print("   ______    \n"
                      "  |      |   \n"
                      "  |          \n"
                      "  |          \n"
                      "  |          \n")
            elif attempt==3:
                print("3 attempts are left!!!")
                print("   ______    \n"
                      "  |      |   \n"
                      "  |      O   \n"
                      "  |          \n"
                      "  |          \n")
            elif attempt==2:
                print("2 attempts are left!!!")
                print("   ______    \n"
                      "  |      |   \n"
                      "  |      O   \n"
                      "  |      |   \n"
                      "  |          \n")
            elif attempt==1:
                print("last attempt are left!!!")
                print("   ______     \n"
                      "  |      |    \n"
                      "  |    \ O /  \n"
                      "  |      |    \n"
                      "  |           \n")
            else:
                print("   ______      \n"
                      "  |      |     \n"
                      "  |    \ O /   \n"
                      "  |      |     \n"
                      "  |    /   \    \n")
                print("sorry",name, "but lost the game!!!","real word was",word)
                break


name = input("What is your name? ")
print("Good Luck ! ", name)
print("Try to gess the word in less than 6 attempt")
hangman()
