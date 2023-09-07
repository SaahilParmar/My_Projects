def track_clients():
    """OPTIONS TO CHOOSE BETWEEN DIET OR WORKOUT. WITH CORNER CASES SOLVED."""
    while True:
        try:
            track = int(input('PRESS 1 FOR DIET OR 2 FOR WORKOUT: '))
            if track > 2 or track <= 0:
                print('ONLY 1 OR 2 IS ALLOWED.')
            else:
                break
        except ValueError:
            print('NO ALPHABETS OR SPECIAL CHARACTERS ARE ALLOWED.')

    if track == 1:
        diet()
    else:
        workout()


def client_choice():
    """OPTIONS TO CHOOSE BETWEEN CLIENTS. WITH CORNER CASES SOLVED."""
    while True:
        try:
            client = int(input('Press 1 for Aamir, 2 for Salman, 3 for Shahrukh: '))
            if client > 3 or client == 0:
                print('ONLY THE GIVEN NUMBERS ARE ALLOWED.')
            else:
                return client
        except ValueError:
            print('NO ALPHABETS OR SPECIAL CHARACTERS ALLOWED.')


def choice_file_read_write(client_name, diet_or_workout):
    """OPTIONS TO CHOOSE WHETHER TO READ OR WRITE A FILE. WITH CORNER CASES SOLVED."""
    while True:
        try:
            choice = int(input(f'PRESS 1 TO READ {client_name}\'s {diet_or_workout} OR 2 TO WRITE: '))
            if choice > 2 or choice == 0:
                print('ONLY THE GIVEN NUMBERS ARE ALLOWED.')
            else:
                return choice
        except ValueError:
            print('NO ALPHABETS OR SPECIAL CHARACTERS ALLOWED.')


def read_file(file_name):
    """FUNCTION TO READ A SPECIFIC FILE."""
    with open(file_name) as file:
        print(file.read())


def write_file(file_name, file_attribute):
    """FUNCTION TO WRITE IN A SPECIFIC FILE WITH THE PREFERRED ATTRIBUTE WITH A TIME STAMP."""
    import time
    timestamp = time.asctime(time.localtime(time.time()))
    with open(file_name, file_attribute) as file:
        file.write(f'[{timestamp}]: {input("TYPE: ")}\n')


def diet():
    client = client_choice()
    
    if client == 1:
        choice = choice_file_read_write('Aamir', 'Diet')
        if choice == 1:
            read_file('Aamir Diet.txt')
        else:
            write_file('Aamir Diet.txt', 'a')

    elif client == 2:
        choice = choice_file_read_write('Salman', 'Diet')
        if choice == 1:
            read_file('Salman Diet.txt')
        else:
            write_file('Salman Diet.txt', 'a')

    else:
        choice = choice_file_read_write('Shahrukh', 'Diet')
        if choice == 1:
            read_file('Shahrukh Diet.txt')
        else:
            write_file('Shahrukh Diet.txt', 'a')


def workout():
    client = client_choice()

    if client == 1:
        choice = choice_file_read_write('Aamir', 'Workout')
        if choice == 1:
            read_file('Aamir Workout.txt')
        else:
            write_file('Aamir Workout.txt', 'a')

    elif client == 2:
        choice = choice_file_read_write('Salman', 'Workout')
        if choice == 1:
            read_file('Salman Workout.txt')
        else:
            write_file('Salman Workout.txt', 'a')

    else:
        choice = choice_file_read_write('Shahrukh', 'Workout')
        if choice == 1:
            read_file('Shahrukh Workout.txt')
        else:
            write_file('Shahrukh Workout.txt', 'a')


if __name__ == '__main__':
    track_clients()

# CORNER CASES HAVE BEEN RESOLVED.
