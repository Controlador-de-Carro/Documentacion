from machine import SoftI2C
from machine import Pin
from machine import sleep
i2c = SoftI2C(scl=Pin(21), sda=Pin(22))
print(i2c.scan())