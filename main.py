# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep
import dht
from oled import OLED
from parallaxlcd import CharLCD

sensor = dht.DHT22(Pin(14))
lcd = CharLCD()
lcd.setup()

oled = OLED()
oled.switchOn()
oled.clearAll()

max = -100
min = 100

while True:
    
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9/5) + 32.0

        if temp < min:
            min = temp
        if temp > max:
            max = temp

        message1 = ('TempC   : %3.1f C' % temp)
        message2 = ('TempF   : %3.1f F' %temp_f)
        message3 = ('Feuchte : %3.1f %%' %hum)
        #message4 = ('Min: %3.1f %%   Max: %3.1f %% ' %min %max)
        message4 = ('Mi:%3.1f ' %min + 'Mx: %3.1f' %max)
        
        lcd.print(message1, 0)
        lcd.print(message2, 1)
        #lcd.print(message3, 2)
        lcd.print(message4, 2)

        oled.writeAt(message1, 0, 0)
        oled.writeAt(message2, 0, 1)
        #oled.writeAt(message3, 0, 2)
        oled.writeAt(message4, 0, 2)

    except OSError as e:
        print('Failed to read sensor.')
