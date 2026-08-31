from machine import Pin
from time import sleep

# Built-in LED (GPIO 2 on most ESP32 development boards)
led = Pin("A6", Pin.OUT)
led1 = Pin("A7", Pin.OUT)
led2 = Pin("B0", Pin.OUT)
led3 = Pin("B1", Pin.OUT)

while True:
    led.on()        # LED ON
    print("LED_RED_ON")
    sleep(1)        # Wait 1 second
    led.off()       # LED OFF
    print("LED_RED_OFF")
    sleep(1)        # Wait 1 second
    led1.on()        # LED1 ON
    print("LED_GREEN_ON")
    sleep(1)        # Wait 1 second
    led1.off()       # LED1 OFF
    print("LED_GREEN_OFF")
    sleep(1)        # Wait 1 second
    led2.on()        # LED2 ON
    print("LED_BLUE_ON")
    sleep(1)        # Wait 1 second
    led2.off()       # LED2 OFF
    print("LED_BLUE_OFF")
    sleep(1)        # Wait 1 second
    led3.on()        # LED3 ON
    print("LED_LIGHT_GREEN_ON")
    sleep(1)        # Wait 1 second
    led3.off()       # LED3 OFF
    print("LED_LIGHT_GREEN_OFF")
    sleep(1)        # Wait 1 second
    
