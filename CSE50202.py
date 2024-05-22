import random

def get_guess():
  """
  This function gets a valid guess from the user within a specific range.
  """
  while True:
    try:
      guess = int(input("Guess a number between 1 and {upper_bound}: "))
      if 1 <= guess <= upper_bound:
        return guess
      else:
        print(f"Invalid guess. Please enter a number between 1 and {upper_bound}.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def give_hint(guess, secret_number):
  """
  This function provides a hint to the user based on their guess.
  """
  difference = abs(guess - secret_number)
  if difference <= 5:
    print("You're very close!")
  elif difference <= 10:
    print("Getting warmer!")
  else:
    if guess < secret_number:
      print("Too low. Guess higher.")
    else:
      print("Too high. Guess lower.")

def play_game():
  """
  This function controls the main game loop.
  """
  global upper_bound  # Access the global variable
  secret_number = random.randint(1, upper_bound)
  guesses = 0

  print("Welcome to the Number Guessing Game!")

  while True:
    guess = get_guess()
    guesses += 1

    if guess == secret_number:
      print(f"Congratulations! You guessed the number in {guesses} attempts.")
      break
    else:
      give_hint(guess, secret_number)

if __name__ == "__main__":
  # Set the upper bound for the guessing range
  upper_bound = 100

  while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
      break
