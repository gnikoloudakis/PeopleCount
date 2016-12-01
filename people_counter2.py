import time

import RPi.GPIO as gpio


class Motion(object):
    def __init__(self):
        gpio.setmode(gpio.BCM)
        self.pir_pin = 12
        gpio.setup(self.pir_pin, gpio.IN)
        self.counter = 0
        self.peoplecount = 0

    def start_sensing(self):
        # print('pir module test (ctrl+c to exit)')
        # time.sleep(1)
        # print('ready')
        # while True:
        if gpio.input(self.pir_pin):
            # print ('motion detected')
            return True
        else:
            # print ('0')
            return False
        # time.sleep(1)

    def stop_sensing(self):
        print('quit')
        gpio.cleanup()
