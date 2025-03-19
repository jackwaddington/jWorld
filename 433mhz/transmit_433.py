import time
import sys
import RPi.GPIO as GPIO

off_1 = '1011111110101010110000111'
off_2 = '1011111110101010001100111'
off_3 = '1011111110101000111100111'
off_4 = '1011111110100010111100111'
off_5 = '1011111110001010111100111'

on_1 = '1011111110101010110011001'
on_2 = '1011111110101010001111001'
on_3 = '1011111110101000111111001'
on_4 = '1011111110100010111111001'
on_5 = '1011111110001010111111001'

short_delay = 0.00016
long_delay = 0.00051
extended_delay = 0.0096

NUM_ATTEMPTS = 10
TRANSMIT_PIN = 26

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for t in range(NUM_ATTEMPTS):
        for i in code:
            if i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(short_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(long_delay)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(long_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_delay)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(extended_delay)
    GPIO.cleanup()

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        exec('transmit_code(' + str(argument) + ')')
