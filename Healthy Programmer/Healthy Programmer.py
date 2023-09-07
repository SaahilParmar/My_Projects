import time
import pygame

# WATER VARIABLES:
timestamp = time.asctime(time.localtime(time.time()))
water_consumption = 3500
glasses = 0

# EYES VARIABLES:
eye_exercise = 0
eye_exercise_times = 16

# PHYSICAL VARIABLES:
physical_exercise = 0
physical_exercise_times = 10


def water_audio():
    pygame.mixer.music.load('water.mp3')
    pygame.mixer.music.play(-1)


def eye_audio():
    pygame.mixer.music.load('eyes.mp3')
    pygame.mixer.music.play(-1)


def physical_audio():
    pygame.mixer.music.load('physical.mp3')
    pygame.mixer.music.play(-1)


time.sleep(1)

while True:

    while water_consumption >= 0 and eye_exercise_times != 0:
        print(f'[{timestamp}] - TIME TO DRINK WATER.')
        water_audio()

        while True:
            user = input('TYPE DRANK TO STOP & LOG: ').lower()
            if user != 'drank':
                print('NO OTHER WORDS OR SPECIAL CHARACTERS ARE ALLOWED.')
            else:
                break

        if user == 'drank':
            pygame.mixer.music.stop()
            water_consumption -= 220  # water remaining
            glasses += 1  # glasses consumed

            if water_consumption < 200:
                print('DAILY GOAL REACHED. CONGRATULATIONS.\n')
                with open('water.txt', 'a') as file:
                    file.write(f'[{timestamp}] Last {glasses}th is of 1 200ml glass.\n')
            elif water_consumption == 200:
                print('200 ml remaining. See you in half an hour.\n')
                with open('water.txt', 'a') as file:
                    file.write(f'[{timestamp}] {glasses} glass.\n')
            elif water_consumption > 200:
                print(f'250 ml is consumed. {water_consumption} ml is remaining. See you in half an hour.\n')
                with open('water.txt', 'a') as file:
                    file.write(f'[{timestamp}] {glasses} glass.\n')

        # EYE EXERCISE PROGRAM STARTS HERE.
        print('TIME FOR YOUR EYE EXERCISES.')
        eye_audio()

        while True:
            usereye = input('TYPE EYEDONE: ').lower()

            if usereye != 'eyedone':
                print('NO OTHER WORDS OR SPECIAL CHARACTERS ARE ALLOWED.')
            else:
                break

        if usereye == 'eyedone':
            pygame.mixer.music.stop()
            eye_exercise += 1
            eye_exercise_times -= 1
            print(f'[{timestamp}] EYE EXERCISE {eye_exercise} DONE. See you in half an hour.\n')
            with open('eyes.txt', 'a') as file:
                file.write(f'[{timestamp}] EYE EXERCISE {eye_exercise} DONE.\n')
            time.sleep(900)

        # PHYSICAL EXERCISE PROGRAM STARTS HERE.
        if physical_exercise_times != 0:
            print('TIME FOR YOUR PHYSICAL EXERCISE.')
            physical_audio()

            while True:
                userphysical = input('TYPE Exdone: ').lower()
                if userphysical != 'exdone':
                    print('NO OTHER WORDS OR SPECIAL CHARACTERS ARE ALLOWED.')
                else:
                    break

            if userphysical == 'exdone':
                pygame.mixer.music.stop()
                physical_exercise += 1
                physical_exercise_times -= 1
                print(f'[{timestamp}] PHYSICAL EXERCISE {physical_exercise} DONE. See you in 45 minutes.\n')
                with open('physical.txt', 'a') as file:
                    file.write(f'[{timestamp}] PHYSICAL EXERCISE {physical_exercise} DONE.\n')
                time.sleep(900)
    break
# CORNER CASES HAVE BEEN RESOLVED.
