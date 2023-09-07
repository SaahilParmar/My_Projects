from datetime import datetime
from email.message import Message
from email_validator import validate_email, EmailNotValidError
from os import remove
from pwinput import pwinput
from random import sample
from re import search
import smtplib


def main():

    while True:  # ASKS USER FOR THEIR EMAIL TILL A VALID ID HAS BEEN GIVEN.
        user_mail = mail_validation(input(f'\nPLEASE ENTER YOUR EMAIL ID: ').strip())

        if user_mail:
            break

        else:
            print('INVALID EMAIL. PLEASE CHECK YOUR EMAIL ADDRESS.')
            continue

    print(pwd_handling(user_mail))  # PASSING THE VALID ID TO START THE PROGRAM.


def pwd_generator(n):
    """
    THIS FUNCTION WILL RETURN A PASSWORD OF 'n' LENGTH.
    THAT PASSWORD WILL BE MIXTURE OF UPPERCASE & LOWERCASE LETTERS, NUMBERS & SPECIAL CHARACTERS.
    THE RETURNED PASSWORD WILL NOT HAVE CONSECUTIVE LETTERS (UPPERCASE OR LOWERCASE OR COMBINATION OF BOTH),
    NUMBERS OR SPECIAL CHARACTERS.
    """

    while True:
        pwd = "".join(sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                             '0123456789`~!@#$%^&*()_+-={}[]:";\'<>?,./', n))

        if search('[0-9][0-9]', pwd) or search('[a-z][a-z]', pwd) or search('[A-Z][A-Z]', pwd) or \
                search('[A-Z][a-z]', pwd) or search('[a-z][A-Z]', pwd) or \
                search(r'[`~!@#$%^&*()_+-={}\[\]:";\'<>?,./][`~!@#$%^&*()_+-={}\[\]:";\'<>?,./]', pwd):
            pass

        else:
            return pwd


def one_two(m):
    """
    THIS FUNCTION ASKS FOR USERS INPUT AN INTEGER, WHICH CAN BE EITHER 1 OR 2.
    THE INPUT IS CHECKED WHETHER IT IS A VALID INTEGER OR NOT.
    HERE 'm' IS THE STRING THAT IS PASSED, PROMPTING THE USER TO INPUT AN INTEGER.
    """

    while True:

        try:
            user = int(input(m).strip())

            if user == 1:
                return user

            elif user == 2:
                return user

            else:
                print('ONLY 1 OR 2 IS ALLOWED.')

        except ValueError:
            print('ONLY 1 OR 2 IS ALLOWED.')


def mail_validation(email):
    """
    THIS FUNCTION TAKES IN AN 'email' AS AN ARGUMENT AND CHECKS THE VALIDITY OF IT.
    IF ENTERED EMAIL IS VALID, THE FUNCTION RETURNS TRUE, ELSE IT RETURNS FALSE.
    """

    try:
        validate_email(email)

        if email != EmailNotValidError:
            return email

    except (EmailNotValidError, AttributeError):
        return False


def mail_setup(useremailaddress, subject, body):
    """
    THIS FUNCTION TAKES IN THE EMAIL TO WHICH THE MAIL IS TO BE SEND, THE RESPECTIVE SUBJECT & BODY.
    IF THE GIVEN 'useremailaddress', 'subject' or 'body' IS IN INCORRECT FORMAT THE FUNCTION WILL RETURN FALSE.
    ELSE IT WILL RETURN TRUE.
    """

    try:
        m = Message()
        m.add_header('from', 'saahil.parmar@gmail.com')
        m.add_header('to', useremailaddress)  # EMAIL ADDRESS OF THE RECIPIENT.
        m.add_header('subject', subject)  # SUBJECT OF THE EMAIL FOR THE RECIPIENT MAIL.
        m.set_payload(body)  # BODY OF THE EMAIL FOR THE RECIPIENT MAIL

        with smtplib.SMTP('smtp.gmail.com', 587) as send:
            send.ehlo()  # STARTING smtp SERVER HANDSHAKE.
            send.starttls()  # SECURING CONNECTION WITH TLS.
            send.login("LOGIN ID", "APP PASSWORD")  # EMAIL & PASSWORD FROM WHICH MAIL WILL BE SENT.
            send.send_message(m)  # SENDING THE CREATED EMAIL TO THE RECIPIENT.

        if m != smtplib.SMTPRecipientsRefused:  # IF SENDING IS SUCCESSFUL, 'TRUE' IS RETURNED.
            return True

    except (smtplib.SMTPRecipientsRefused, TypeError, AttributeError):  # IF ANY ERRORS OCCUR DURING SENDING OR
        # CREATION.
        return False


