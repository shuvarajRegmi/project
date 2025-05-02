#generate a random number 
#loop
#ask thr user to make a guess
#if not a valid number 
#print an error 
#if number < guess 
#print too low 
# if number > guess 
#print too high 
#else 
#print well done

import random
number_to_guess=random.randint(1,100)
while True:
    try:
        guess=int(input('Guess the number between 1 and 100:'))

        if guess < number_to_guess:
         print('too low')    
        elif guess > number_to_guess:
         print('too hugh!')
        else:
            print('Congratulation! you gussed the number.')
            break
    except ValueError:
     print('please enter a valid number.')

    
    