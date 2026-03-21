# import time
# import datetime
# import pygame
#
# def set_alarm(alarm_time):
#     pygame.mixer.init()
#     sound_file = "my_music.mp3"
#
#     now = datetime.datetime.now()
#     alarm = datetime.datetime.strptime(alarm_time, "%H:%M:%S").replace(
#         year=now.year, month=now.month, day=now.day
#     )
#
#     # If time already passed, set for next day
#     if alarm <= now:
#         alarm += datetime.timedelta(days=1)
#
#     print(f"⏰ Alarm set for {alarm}")
#
#     while True:
#         if datetime.datetime.now() >= alarm:
#             print("🔔 Wake Up!")
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play()
#
#             while pygame.mixer.music.get_busy():
#                 time.sleep(1)
#             break
#
#         time.sleep(1)
#
# if __name__ == "__main__":
#     alarm_time = input("Enter alarm time (HH:MM:SS): ")
#     set_alarm(alarm_time)



# TEST

import time
import pygame

def set_alarm(seconds):
    print(f"⏰ Alarm will ring in {seconds} seconds")
    time.sleep(seconds)

    pygame.mixer.init()
    pygame.mixer.music.load("my_music.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

if __name__ == "__main__":
    seconds = int(input("Enter seconds: "))
    set_alarm(seconds)