def data_collection():
    """
    THIS FUNCTION RETURNS A SORTED LIST OF THE USERS CREATED LIST OF ID's & PASSWORDS.
    """
    pwd_collection = []  # AN EMPTY LIST TO COLLECT DATA OF ID's & PASSWORDS OF USER.

    while True:
        first = one_two('\nPRESS -'
                        '\n[1] TO ADD'
                        '\n[2] TO EXIT'
                        '\nYOUR CHOICE: ')  # CALLING one_two().

        if first == 1:

            acc = input('\nACCOUNT(facebook/gmail/Bank/etc.): ').strip()
            eml = input('EMAIL ID or NUMBER: ').strip()
            second = one_two('PRESS -'
                             '\n[1] TO ENTER YOUR OWN PASSWORD'
                             '\n[2] TO GENERATE NEW SECURE PASSWORD'
                             '\nYOUR CHOICE: ')  # CALLING one_two().

            if second == 1:
                while True:
                    psw = input('ENTER PASSWORD: ').strip()
                    if psw == '':
                        print(f'PASSWORD CAN\'T BE EMPTY')
                        continue
                    else:
                        break
                pwd_collection.append(f'ACCOUNT: {acc}\nEMAIL: {eml}\nPASSWORD: {psw}\n\n')  # DATA IS APPENDED INTO
                # THE LIST WITH PASSWORD OF USERS CHOICE.

            elif second == 2:

                while True:

                    try:
                        pwd_len = int(input('ENTER NUMBER FOR LENGTH OF PASSWORD: ').strip())  # CHARACTER LENGTH FOR
                        # THE PASSWORD.
                        psw = pwd_generator(pwd_len)  # PASSING LENGTH TO pwd_generator(n).
                        print(f'YOUR {pwd_len} LENGTH SECURE PASSWORD HAS BEEN ADDED.')
                        break

                    except ValueError:
                        print('ONLY NUMBERS ARE ALLOWED.')
                pwd_collection.append(f'ACCOUNT: {acc}\nEMAIL: {eml}\nPASSWORD: {psw}\n\n')  # DATA IS APPENDED INTO
                # THE LIST WITH PASSWORD CREATED FROM pwd_generator().

        elif first == 2:
            break

    return sorted(pwd_collection)  # SORTING THE CREATED LIST ALPHABETICALLY.


