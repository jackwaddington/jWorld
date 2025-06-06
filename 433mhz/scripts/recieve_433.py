from datetime import datetime
import matplotlib.pyplot as pyplot
import RPi.GPIO as GPIO

RECEIVED_SIGNAL = [[], []]  # [[time of reading], [signal reading]]
MAX_DURATION = 5
RECEIVE_PIN = 4 #gpio ref, this is pin 7 on the board

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RECEIVE_PIN, GPIO.IN)
    cumulative_time = 0
    beginning_time = datetime.now()
    print('**Started recording**')  # Corrected line
    while cumulative_time < MAX_DURATION:
        time_delta = datetime.now() - beginning_time
        RECEIVED_SIGNAL[0].append(time_delta)
        RECEIVED_SIGNAL[1].append(GPIO.input(RECEIVE_PIN))
        cumulative_time = time_delta.seconds
    print('**Ended recording**')  # Corrected line
    print(len(RECEIVED_SIGNAL[0]), 'samples recorded')  # Corrected line
    GPIO.cleanup()

    print('**Processing results**')  # Corrected line
    for i in range(len(RECEIVED_SIGNAL[0])):
        RECEIVED_SIGNAL[0][i] = RECEIVED_SIGNAL[0][i].seconds + RECEIVED_SIGNAL[0][i].microseconds / 1000000.0

    print('**Plotting results**')  # Corrected line
    pyplot.plot(RECEIVED_SIGNAL[0], RECEIVED_SIGNAL[1])
    pyplot.axis([0, MAX_DURATION, -1, 2])
    pyplot.show()

