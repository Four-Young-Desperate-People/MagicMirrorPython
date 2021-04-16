#!/usr/bin/python3

import RPi.GPIO as GPIO
#from time import sleep
import asyncio
import websockets


async def socket():
    uri = "ws://localhost:3683/led"
    white = 6
    blue = 5
    green = 26
    red = 21
    GPIO.setwarnings(False)  # disable warnings
    GPIO.setmode(GPIO.BCM)  # set pin numbering system to GPIO
    GPIO.setup(white, GPIO.OUT)
    white_pwm = GPIO.PWM(white, 100)  # create PWM instance with frequency
    white_pwm.start(50)  # start PWM of required Duty Cycle
    async with websockets.connect(uri) as websocket:
        print("Connected to websocket")
        while True:
            he = await websocket.recv()

            white_pwm.ChangeDutyCycle(int(he))



def main():
    white = 6
    blue = 5
    green = 26
    red = 21

    asyncio.get_event_loop().run_until_complete(socket())


if __name__ == "__main__":
    main()
