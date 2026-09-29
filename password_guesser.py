#!/usr/bin/env python3


from password_program import check_pin
from itertools import product
import time
import string
print()
print()
print(f'==============================')
print(f'++++++++++++++++++++++++++++++')
print(f'      Password Checkah')
print(f'++++++++++++++++++++++++++++++')
print(f'==============================')

count = 0
start = time.perf_counter()
for length in range(1, 6):
    for number in product(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, repeat=length):
        count += 1
        guess = ''.join(number)
        if check_pin(guess):
            print()
            print('*****')
            print(guess)
            print('*****')
            print('Password Found')
            print()
            end = time.perf_counter()
            break
    

elapsed = end - start
print()
print(f'Time : {round(elapsed, 2)}')
print() 
print(f'Guesses: {count:,}')
print()
guess_per_sec =  count / elapsed
print(f'Guesses per second: {guess_per_sec:,.2f}')    
print()


