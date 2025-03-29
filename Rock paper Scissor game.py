import random

# Print game rules
print("Winning rules of the game ROCK PAPER SCISSORS are:\n"
      "Rock vs Paper -> Paper wins\n"
      "Rock vs Scissors -> Rock wins\n"
      "Paper vs Scissors -> Scissors wins\n")

while True:
    print("Enter your choice: \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # Take input from user
    choice = int(input("Enter your choice: "))

    # Loop until user enters a valid input
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice (1, 2, or 3): "))

    # Assign choice name
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # Print user choice
    print(f"User choice is: {choice_name}")
    print("Now it's Computer's Turn...")

    # Computer chooses randomly
    comp_choice = random.randint(1, 3)

    # Assign computer choice name
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print(f"Computer choice is: {comp_choice_name}")
    print(f"{choice_name} vs {comp_choice_name}")

    # Determine the winner
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2):  
        result = 'Paper'  # Rock vs Paper -> Paper wins
    elif (choice == 1 and comp_choice == 3):  
        result = 'Rock'   # Rock vs Scissors -> Rock wins
    elif (choice == 2 and comp_choice == 1):  
        result = 'Paper'  # Paper vs Rock -> Paper wins
    elif (choice == 2 and comp_choice == 3):  
        result = 'Scissors'  # Paper vs Scissors -> Scissors wins
    elif (choice == 3 and comp_choice == 1):  
        result = 'Rock'   # Scissors vs Rock -> Rock wins
    elif (choice == 3 and comp_choice == 2):  
        result = 'Scissors'  # Scissors vs Paper -> Scissors wins

    # Print the result
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == choice_name:
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    # Ask if the user wants to play again
    ans = input("Do you want to play again? (Y/N): ").lower()
    if ans == 'n':
        print("Thanks for playing!")
        break
