import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BCM)
gpio.setup(12, gpio.IN, pull_up_down=gpio.PUD_DOWN)

counter = 0
peoplecount = 0


while(1):
	presence = gpio.input(12)
	if presence:
		print("HIGH")
	else:
		print("LOW")
	time.sleep(0.1)
