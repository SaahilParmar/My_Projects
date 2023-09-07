import random
characters = ('snake', 'gun', 'water')
user_score = 0
computer_score = 0
games = 4

print(f'THIS IS SNAKE-WATER-GUN.\n=> SNAKE BEATS WATER.\n=> WATER BEATS GUN.\n'
      f'=> GUN BEATS SNAKE.\n-----------------------')

while games != 0:
    print(F'TYPE SNAKE, WATER OR GUN.                                                      [YOUR LIVES LEFT: {games}]')

    while True:
        user = input('YOUR CHOICE: ').lower()
        if user not in characters:
            print('ONLY SNAKE, WATER OR GUN IN ALLOWED.')
        else:
            break

    choice = random.choice(characters)

    if choice == 'snake':
        print('COMPUTER CHOSE: 🐍\n')
    elif choice == 'gun':
        print('COMPUTER CHOSE: 🔫\n')
    else:
        print('COMPUTER CHOSE: 💧\n')

    if user or choice == 'snake' or user and choice == 'snake':

        if user == 'snake' and choice == 'gun':
            computer_score += 1
            print(f'Your 🐍 got shot by 🔫. YOU LOSE.    [YOUR SCORE:{user_score}.COMPUTER SCORE:{computer_score}]\n')
        elif choice == 'snake' and user == 'gun':
            user_score += 1
            print(f'Your 🔫 shot the 🐍. YOU WIN.    [YOUR SCORE:{user_score}.COMPUTER SCORE:{computer_score}]\n')
        elif user == 'snake' and choice == 'water':
            user_score += 1
            print(f'Your 🐍 drank the 💧. YOU WIN.    [YOUR SCORE:{user_score}.COMPUTER SCORE:{computer_score}]\n')
        elif choice == 'snake' and user == 'water':
            computer_score += 1
            print(f'🐍 drank your 💧. YOU LOSE.    [YOUR SCORE:{user_score}.COMPUTER SCORE:{computer_score}]\n')

    if user or choice == 'water' or user and choice == 'water':

        if user == 'water' and choice == 'gun':
            user_score += 1
            print(f'Your 💧 drowned the 🔫. You WIN.    [YOUR SCORE:{user_score}.COMPUTER SCORE:{computer_score}]\n')
        elif choice == 'water' and user == 'gun':
            computer_score += 1
            print(f'Your 🔫 drowned in the 💧. You LOSE.    [YOUR SCORE:{user_score}.COMPUTER SCORE:{computer_score}]\n')

    if user == choice:

        if user and choice == 'snake':
            print(f'🐍=🐍. It\'s a draw.    [YOUR SCORE:{user_score}.COMPUTER SCORE:{computer_score}]\n')
        elif user and choice == 'water':
            print(f'💧=💧. It\'s a draw.    [YOUR SCORE:{user_score}.COMPUTER SCORE:{computer_score}]\n')
        else:
            print(f'🔫=🔫. It\'s a draw.    [YOUR SCORE:{user_score}.COMPUTER SCORE:{computer_score}]\n')

    games -= 1

while games == 0:

    if user_score > computer_score:
        print('✨✨YOU ARE THE WINNER✨✨')
        break
    else:
        print('YOU LOSE. BETTER LUCK NEXT TIME.🙁🙁')
        break

# CORNER CASES HAVE BEEN RESOLVED.
