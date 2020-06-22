# Three Cup Monte game

from random import shuffle

# shuffle function
def shuffle_MyList(mylist):
    shuffle(mylist)
    return mylist

# Player guess function
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("pick a cup 0,1 or 2: ")
    return int(guess)

# win/lose function to verify player guess
def guess_check(mylist,guess):
    if mylist[guess] == 'O':
        print("Your guess is correct and you win the three cup Monte! Congratulations!!!")
        print(mylist)
    else:
        print("Sorry you choose wrong and you lost the game.")
        print(mylist)

# calling all the functions
mylist = ['','','O']
shuffled_List = shuffle_MyList(mylist)
guess = player_guess()
guess_check(shuffled_List,guess)
        