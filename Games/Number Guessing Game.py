num = 27
guesses = 6
print(f'This is a number guessing game.                                              [Guesses:{guesses}]')
while guesses != 0:
    while True:
        try:
            user = int(input('Try to guess the number:  '))
            break
        except ValueError:
            print('Letters or Special characters are not allowed.')
    if user < num:
        print(f'Your number is small. Try higher.                                            [Guesses:{guesses - 1}]')
    elif user > num:
        print(f'Your number is high. Try smaller.                                            [Guesses:{guesses - 1}]')
    elif user == num:
        print('Correct Answer')
        break
    guesses -= 1
print('GAME OVER.')

# CORNER CASES HAVE BEEN RESOLVED.
