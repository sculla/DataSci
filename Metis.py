def guess_game():
    """
    Initiate guess game, user is asked to guess a random number between 0 and 100.
    User receives 10 guesses, and upon completion gets fabulous prize!
    :return: N/A
    """
    # import random number tool & exit
    import random
    from sys import exit

    # initialize variables and generate secret_number
    num_guess = 1
    user_guess = 0
    secret_number = random.randint(0, 100)

    print("You have 10 tries to guess a number between 0, and 100:")
    # While guess is less than or equal 10 ask for user input
    while num_guess <= 10:
    # what are you guessing??
        while True:
            try:
                user_guess = int(input("Guess #{}, What number would you like to guess? ".format(num_guess)))
                break
            except ValueError:
                print("\nPlease enter only an Integer.\n")

        if num_check(user_guess, secret_number):
            exit()
        num_guess += 1

    # you fail... sorry
    print("I'm sorry, you didn\'t get it correct. The answer was {}.".format(secret_number))
    exit()


def num_check(user: int, secret: int):
    
    """
    Returns a boolean of the comparison of the user input guess to the secret number chosen.
    :param user: Integer of guessed number as returned by input
    :param secret: Integer of random number that was generated
    :return: Boolean check if user is correct
    """
    # Greater?
    if user > secret:
        print("Your guess was: {}.\nThat is too high, please try again!\n".format(user))
        return False
    # Lesser?
    elif user < secret:
        print("Your guess was: {}.\nThat is too low, please try again!\n".format(user))
        return False
    # All other.... means ==
    elif user == secret:
        print("You've guessed right!\nThe \"Super Secret Number\" was {}".format(secret))
        return True

guess_game()