# TO CHECK WHETHER THE USER IS ELIGIBLE FOR A LICENSE, ETC.

while True:
    try:
        age = int(input('AGE? '))
        if age == 0:
            print('0 IS NOT A VALID AGE. ENTER A VALID AGE.')
        else:
            break
    except ValueError:
        print('ONLY NUMBERS ARE ALLOWED.')

if 18 <= age <= 100:
    print('OK')
else:
    print('NOT OK.')

# CORNER CASES HAVE BEEN RESOLVED.