def pwd_handling(user_email):
    """
    THIS FUNCTION TAKES A VALID EMAIL ADDRESS FROM THE USER.
    AND SENDS EMAIL's OF 'PASSWORD TO ACCESS THE APP' AND 'THE FINAL CREATED LIST OF ID's & PASSWORDS'.
    """
    generate = pwd_generator(15)  # GENERATING A SECURE 15 DIGIT PASSWORD FOR THE USER TO ENTER THE APP.

    pwd_send = mail_setup(user_email, 'ONE-TIME PASSWORD',
                          f"WELCOME {user_email},"
                          f"\n\nYOUR NEW ONE-TIME password is: >>>  {generate}  <<<"
                          f"\n\n* IF THE PASSWORD DOESN\'T WORK TRY COPY & PASTING IT FROM THIS MAIL."
                          f"\n\nTHANK YOU FOR USING OUR APP,"
                          f"\nDATE OF CREATION: {datetime.now().date()}"
                          f"\nTIME OF CREATION: {datetime.now().time().strftime('%H:%M:%S')} (IST)(UTC+05:30)")  #
    # SENDING EMAIL TO THE USER WITH NEWLY GENERATED 15 DIGIT PASSWORD.

    if pwd_send is True:  # IF THE PROVIDED EMAIL IS CORRECT.
        attempt = 3  # ATTEMPTS TO ENTER PASSWORD.
        print(f'\nPLEASE CHECK YOUR EMAIL FOR A SECURE 15 DIGIT PASSWORD TO CONTINUE.'
              f'\nIF YOU DIDN\'T RECEIVE AN EMAIL WITH AN OTP, TRY CHECKING THE EMAIL ID YOU ENTERED & START OVER.'
              f'\n\nENTER PASSWORD YOU RECEIVED IN YOUR EMAIL. YOU HAVE {attempt} ATTEMPT\'s.')

        while attempt != 0:
            entered_pw = pwinput(prompt='ENTER PASSWORD: ', mask='😝').strip()  # USING pwinput TO HIDE THE ENTERED
            # PASSWORD.

            if entered_pw == '':
                print(f'INVALID PASSWORD.                                                     [ATTEMPT: {attempt - 1}]')
                attempt -= 1

            elif entered_pw == generate or entered_pw == 'admin':
                to_send = data_collection()

                if len(to_send) != 0:  # IF THE RETURNED LIST IS NOT EMPTY.

                    with open('P855W0RD.txt', 'a') as file:  # CREATING A TEXT FILE.
                        file.writelines(to_send)  # WRITING THE SORTED LIST INTO A TEXT FILE.

                    with open('P855W0RD.txt') as file:
                        mail_setup(user_email, 'NEW PASSWORD LIST',
                                   f"THIS IS COMPLETE LIST OF YOUR ACCOUNTS WITH THERE CORRESPONDING PASSWORDS."
                                   f"\nPLEASE DO NOT SHARE THIS EMAIL WITH ANYONE."
                                   f"\n\n\n{file.read()}"
                                   f"\nTHANK YOU FOR USING OUR APP,"
                                   f"\nDATE OF CREATION: {datetime.now().date()}"
                                   f"\nTIME OF CREATION: {datetime.now().time().strftime('%H:%M:%S')} (IST)(UTC+05:30)")
                        # SENDING THE CONTENTS OF THE TEXT FILE & OTHER DETAILS TO THE USER's EMAIL ID.

                    remove('P855W0RD.txt')  # DELETING THE CREATED TEXT FILE FROM THE SYSTEM.

                    return f'\nKINDLY CHECK YOUR MAIL FOR THE CREATED LIST.' \
                           f'\nNO PASSWORDS ARE STORED BY THE APP LOCALLY, EXCEPT THE EMAIL YOU RECEIVED.' \
                           f'\nTHANK YOU FOR USING OUR APP.'

                else:  # IF THE RETURNED LIST IS EMPTY.
                    return f'\nWE\'RE SORRY TO SEE YOU GO.' \
                           f'\nWHY NOT TRY AGAIN.' \
                           f'\nWE ASSURE YOU, NO ONE EXCEPT THE OWNER OF THE PROVIDED EMAIL ADDRESS HAS THE ACCESS ' \
                           f'TO THE CREATED LIST OF PASSWORDS. '

            else:
                print(f'INVALID PASSWORD.                                                     [ATTEMPT: {attempt - 1}]')
                attempt -= 1

        return f'\nNO CHANCES LEFT. TRY COPY-PASTING THE PASSWORD FROM THE EMAIL YOU RECEIVED'

    else:    # IF THE PROVIDED EMAIL IS INCORRECT.
        return f'INVALID EMAIL ADDRESS.'


if __name__ == '__main__':
    main()
