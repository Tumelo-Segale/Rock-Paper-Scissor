import random

def get_user_choice(): # Get user's choice
    user_input = input("Enter Rock, Paper, or Scissors: ").lower()
    if user_input in ['rock', 'paper', 'scissors']: # Choices to select from
        return user_input
    else: # If user entered something not in the choices
        print("Invalid choice. Please try again.")
        return get_user_choice()

def get_computer_choice(): # Computer chooses from given choices
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices) # Select choice at random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice: # If game is a tie
        return "It's a tie!"
    elif user_choice == 'rock' and computer_choice == 'scissors': # If user wins
        return "You win!"
    elif user_choice == 'paper' and computer_choice == 'rock':
        return "You win!"
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return "You win!"
    else:
        return "You lose!" # If computer wins/If user loses

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"You chose: {user_choice}") # Display user's choice
    print(f"Computer chose: {computer_choice}") # Display computer's choice
    
    result = determine_winner(user_choice, computer_choice) # Determine the winner
    print(result) # Display the result

play_game()

while True:
    play_again = input("Do you want to play again? (yes/no): ").lower() # Ask if user wants to play again
    if play_again == 'yes':
        play_game() # If user wants to play again
    else:
        print("Thanks for playing!")
        break
#886356
