import random
import math

lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

# generating random number between the lower and upper
x = random.randint(lower, upper)
print("\n\You've only ",
      round(math.log(upper - lower +1, 2)),
      " chances to guess the integer!\n")

# Initialising the number of guesses.
count = 0

# for calculating of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("Guess a number:- "))

    if x == guess:
        print("Congratulations you did it!! ",
              count, " try")
        # once guessed, loop will break

        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too large!")

# If Guessing is more than required guesses,
# shows this output.
        if count >= math.log(upper - lower + 1, 2):
            print("\nThe number is %d" % x)
            print("\tBetter luck Next time!")            
