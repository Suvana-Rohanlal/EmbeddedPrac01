#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Suvana Rohanlal 
Student Number: RHNSUV001
Prac: 1
Date: 24/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
chan_in = [16,18]
chan_out = [29,31,33]
GPIO.setup(chan_in,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(chan_out,GPIO.OUT)

arr1 = ["0","0","0","0","1","1","1","1"]
arr2 = ["0","0","1","1","0","0","1","1"]
arr3 = ["0","1","0","1","0","1","0","1"]
# Logic that you write
def main():
    GPIO.setwarnings(False);

global i
i=0

def increase(channel):
	global i
	i+=1
	if i == 8:
		i = 0
	GPIO.output(29, int(arr1[i]))
	GPIO.output(31, int(arr2[i]))
	GPIO.output(33, int(arr3[i]))
	print("Increased by 1")

def decrease(channel):
	global i
	i-=1
	if i == -1:
		i = 7
	GPIO.output(29, int(arr1[i]))
	GPIO.output(31, int(arr2[i]))
	GPIO.output(33, int(arr3[i]))
	print("Decreased by 1")

GPIO.add_event_detect(16, GPIO.FALLING, callback = increase, bouncetime=150)
GPIO.add_event_detect(18, GPIO.FALLING, callback = decrease, bouncetime=150)

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    
