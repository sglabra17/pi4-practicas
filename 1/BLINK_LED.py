import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

pines = [21,20,16,12,1,7,8,25,24,23,18,17]

for i in pines:
    
    GPIO.setup(i,GPIO.OUT)

while True:
    for b in pines:
        GPIO.output(b,1)
    time.sleep(0.2)

    for b in pines:
        GPIO.output(b,0)
    time.sleep(0.2)
    
GPIO.cleanup()

print('fiN')