import random

# write 'hello world' to the console
# print('hello world')

# The player can choose rock, paper, or scissors, and invalid inputs are handled gracefully. After each round, display whether the player won, lost, or tied. Allow the player to play again after each round and display their score at the end of the game. Inputs are converted to lowercase for consistency.
def play_game():
    choices = ['rock', 'paper', 'scissors']
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice not in choices:
            print("Invalid input. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)

        print(f"Player chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("Player wins!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

play_game()
