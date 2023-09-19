import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        if sonar.distance >= 80:
            print(f'Garage door is OPEN. Distance is {sonar.distance}')
        elif sonar.distance < 80:
            print(f'Garage door is CLOSED. Distance is {sonar.distance}')
        else:
            print('Something\'s bugged.')
    except RuntimeError:
        print("Retrying!")
    time.sleep(2)