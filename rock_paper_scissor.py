#Ask the user to make a choice 
#if choice is not valid 
#print an error 
#lets the computer to make a choice 
#print choice (emojis)
#determine the winner 
#ask the user if they want to continue 
#if not 
#terminate
import random
choices=('r', 'p', 's')
user_choice=input('rock, paper, or scissor? (r/p/s)').lower()
#if user_choice !='r' and user_choice !='p' and user_choice !='s':
if user_choice not in choices:    
    print('Invalid choice')
computer_choice=random.choice(choices)
print(f'you chose',+ {user_choice})

    

    