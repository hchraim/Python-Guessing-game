word = "elephant" # Secret word variable
guess = "" # guess variable blank for user input
guess_count = 0 # keeps track of how many times the user guesses, starts at 0
guess_limit = 3 # max amount of guesses
out_of_guesses = False 




print("Hello there and welcome to my guessing game!")
print("You will need to guess the correct word in 3 or less tries otherwise you will lose")
print(input("are you ready? ")) # Intro
 
print("Cool! The word I am currently thinking of is a VERY BIG ANIMAL!")
while guess != word and not (out_of_guesses): # run this section of code as long as hes yet to get the right word and still has guesses
    if guess_count < guess_limit: # checking if guess count is less than the limit so it can keep looping
        guess = input("Enter a guess: ")
        guess_count += 1 # add 1 attempt
    else: # otherwise they will have no more guesses
        out_of_guesses = True
        
if out_of_guesses:
    print("Out of guesses, you lose :(")
else:
    print("Yay you win!")