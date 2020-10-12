#!/usr/bin/env python3

import os
import subprocess
from gpiozero import Button
from signal import pause
from google_speech import Speech

class Player:
    def __init__(self):
        os.system("mpc stop")

        os.system("mpc clear")
        os.system("mpc load https://www.radioeins.de/live.m3u")
        os.system("mpc load http://streams.fluxfm.de/live/mp3-320/audio/play.m3u")
        os.system("mpc add http://hr-hr1-live.cast.addradio.de/hr/hr1/live/mp3/128/stream.mp3")
        os.system("mpc load http://serpent0.duckdns.org:8088/mbcfm.pls")

        self.play()
    def play(self):
        os.system("mpc play")
    def pause(self):
        os.system("mpc pause")
    def stop(self):
        os.system("mpc stop")
    def next(self):
        self.play()
        os.system("mpc next")
        print("Next station")
    def previous(self):
        self.play()
        os.system("mpc prev")
        print("Previous station")
    def info(self) -> str:
        info = subprocess.run(["mpc","current"], capture_output=True, text=True)
        return info.stdout


def poweroff():
    print("Shutdown Raspberry Pi")
    os.system("sudo shutdown -h now")


buttonForPowerToggle = Button(3)
buttonForVolumeUp = Button(12)
buttonForVolumeDown = Button(16)


buttonForPowerToggle.when_pressed = poweroff

player = Player()

def volumeUp():
    if buttonForVolumeDown.is_pressed: os.system("amixer sset Digital 3%+")
def volumeDown():
    if buttonForVolumeUp.is_pressed: os.system("amixer sset Digital 3%-")

buttonForVolumeUp.when_pressed = volumeUp
buttonForVolumeDown.when_pressed = volumeDown


buttonForNext = Button(17)
buttonForPrev = Button(27)
buttonForInfo = Button(11)

def info(): 
    info =  player.info()
    player.stop()
    print("Now playing " + info)
    Speech("Now playing " + info,"en").play()
    player.play()
def nextStation():
    if buttonForPrev.is_pressed:
        player.next()
def previousStation():
    if buttonForNext.is_pressed:
        player.previous()

buttonForNext.when_pressed = nextStation
buttonForPrev.when_pressed = previousStation
buttonForInfo.when_pressed = info

pause()