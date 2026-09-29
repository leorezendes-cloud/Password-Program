#!/usr/bin/env python3

from pathlib import Path
from getpass import getpass
from utilities import get_choice


def main_menu():
    print()
    print(f'1. Access File')
    print()
    print(f'2. Change PIN')
    print()
    print(f'3. Exit')
    print()
    choice = get_choice(3)
    match choice:
        case 1:
            print('Welcome to the good stuff!!!')
            print()
            print('Would you like to go back to the menu?')
            print()
            menu_choice = get_choice(2)
            match menu_choice:
                case 1:
                    main_menu()
                case 2:
                    print()
                    print('Goodbye, Signing out')
                    print()
        case 2:
            while True:
                print()
                entered_pin = getpass('Confirm old PIN to change PIN: ')
                print()
                user_pin = pin_file.read_text()
                if entered_pin == user_pin:
                    while True:
                        print('WARNING : PIN will not display characters!!')
                        new_pin = getpass('Enter your new PIN: ')
                        print()
                        print()
                        print()
                        check_pin = getpass('Confirm your new PIN: ')
                        if new_pin == check_pin:
                            pin_file.write_text(new_pin)
                            print()
                            print('PIN has changed')
                            print()
                            break    
                        else: 
                            print()
                            print("PIN's DO NOT MATCH, try again")
                            print()
                    main_menu()
                    break
                else:
                    print()
                    print('Wrong PIN, try again')
                    print()
        case 3:
            print()
            print('Goodbye, Signing out')
            print()
            return
    return        

    
pin_file = Path('pin.txt')

def check_pin(guess):
    if guess == pin_file.read_text():
        return True
    else:
        return False


if __name__ == '__main__':
        if not pin_file.exists():
            print('No PIN found Create a new PIN')
            print('WARNING : PIN will not display characters!!')
            user_pin = getpass('Enter your new PIN: ')
            pin_file.write_text(user_pin)
            main_menu()
        else:
            user_pin = pin_file.read_text()
            while True:
                entered_pin = getpass('Enter your PIN: ')
                if entered_pin == user_pin:
                    print('Welcome')
                    main_menu()
                    break
                else:
                    print()
                    print('Wrong PIN try again')
                    print()


