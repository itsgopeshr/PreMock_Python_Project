import random

def play_rps(user_choice):
    options = ['stone', 'paper', 'scissors']
    computer_choice = random.choice(options)
    
    user_choice = user_choice.lower()
    
    if user_choice not in options:
        return None, computer_choice, "Invalid choice."
        
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You Win!"
    else:
        result = "Computer Wins!"
        
    return result, computer_choice, "Success"