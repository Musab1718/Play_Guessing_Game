import random

def play_guessing_game(low=1, high=100, close_threshold=5, max_attempts=7):
    random_num = random.randint(low, high)
    attempts = 0
    print(f"Guess a number between {low} and {high}! You have {max_attempts} attempts.")

    while attempts < max_attempts:
        user_input = input(f"Attempt {attempts + 1}/{max_attempts} - Enter number: ")
        
        try:
            guessing_num = int(user_input)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        # Check for win
        if guessing_num == random_num:
            print(f"Yes, you got it! It's {guessing_num}.")
            print(f"You solved it in {attempts} attempt{'s' if attempts > 1 else ''}!")
            return True

        # Check if attempts ran out
        if attempts >= max_attempts:
            print(f"\nGame over! You ran out of attempts. The number was {random_num}.")
            return False

        # Proximity and directional hints
        remaining = max_attempts - attempts
        if guessing_num > random_num:
            if guessing_num - random_num <= close_threshold:
                print(f"You're very close! Go down a little. ({remaining} left)")
            else:
                print(f"{guessing_num} is too high. ({remaining} left)")
        else:
            if random_num - guessing_num <= close_threshold:
                print(f"You're very close! Go up a little. ({remaining} left)")
            else:
                print(f"{guessing_num} is too low. ({remaining} left)")

if __name__ == "__main__":
    play_guessing_game()