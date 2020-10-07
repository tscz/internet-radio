from gpiozero import Button
from signal import pause
import os


def shutdown():
    print("Shutdown Raspberry Pi")
    os.system("shutdown -h now")

button = Button(3)

button.when_pressed = shutdown

pause()