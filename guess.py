import random

figure= random.randint(1,100)
#print(figure)
def guess():
    count=1
    guess=int(input(f"Enter a guess between 1 and 100: "))

    while guess != figure and count < 9:
        if count == 3:
            print(f"The number is between {figure - random.randint(4,7)} and {figure + random.randint(5,11)}")
        elif count == 6: 
            print(f"The number is between {figure - random.randint(1,5)} and {figure + random.randint(1,7)}")

        if guess > figure: 
            print("Too High!")
        elif guess < figure:
            print("Too Low!")

        
        print("Try again!")
        print(f"Your remaining guesses are {9 - count}")
        guess=int(input(f"Enter a guess between 1 and 100: "))
        count=count+1
    if guess == figure: 
        print(f"You got it in {count} guesses!!!")
    else: 
        print("You are out of tries!")
        print(f"The number was: {figure}")

guess()