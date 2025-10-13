import random

def game():
    RPS = ["rock", "paper", "scissors"]

    guess = random.choice(RPS).lower()
    choice = input("What do you choose (rock, paper, scissors): ").lower()

    print(f"You: {choice}, Computer: {guess}")

    def RPSlogic():
        if guess == choice:
            return "It's a tie!"
        elif (guess == "rock" and choice == "scissors") or (guess == "paper" and choice == "rock") or (guess == "scissors" and choice == "paper"):
            return "You lose!"
        else:
            return "You win!"

    result = RPSlogic()
    print(result)


while True:
    game()
    play_again = input("Do you want to play again? (y or n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Bye.")
        break
    else:
        game()

