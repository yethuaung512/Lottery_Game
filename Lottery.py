import random
import time
import sys

random_number = random.randint(1, 5)

player = False

def rules():
    print(">You must be 18 or older than 18.")
    print(">You must have at least $5000.")
    print(">You must use 1000 at least every single time.")
    print(">Your name must be more than one alphabelt.")
    print(">You should not bet more than you have.")

def again():
    bet_money = int(input("Bet your money: $"))
    if bet_money > sMoney:
        print("You don't have enough money, please check your balance.")
        rules()
    elif bet_money < 999:
        rules()
    else:
        left_money = sMoney - bet_money
        print("You've left $", left_money)
        print("If you win, you'll get 10 times of your money. Be lucky!!")
        guess_number = int(input("Guess your lucky number(1-5): "))
        while guess_number == random_number:
            money_won = bet_money * 10
            print("This is the money you won", money_won, "$")
            total_money = money_won + left_money
            print("You've got $", total_money)
            print("You wanna play again? yes or no\n")
        else:
            print("Sorry, the lucky number is", random_number)
            print("You wanna play again? yes or no\n")

while player == False:
    print("__Wecome to our lottery Game__")
    print("Press 1 to read rules and regulations and Press 2 to start the game.")
    press = input("Chosen number: ")
    if press == "1":
        rules()
    else:
        print("Let's start the game now!")
        if True:
            name = input("Please enter your name: ")
            age = int(input("Please enter your age: "))
            if len(name) > 2 and age > 18:
                print("The game will start in 3 seconds.")
                time.sleep(3)
                while True:
                    sMoney = int(input("Type the amount of your show money: $"))
                    if sMoney > 4999:
                        print("This is your money $", sMoney)
                        again()
                        Choice = input("Choose: ")
                        if Choice.lower() == "yes":
                            again()
                        else:
                            print("Press 0 to quit the game. See you again!")
                            quit = int(input(""))
                            if quit == 0:
                                sys.exit("This will end in 3 seconds.")
                            time.sleep(3)
                    else:
                        print("Please get more money.")
                        rules()
            else:
                print("You must be over 18 or your name should be more than two alphabelt.")
else:
    print("Read the rules again.")
    rules()


