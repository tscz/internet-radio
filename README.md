# Internet-Radio for Raspberry Pi OS based on MPD
 
## Features 
* receives radio streams from internet and plays them
* Can switch between predefined internet stations
* Displays current internet station + Infos from the stream
* Allows to increase/decrease the volume via rotary switch
* Allows to switch the channel via rotary switch 
* Can be turned off/on via button
* Remembers last station and volume value
* Can be controlled via smartphone app

## Planned features
* Allows CRUD for Internet Stations+Stream URLS
* Shows a status light while running


## Setup

### Hardware Prerequisites
* Raspberry Pi 2 Model B Rev 1.1
* Hifiberry Amp2
* 3 Speaker
* 3-Way Speaker Crossover
* 2 Rotary Encoder with push button

### Software Prerequisites
* Raspberry Pi OS Lite (https://www.raspberrypi.org/downloads/raspberry-pi-os/)
* MPD (https://www.musicpd.org/)
* MPC (https://www.musicpd.org/clients/mpc/)
* Google Speech for Python (https://pypi.org/project/google-speech/)
* GPIOZero (https://gpiozero.readthedocs.io/en/stable/)

### Install
* Download Raspberry Pi OS and install on SD card
* Install Audio Hardware
* Install MPD
* Install MPC
* Install Python
* Install PIP + 3rd party libraries
* Install Script and setup Deamon Process
* Install Android App