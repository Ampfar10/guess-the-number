import random
import os
import time
from plyer import notification

#Guess The Number
def guess_the_number(name):
    # Number of tries
    easy_tries = 6
    medium_tries = 16
    hard_tries = 20
    

    #levels
    easy = random.randint(0, 10)
    medium = random.randint(1, 20)
    hard = random.randint(1, 30)

    #Start Of The Game
    print(f"Welcome {name} to guess the number game")
    print(" ")
    menu = input("""1.Play\n2.View Points \n3.Back\n4.Exit\n""")


    if menu == "1":
        level = input("Select a difficulty level \n1.Easy\n2.Medium\n3.Hard\n ")
########################EASY#################################
        if level == "1":
                    tries = easy_tries
                    print(f"You Have {tries} Tries\nGoodLuck...")
                    while tries > 0:
                        guess = input("Enter A Number from 1-10: ")
                        if guess == f"{easy}":
                            print("Congratulations, you won!")
                            with open(f'{name}.csv','r') as numbers_file:
                                total = +15
                                for line in numbers_file:
                                    if line.strip():
                                        total += int(line)
                            print(f"Points: {total}")
                            a = open(f'{name}.csv', 'w')
                            a.write(str(total))
                            a.close()
                            time.sleep(2)
                            guess_the_number(name)
                        else:
                            with open(f'{name}.csv','r') as numbers_file:
                                total = -5
                                for line in numbers_file:
                                    if line.strip():
                                        total += int(line)
                            print(f"Points: {total}")
                            a = open(f'{name}.csv', 'w')
                            a.write(str(total))
                            a.close()
                            tries -= 1
                            if tries == 0:
                                print(f"Game Over The Number Was {easy}")
                                time.sleep(2)
                                os.system("cls")
                                guess_the_number(name)
                            print("Try Again")
                            print(f"You have {tries} tries left.")
###########################MEDIUM#########################                    
        elif level == "2":    
                    tries = medium_tries
                    print(f"You Have {tries} Tries\nGoodLuck...")
                    while tries > 0:
                        guess = input("Enter A Number from 1-20: ")
                        if guess == f"{medium}":
                            print("Congratulations, you won!")
                            with open(f'{name}.csv','r') as numbers_file:
                                total = +25
                                for line in numbers_file:
                                    if line.strip():
                                        total += int(line)
                            print(f"Points: {total}")
                            a = open(f'{name}.csv', 'w')
                            a.write(str(total))
                            a.close()
                            time.sleep(2)
                            guess_the_number(name)
                        else:
                            with open(f'{name}.csv','r') as numbers_file:
                                total = -15
                                for line in numbers_file:
                                    if line.strip():
                                        total += int(line)
                            print(f"Points: {total}")
                            a = open(f'{name}.csv', 'w')
                            a.write(str(total))
                            a.close()
                            tries -= 1
                            if tries == 0:
                                print(f"Game Over The Number Was {medium}")
                                time.sleep(2)                                
                                os.system("cls")
                                guess_the_number(name)
                            print("Try Again")
                            print(f"You have {tries} tries left.")
########################HARD############################                  
        elif level == "3":    
                    tries = hard_tries
                    print(f"You Have {tries} Tries\nGoodLuck...")
                    while tries > 0:
                        guess = input("Enter A Number from 1-30: ")
                        if guess == f"{hard}":
                            print("Congratulations, you won!")
                            with open(f'{name}.csv','r') as numbers_file:
                                    total = +50
                                    for line in numbers_file:
                                        if line.strip():
                                            total += int(line)
                            print(f"Points: {total}")
                            a = open(f'{name}.csv', 'w')
                            a.write(str(total))
                            a.close()
                            time.sleep(2)
                            guess_the_number(name)
                        else:
                            with open(f'{name}.csv','r') as numbers_file:
                                total = -5
                                for line in numbers_file:
                                    if line.strip():
                                        total += int(line)
                            print(f"Points: {total}")
                            a = open(f'{name}.csv', 'w')
                            a.write(str(total))
                            a.close()
                            tries -= 1
                            if tries == 0:
                                print(f"Game Over The Number Was {hard}")
                                time.sleep(2)                                
                                os.system("cls")
                                guess_the_number(name)
                            print("Try Again")
                            print(f"You have {tries} tries left.")
        else:
            print("Invalid Option")
            time.sleep(2)
            guess_the_number(name)
    elif menu == "2":
        with open(f'{name}.csv','r') as numbers_file:
            total = +0
            for line in numbers_file:
                if line.strip():
                    total += int(line)
        print(f"You Have {total} Points")
        time.sleep(2)
        os.system("cls")   
        guess_the_number(name)
    elif menu == "3":
        game(name)   
    elif menu == "4":
        print("GoodBye...")
        pass  
    else:
        print("Invalid Option..")
        time.sleep(2)
        guess_the_number(name)
