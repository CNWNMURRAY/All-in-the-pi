#Install the raspberry pi 3  library in a Terminal window using

$ sudo pip install rrb3 

#Open a Python console by typing the following into a Terminal window:

$ sudo python #(python 2)
$ sudo apt-get (python #(python 3)

import RPi.GPIO as GPIO # imports general-purpose input/output (GPIO) is a generic pin on an integrated circuit 
#whose behavior—including whether it is an input or output pin—is controllable by the user at run time.
import time

#type the following, one line at a time:

from rrb3 import *
rr = RRB3(9, 6)
rr.set_led1(1)
rr.set_led1(0)
rr.set_led2(1)
rr.set_led2(0)
rr.sw1_closed()
#should display the answer "False" because no switch is attached.

#LED LIGHTS
#To turn LED1 on just do:

rr.set_led1(1)

#To turn it off again do:

rr.set_led1(0)

#To turn the Open Collector OC1 output on just do:

rr.set_oc1(1)

#To turn it off again do:

rr.set_oc1(0)

