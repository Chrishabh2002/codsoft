import random

# Function to prompt the user for their choice
def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = ''
    
    # Loop until a valid choice is entered
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in choices:
            print("Invalid choice! Please try again.")
    return user_choice

# Function to randomly generate the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

# Function to display the result of the round
def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

# Main function to control the flow of the game
def main():
    user_score = 0
    computer_score = 0
    play_again = 'yes'
    
    # Main game loop
    while play_again.lower() in ['yes', 'y']:
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)
        
        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        # Display the result of the round
        display_result(user_choice, computer_choice, winner)
        
        # Display the current scores
        print(f"\nScores -> You: {user_score}, Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ")
    
    # Goodbye message
    print("\nThanks for playing!")

# Entry point of the script
if __name__ == "__main__":
    main()
