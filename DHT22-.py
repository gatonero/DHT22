# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep
import dht

sensor = dht.DHT22(Pin(23))

while True:
    
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9/5) + 32.0
        message1 = ('TempC   : %3.1f C' % temp)
        message2 = ('TempF   : %3.1f F' %temp_f)
        message3 = ('Feuchte : %3.1f %%' %hum)
        
        print(message1)
        print(message2)
        print(message3)

    except OSError as e:
        print('Failed to read sensor.')