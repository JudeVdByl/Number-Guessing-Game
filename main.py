import art
import random



def start_round():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty in ['easy','e']:
        game_lives = 10
        num = -1
        random_number = random.randint(1, 100)
        while game_lives != 0 and num != random_number:
            print("\n")
            num = int(input("Make a guess: "))
            if num < random_number:
                game_lives -= 1
                print(f"Too low, you have {game_lives} lives left")
                if game_lives != 0:
                    print(f"Guess again")
            elif num > random_number:
                game_lives -= 1
                print(f"Too High, you have {game_lives} lives left")
                if game_lives != 0:
                    print(f"Guess again")

        if num == random_number:
            print(f"YOU WIN!")
        else:
            print(f"\nThe number was {random_number}")
            print(f"YOU LOSE!")


    elif difficulty in ['hard','h']:
        game_lives = 5
        num = -1
        random_number = random.randint(1, 100)
        while game_lives != 0 and num != random_number:
            print("\n")
            num = int(input("Make a guess: "))
            if num < random_number:
                game_lives -= 1
                print(f"Too low, you have {game_lives} lives left")
                if game_lives != 0:
                    print(f"Guess again")
            elif num > random_number:
                game_lives -= 1
                print(f"Too High, you have {game_lives} lives left")
                if game_lives != 0:
                    print(f"Guess again")

        if num == random_number:
            print(f"YOU WIN!")
        else:
            print(f"\nThe number was {random_number}")
            print(f"YOU LOSE!")




go_again = True
go_again_check = ''
while go_again == True:
    print('\n' * 100)
    print(art.logo)
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100")
    start_round()
    go_again_check = input('\nWould you like to play again?').lower()
    if go_again_check not in ['y','yes']:
        go_again = False

print("\nGame Over! Thanks for Playing")


