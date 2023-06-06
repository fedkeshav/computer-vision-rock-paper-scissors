#%%
import random

def  get_computer_choice():
    comp_choice= random.choice(['Rock', 'Paper', 'Scissors'])
    return comp_choice

def get_user_choice():
    user_choice = input('Choose your action from Rock, Paper and Scissors: ')
    return user_choice.lower().capitalize()

def get_winner(computer_choice, user_choice):
    if (computer_choice == 'Rock' and user_choice == 'Scissors') or \
        (computer_choice == 'Scissors' and user_choice == 'Paper') or \
        (computer_choice == 'Paper' and user_choice == 'Rock'):
            print('You lost')
    elif computer_choice == user_choice:
         print('It is a tie!')
    else:
         print('You win')

#%%
def play():
     computer_choice = get_computer_choice()
     user_choice = get_user_choice()
     get_winner(computer_choice,user_choice)
     print(f'Computer chose {computer_choice} and User chose {user_choice}')

# %%

play()
# %%