#TicTacToe
def tictactoe():
    print("This Game Will Be Available Soon")
    time.sleep(2)
    game(name)
#Hangman
def hangman():
    print("This Game Will Be Available Soon")
    time.sleep(2)
    game(name)

def game(name):
    print(f"""                                                          $$\     $$\                                                         $$\                           
                                                          $$ |    $$ |                                                        $$ |                          
 $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\       $$$$$$\   $$$$$$$\   $$$$$$\        $$$$$$$\  $$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$  __$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|      \_$$  _|  $$  __$$\ $$  __$$\       $$  __$$\ $$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  $$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\          $$ |    $$ |  $$ |$$$$$$$$ |      $$ |  $$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\         $$ |$$\ $$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$$ |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |        \$$$$  |$$ |  $$ |\$$$$$$$\       $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
 \____$$ | \______/  \_______|\_______/ \_______/          \____/ \__|  \__| \_______|      \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|      
$$\   $$ |                                                                                                                                                  
\$$$$$$  |                                                                                                                                                  
 \______/ \n""")
    games = input("1.Guess The Number\n2.TicTacToc\n3.Hangman\n4.Daily Points\n5.View Points\n6.Exit\n")
    if games == "1":
        print("Guess The Number")
        guess_the_number(name)
    elif games == "2":
        print("TicTacToe")
        tictactoe()
    elif games == "3":
        print("Hangman")
        hangman()
    elif games == "4":
        print("Will Be Available Soon")
        time.sleep(2)
        #daily = random.randint(1, 50)
        #with open(f'{name}.csv','r') as numbers_file:
            #total = +daily
            #for line in numbers_file:
                #if line.strip():
                    #total += int(line)
        #print(f"You Got {daily} Points\nYou Now Have {total} Points")
        #a = open(f'{name}.csv', 'w')
        #a.write(str(total))
        #a.close()
        #time.sleep(2)
        #os.system("cls")
        game(name)
    elif games == "5":
        with open(f'{name}.csv','r') as numbers_file:
            total = +0
            for line in numbers_file:
                if line.strip():
                    total += int(line)
        print(f"You Have {total} Points")
        time.sleep(2)
        os.system("cls")
        game(name)
    elif games == "6":
        print("GoodBye...")
        pass
    else:
        print("Invalid option")
        time.sleep(2)
        os.system("cls")
        game(name)
        

name = input("Welcome Please Enter Your Name: ")
if name == ' ':
    print("Name Cant Be Blank...")
else:
    try:
        a = open(f'{name}.csv', 'r')
        a.close()
        notification.notify(
            title= f"Welcome Back {name}",
            message= " Hope You Ready To Have Some Fun",
            app_name = "Guess The Number",
            app_icon='Startup.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
        )

        time.sleep(2)
    except FileNotFoundError:
        print(f"{name}.csv not found")
        time.sleep(2)
        print(f"Creating {name}.csv....")
        time.sleep(2)
        a = open(f'{name}.csv', 'w')
        a.write("20")
        a.close()
        print("Setting points to 20...")
        time.sleep(2)
        notification.notify(
            title= "New Member",
            message= f"Welcome {name} Hope You Have Fun",
            app_name = "Guess The Number",
            app_icon='Startup.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
        )

        time.sleep(2)

game(name)



    
