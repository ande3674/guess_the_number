# ande3674 issue: count the number of guesses
import random

correct = 'you guessed correctly!'
too_low = 'Too Low!!!'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''

    while True:
        try:
            guess = int(input('Guess the secret number? '))
        except ValueError:
            print("Please enter an integer")
        else:
            break

    return guess


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    count = 0

    while True:
        guess = get_guess()
        count += 1
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            print('Guessed in ', count, ' guesses')
            play_again = int(input('press 1 to play again, any other number to quit'))

            if play_again == 1:
                count = 0
                continue
            else:
                break


if __name__ == '__main__':
    main()