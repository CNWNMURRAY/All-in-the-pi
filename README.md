# All-in-the-pi
ABOUT

This project is a homework assignment that requires us to contribute to and or modify an open source project. We chose to contribute if possible and modify three open source projects that use the raspberrypi.

THREE OPEN SOURCE PROJECTS

-[samuelclay/Raspberry-Pi-Photo-Frame] (https://github.com/samuelclay/Raspberry-Pi-Photo-Frame.git)

-[simonmonk/raspirobotboard3] (https://github.com/simonmonk/raspirobotboard3.git)

-[jpescada/TwitterPiBot] (https://github.com/jpescada/TwitterPiBot.git)

GOAL FOR EACH PROJECT

-samuelclay/Raspberry-Pi-Photo-Frame

-[] add robotic functionailty meaning it will be able to move.

-[X] add a calendar reader and text reader (task, todo list)

-[X] attempt to get modifications accepted by original project

~~-claywebb/robot-framework~~ this code was stricken due to difficulties using gpio pins with the raspberry pi 3. 

Common issues with the raspberry pi 3 in accessing gpio pins using sudo apt-get rpio.gpio. The raspberry pi 3 was not recognized as a raspberry pi.

This was also an issue with the raspberry pi2 but it was solved.

The goals for the project were:

-[] improve documentation

-[X] add calendar/photo display

-[X] add text reader

-[] attempt to get modifications accepted

-jpescada/TwitterPiBot

-[] add motion sensor

-[X] add photo and calendar display

-[X] read calendar events

-[] attempt to get modifications accepted

Goal for All-in-the-pi

We are trying to make a raspberrypi robot that will display a google calendar, read off a todo list or task list and then show photos when it senses motion. The raspberrypi robot should remind it's owner of any events or task they have to do that day, update them on current events that intrest them and to stop and smell the roses with pictures of family and friends.

Hardware Parts for a rover

-[] Raspberry pi 3

-[] LCD screen

-[] HDMI cord length depends on robot ddesign

-[] PIR (motion) sensor

-[] SD card

-[] portable charger or battery pack

Software 

Robotic functions

$ sudo pip install rrb3 

Calendar

$sudo pip install google-api-python-client (edited)

$pip install oauth2client

$pip install httplib2

Test-to-speech
$ sudo apt-get install flite
$ sudo pip install puyttsx
