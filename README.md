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
* SSH to connect remotely connect to Raspi

### Install
1. Download Raspberry Pi OS and install on SD card
2. Boot and config Raspberry Pi Os via `sudo raspi-cofig` to basic config:
    * Change password
    * Change keyboard layout
    * Change Wifi
    * Enable SSH
3. Connect via SSH to raspi , i.e. via `ssh pi@hostname`
4. Configure Audio Hardware (see https://www.hifiberry.com/docs/software/configuring-linux-3-18-x/)
    ````bash
    sudo nano /boot/config.txt
    sudo nano /etc/asound.conf
    sudo reboot
    ````
    After succesfull activation the audio hardware should be detected as shown in 
    ````bash
    pi@raspberrypi:~ $ aplay -l
    **** List of PLAYBACK Hardware Devices ****
    card 0: sndrpihifiberry [snd_rpi_hifiberry_dacplus], device 0: HiFiBerry DAC+ HiFi pcm512x-hifi-0 [HiFiBerry DAC+ HiFi pcm512x-hifi-0]
    Subdevices: 1/1
    Subdevice #0: subdevice #0
    ````
5. Install MPD and verify that it is started 
    ````bash
    sudo apt update
    sudo apt upgrade
    sudo apt install mpd
    sudo service mpd start
    ````
    Find out the current alsa audio hardware device and mixer index. The mixer control for an AMP2 is always "Digital" (see https://www.hifiberry.com/docs/archive/mixer-controls-on-the-hifiberry-boards/)
    ````bash
    aplay -l
    aplay -L
    ````
    and configure it in the `/etc/mpd.conf` file with additional block
    ````bash
    audio_output {
            type            "alsa"
            name            "HifiBerry Amp2 Device"
            device          "hw:CARD=sndrpihifiberry,DEV=0"
            mixer_type      "hardware"      
            mixer_device    "default"       
            mixer_control   "Digital"      
            mixer_index     "0"     
    }       
    ````

* Install MPC and verify that it is working
    ````bash
    sudo apt install mpc
    mpc load http://streams.fluxfm.de/live/mp3-320/audio/play.m3u
    mpc play
    ````
    > Hint: radio station urls can be found via WEB API https://de1.api.radio-browser.info/json/stations/byname/{stationName} quite easily
* Install Python 3, Pip + 3rd party libraries
    ````bash
    python3 --version
    sudo apt install python3-pip
    sudo apt install python3-gpiozero
    pip3 install google_speech
    sudo apt install sox libsox-fmt-mp3
    ````
* Install Script and Setup Deamon Process
    ````bash
    nano /home/pi/.local/bin/radio
    chmod +x radio
    ````
    Create a service deamon `/etc/systemd/system/radio.service`

* Install Android App