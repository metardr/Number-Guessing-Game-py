# First import random module
import random

# Main function
def play_game():
    number = random.randint(1, 100) #Range for the game using the .randint from random
    attempts = 0 #Count the attempts - variable
    
    print("I'm thinking of a number between 1 and 100.")
    # while loop including if, elif, else statment
    while True: 
        try:
            guess = int(input("Your guess: ")) #User guess input
            attempts += 1 #Count the attempts
            
            if guess < number:
                print("Higher!")
            elif guess > number:
                print("Lower!")
            else:
                print(f"Correct! You won in {attempts} attempts!") #Using f string to diaplay number of attempts
                break
                
        except ValueError: #Handle non valid input
            print("Please enter a valid number.")


#Prompt user to play again or say thanks for playing if user choses to leave
#Use __name__ = "__main__"

if __name__ == "__main__":
    while True:
        play_game()
        if input("\nPlay again? (y/n): ").lower() != 'y':
            break
    print("Thanks for playing!")