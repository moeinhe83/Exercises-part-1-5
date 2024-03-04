# Practice_5

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('cls')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 5', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

# Value Input
number = int(input('Enter Number ==> '))

# IF
if number % 3 == 0 and number % 6 == 0:
    print(colored('==================================='))
    print(colored(f'{number} By 3 and 6', color='green'))

elif number % 3 == 0:
    print(colored('==================================='))
    print(colored(f'{number} By 3', color='blue'))

elif number % 6 == 0:
    print(colored('==================================='))
    print(colored(f'{number} By 6', color='yellow'))

else:
    print(colored('==================================='))
    print(colored(f'{number} NOT By 3 and 6', color='red'))

# Finish
# Create By Moein Heshmati
    