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
chan_in = [16,18]  #input(buttons) GPIO channels are 16 and 18
chan_out = [11,13,15] #output(LEDs) GPIO channels are 11, 13 and 15
GPIO.setup(chan_in,GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #setting input channels
GPIO.setup(chan_out,GPIO.OUT) #setting output channels

arr1 = ["0","0","0","0","1","1","1","1"] #3 arrays to store numbers 0 to 7
arr2 = ["0","0","1","1","0","0","1","1"] #these arrays will be used for each LED
arr3 = ["0","1","0","1","0","1","0","1"]
# Logic that you write
def main():
	GPIO.setwarnings(False)

global i
i=0

def increase(channel): #method to increase count
	global i
	i+=1
	if i == 8:   #checks if the button count goes to 8 and sets the count to zero
		i = 0
	GPIO.output(11, int(arr1[i])) #setting the led to the number on the counter
	GPIO.output(13, int(arr2[i]))
	GPIO.output(15, int(arr3[i]))
	print("Increased by 1")

def decrease(channel): #method to decrease count
	global i
	i-=1
	if i == -1: #checks i the button count goes to -1 and sets it to 7
		i = 7
	GPIO.output(11, int(arr1[i])) #setting the led to the number on the counter
	GPIO.output(13, int(arr2[i]))
	GPIO.output(15, int(arr3[i]))
	print("Decreased by 1")

GPIO.add_event_detect(16, GPIO.FALLING, callback = increase, bouncetime=150) #add falling edge detection on the channel
GPIO.add_event_detect(18, GPIO.FALLING, callback = decrease, bouncetime=150) #ignoring further edges for 150ms for switch bounce handling  

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
