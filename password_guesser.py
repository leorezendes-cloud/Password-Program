#!/usr/bin/env python3


from password_program import check_pin



for number in range(0, 100000):
    guess = str(number).zfill(5)
    if check_pin(guess):
        print(guess)
        print('Password Found')
        break
