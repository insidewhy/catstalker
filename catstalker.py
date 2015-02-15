#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import argparse

def main():
    parser = argparse.ArgumentParser(description='control energenie remote board')
    parser.add_argument('-s', '--socket', type=int)
    parser.add_argument('-o', '--off', action='store_true')
    args = parser.parse_args()

    try:
        # set the pins numbering mode
        GPIO.setmode(GPIO.BOARD)

        # Select the GPIO pins used for the encoder K0-K3 data inputs
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)

        # Select the signal used to select ASK/FSK
        GPIO.setup(18, GPIO.OUT)

        # Select the signal used to enable/disable the modulator
        GPIO.setup(22, GPIO.OUT)

        # Disable the modulator by setting CE pin lo
        GPIO.output (22, False)

        # Set the modulator to ASK for On Off Keying
        # by setting MODSEL pin lo
        GPIO.output (18, False)

        # Initialise K0-K3 inputs of the encoder to 0000
        GPIO.output (11, False)
        GPIO.output (15, False)
        GPIO.output (16, False)
        GPIO.output (13, False)
        time.sleep(0.25)

        # socket on    off
        # all    1011  0011
        # 1      1111  0111
        # 2      1110  0110
        # 3      1101  0101
        # 4      1100  0100
        pin0 = not args.off
        pin1 = True
        pin2 = True
        pin3 = True

        if args.socket is None:
            pin1 = False
        elif args.socket == 2:
            pin3 = False
        elif args.socket == 3:
            pin2 = False
        elif args.socket == 4:
            pin3 = pin2 = False

        set_output(pin3, pin2, pin1, pin0)

        GPIO.cleanup()

    # Clean up the GPIOs for next time
    except KeyboardInterrupt:
        GPIO.cleanup()

def set_output(pin3, pin2, pin1, pin0):
    GPIO.output (11, pin3)
    GPIO.output (15, pin2)
    GPIO.output (16, pin1)
    GPIO.output (13, pin0)
    # let it settle, encoder requires this
    time.sleep(0.1)
    # Enable the modulator
    GPIO.output (22, True)
    # keep enabled for a period
    time.sleep(0.25)
    # Disable the modulator
    GPIO.output (22, False)

main()
