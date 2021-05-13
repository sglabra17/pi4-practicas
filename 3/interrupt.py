import lcddriver
import RPi.GPIO as GPIO
import time

#instance -> lcd
lcd = lcddriver.lcd()

GPIO.setwarnings(False)#disable gpio warnigs
#GPIO mode
GPIO.setmode(GPIO.BCM)
#GPIO setup
GPIO.setup(17,GPIO.IN)
GPIO.setup(18,GPIO.OUT)

try:
    while True:
        GPIO.output(18,GPIO.input(17))
        if GPIO.input(17):
            lcd.lcd_clear()
            lcd.lcd_display_string("PULSADO",1)
            time.sleep(0.1)
        else:
            lcd.lcd_clear()
            lcd.lcd_display_string("LEVANTADO",1)
            time.sleep(0.1)     
except:
    GPIO.cleanup()
    print('Proceso Interrumpido')




