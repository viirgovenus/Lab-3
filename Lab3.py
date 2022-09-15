

print("Welcome to the Flarsheim Guesser!")

replay = True

# create nested loop to continously run

while replay:
    print()
    print("Please think of a number between and including 1 and 100")
    print()

    re3 = int(input("What is the remainder when your number is divided by 3?")) # handling the errors
    while (re3 < 0) or (re3 >= 3):
        if (re3 < 0):
            print("The value entered must be greater than 0")
        elif (re3 >= 3):
            print("The value entered must be less than 3")
        else:
            print("Please enter a valid number")
        re3 = int(input("What is the remainder when your number is divided by 3?"))
        
    list3 = [] # creating empty list to divide all numbers by 3

    if (re3 == 0) or (re3 == 1) or (re3 == 2):
        for i in range(1, 101):
            rem3 = i % 3
            if (rem3 == re3):
                list3.append(i)

    re5 = int(input("What is the remainder when your number is divided by 5?")) # handling the errors
    while (re5 < 0) or (re5 >= 5):
        if re5 < 0:
            print("The value entered must be greater than 0")
        elif re5 > 5:
            print("The value entered must be less than 5")
        else:
            print("Please enter a valid number")
        re5 = int(input("What is the remainder when your number is divided by 5?"))

    list5 = []

    if (re5 == 0) or (re5 == 1) or (re5 == 2) or (re5 == 3) or (re5 == 4):
        for i in list3:
            rem5 = i % 5
            if (rem5 == re5):
                list5.append(i)


    re7 = int(input("What is the remainder when your number is divided by 7?")) #handling the errors
    while (re7 < 0) or (re3 >= 7):
        if re7 < 0:
            print("The value entered must be greater than 0")
        elif re7 > 7:
            print("The value entered must be less than 7")
        else:
            print("Please enter a valid number")
        re7 = int(input("What is the remainder when your number is divided by 7?"))

    list7 = []

    if (re7 == 0) or (re7 == 2) or (re7 == 3) or (re7 == 4) or (re7 == 5) or (re7 == 6): #calculating the remainders from past
        for i in list5:
            rem7 = i % 7
            if (rem7 == re7):
                list7.append(i)

# Generating the total number

    print("Your number is...", list7[0])
    print("How cool is that???")
    print()
    

# to restart or end the game
    while True:
        replay = input("Would you like to play again? Choose Y for yes, or N for no.")
        if replay == "Y":
            break
        elif replay == "N":
            break
        else:
            print("Please enter a valid character")
        



