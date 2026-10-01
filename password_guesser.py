#!/usr/bin/env python3


from password_program import check_pin
from itertools import product
import time
import string


character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
benchmark = 18000000
max_length = 8
def table(character_set, max_length, benchmark):
    print()
    print()
    print(f'=======================================')
    print(f'+++++++++++++++++++++++++++++++++++++++')
    print(f'           Password Checkah')
    print(f'+++++++++++++++++++++++++++++++++++++++')
    print(f'=======================================')
    print(f'{"Length"}| {"Possibilities":>16} |{"Est. Max Time":>6}')
    print(f'_______________________________________')
    for length in range(1, max_length + 1):
        combinations = len(character_set) ** length
        est_time = (combinations / benchmark)
        if est_time < 1:
            est_time = f'< 1 sec'
        elif est_time >= 1 and est_time <= 60:
            est_time = f'{est_time:.1f} secs'
        elif est_time > 60 and est_time <= 3600:
            est_time = f'{est_time/60:.1f} mins'
        elif est_time > 3600 and est_time<=86400:
            est_time = f'{est_time/3600:.1f} hours'
        elif est_time > 86400 and est_time <=31536000:
            est_time = f'{est_time/86400:.1f} days'
        elif est_time > 31536000:
            est_time = f'{est_time/3153600:.2f} yrs'
       
        print(f'{length:<4} {combinations:>21,} {est_time:>12}' )
        
table(character_set, max_length, benchmark)

        


def checker(character_set, max_length):
    count = 0
    start = time.perf_counter()
    loading = f'*Clears throat*'
    for length in range(1, max_length + 1):
        last_update = time.perf_counter()
        combinations = len(character_set) ** length
        new_count = 0
        if length == 1:
            print()
            print(f'\r{loading}', end=" | ")
        if length == 2:
            loading = 'Calculating'
            print(f'{loading}', end = " ")
        if length == 3:
            loading = 'Alright Checking Passwords'
            print()
            print(loading)
        for number in product(character_set, repeat=length):
            count += 1
            new_count += 1
            guess = ''.join(number)
            now = time.perf_counter()
            update_time = now - last_update
            if update_time >= 1:
                progress = (new_count / combinations) * 100
                print(f'\rChecking Length {length}', end=" | ")
                print(f'Progress: {progress:.2f}%', end="", flush=True)
                last_update = now
            if count == 300000000:
                loading ='Damn, is this Fort Knox?? .. 4 to 5 mins..'
                print()
                print(loading)
                print()
            if check_pin(guess):
                print()
                print('*****')
                print(guess)
                print('*****')
                print('Password Found')
                print()
                end = time.perf_counter()
                elapsed = end - start
                print(f'Time : {round(elapsed, 2)}')
                print() 
                print(f'Guesses: {count:,}')
                print()
                guess_per_sec =  count / elapsed
                combinations = len(character_set) ** length
                print(f'Guesses per second: {guess_per_sec:,.2f}') 
                print()
                return
    print()
    print('Password Not Found, My bad brodie') 
    print()
    print('This must be military grade security')
    print()
    print('Has to be, the Checkah never fails!!')
    print()
    print()
checker(character_set, max_length)
    



