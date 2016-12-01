import time

import RPi.GPIO as gpio


class Motion(object):
    def __init__(self):
        gpio.setmode(gpio.BCM)
        self.pir_pin = 12
        gpio.setup(self.pir_pin, gpio.IN)
        self.counter = 0
        self.peoplecount = 0

    def check_motion(self):
        try:
            print('pir module test (ctrl+c to exit)')
            time.sleep(1)
            print('ready')
            while True:
                if gpio.input(self.pir_pin):
                    print ('motion detected')
                else:
                    print ('0')
                time.sleep(1)
        except KeyboardInterrupt:
            print('quit')
            gpio.cleanup()
