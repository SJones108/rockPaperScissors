import random

actions = ["R", "P", "S"]

while True:
    # Computer chooses its action randomly
    computer_action = random.choice(actions)

    # Ask the player for their action
    player_action = input("Choose R, P, or S (or 'quit' to end the game): ")

    if player_action == "quit":
        # End the game if the player chooses to quit
        print("Thank you for playing")
        break
    elif player_action not in actions:
        # Prompt the player to choose a valid action
        print("Invalid action. Please choose R, P, or S.")
        continue

    print(f"You chose {player_action}. The computer chose {computer_action}.")

    # Determine the winner of the game
    if player_action == computer_action:
        print("Game tied")
    elif (player_action == "R" and computer_action == "P") \
        or (player_action == "S" and computer_action == "R") \
        or (player_action == "P" and computer_action == "S"):
        print("You lose")
    else:
        print("You win")