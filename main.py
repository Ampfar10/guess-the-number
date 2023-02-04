import random
import os


easy = random.randint(1, 10)
medium = random.randint(1, 20)
hard = random.randint(1, 30)

print("\n")
name = input("Enter Your Name: ")
try:
    a = open(f'{name}.csv', 'w')
    a.close()
except FileNotFoundError:
        file = open(name, 'w')


print("""                                                          $$\     $$\                                                         $$\                           
                                                          $$ |    $$ |                                                        $$ |                          
 $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\       $$$$$$\   $$$$$$$\   $$$$$$\        $$$$$$$\  $$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$  __$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|      \_$$  _|  $$  __$$\ $$  __$$\       $$  __$$\ $$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  $$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\          $$ |    $$ |  $$ |$$$$$$$$ |      $$ |  $$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\         $$ |$$\ $$ |  $$ |$$   ____|      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$$ |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |        \$$$$  |$$ |  $$ |\$$$$$$$\       $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
 \____$$ | \______/  \_______|\_______/ \_______/          \____/ \__|  \__| \_______|      \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|      
$$\   $$ |                                                                                                                                                  
\$$$$$$  |                                                                                                                                                  
 \______/                                                                                                                                                   """)
print(f"Welcome {name} to guess the number game")
print(" ")
menu = input("""1.Play
2.View Score \n""")

while True:
    if menu == "1":
        level = input("Would you like to play easy/medium/hard ")
        pass
        while True:
            if level == "easy":    
                guess = input("Enter A Number from 1-10: ")
                if guess == f"{easy}":
                    print("You Win!")
                    with open(f'{name}.csv','r') as numbers_file:
                        total = +15
                        for line in numbers_file:
                            if line.strip():
                                total += int(line)
                    print(f"Score: {total}")
                    a = open(f'{name}.csv', 'w')
                    a.write(str(total))
                    a.close()
                    break
                else:
                    with open(f'{name}.csv','r') as numbers_file:
                        total = -2
                        for line in numbers_file:
                            if line.strip():
                                total += int(line)
                    print(f"Score: {total}")
                    a = open(f'{name}.csv', 'w')
                    a.write(str(total))
                    a.close()
                    print(f"Try Again")
###############################################################
            elif level == "medium":    
                guess = input("Enter A Number: ")
                if guess == f"{medium}":
                    print("You Win!")
                    with open(f'{name}.csv','r') as numbers_file:
                        total = +25
                        for line in numbers_file:
                            if line.strip():
                                total += int(line)
                    print(f"Score: {total}")
                    a = open(f'{name}.csv', 'w')
                    a.write(str(total))
                    a.close()
                    break
                else:
                    with open(f'{name}.csv','r') as numbers_file:
                        total = -4
                        for line in numbers_file:
                            if line.strip():
                                total += int(line)
                    print(f"Score: {total}")
                    a = open(f'{name}.csv', 'w')
                    a.write(str(total))
                    a.close()
###############################################################
            elif level == "hard":    
                guess = input("Enter A Number: ")
                if guess == f"{hard}":
                    print("You Win!")
                    with open(f'{name}.csv','r') as numbers_file:
                        total = +50
                        for line in numbers_file:
                            if line.strip():
                                total += int(line)
                    print(f"Score: {total}")
                    a = open(f'{name}.csv', 'w')
                    a.write(str(total))
                    a.close()
                    break
                else:
                    with open(f'{name}.csv','r') as numbers_file:
                        total = -6
                        for line in numbers_file:
                            if line.strip():
                                total += int(line)
                    print(f"Score: {total}")
                    a = open(f'{name}.csv', 'w')
                    a.write(str(total))
                    a.close()
    
            else:
                print("Invalid Option")
                break
    elif menu == "2":
        print("Coming soon")
        break
