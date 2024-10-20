from machine import Pin, PWM, Timer, I2C
import utime

led = PWM(Pin(15))
led.freq(1000)      # Set the frequency value
led_value = 0       #LED brightness initial value
led_speed = 5      # Change brightness in increments of 5



def OnboardLED():
    inled = Pin(25, Pin.OUT) # sandard PICO
    # Onboard LED - Flash setting
    utime.sleep_ms(100)
    inled.value(1)
    utime.sleep_ms(100)
    inled.value(0)
 
 
if __name__ == '__main__':
    while True:
        OnboardLED()
        leds = [Pin(i,Pin.OUT) for i in range(0,5)]

        for n in range(0,5):
            leds[n].value(1)
            utime.sleep_ms(50)
        for n in range(0,5):
            leds[n].value(0)
            utime.sleep_ms(50)
