# Exercise 7: Healthy Programmer
"""
This program will make you healthy programmer.
Programme will remind you to drink water, do eye exercise, and do physical activity.
Assume working_hour = 8 hours # 9am - 5pm
"""

from pygame import mixer
from datetime import datetime
from time import time


def playmusic(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(1)
    mixer.music.play()
    while True:
        input_from_user = input().lower()
        if stopper == input_from_user:
            mixer.music.stop()
            break


def filelog(msg):
    with open("log.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    working_start = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 9)
    working_end = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 18)
    if working_start < datetime.now() < working_end:
        water_init = time()
        eye_init = time()
        exercise_init = time()
        water_sec = 30 * 60  # 30 Minutes
        eye_sec = 45 * 60  # 45 Minutes
        exercise_sec = 60 * 60  # 1 Hours

        while True:
            if time() - water_init > water_sec:
                print("Time To Drank Water.For stop alarm enter 'Drank'")
                playmusic("Love You Oye.mp3", "drank")
                filelog("Drink water at")
                water_init = time()
            if time() - eye_init > eye_sec:
                print("Time To Rest Eyes.For stop alarm enter 'EyeDone'")
                playmusic("Love You Oye.mp3", "eyedone")
                filelog("Rest Eyes at")
                eye_init = time()
            if time() - exercise_init > exercise_sec:
                print("Time To Exercise.For stop alarm enter 'ExDone'")
                playmusic("Love You Oye.mp3", "exdone")
                filelog("Exercise Done at")
                exercise_init = time()
    else:
        print("Not Working Hour!!")
