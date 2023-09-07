def one_word_input(input_message, password, error_message):
    """RETURNS A SINGLE WORD STRING INPUT WITHOUT ANY ERRORS."""
    while True:
        user_input = input(input_message).lower()
        if user_input == password:
            return user_input
        else:
            print(error_message)


def one_integer_input(input_message, password, incorrect_integer_message, error_message):
    """RETURNS AN INTEGER INPUT WITHOUT ANY ERRORS."""
    while True:
        try:
            user_input = int(input(input_message))
            if user_input == password:
                return user_input
            else:
                print(incorrect_integer_message)
        except ValueError:
            print(error_message)
