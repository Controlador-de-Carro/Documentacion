from machine import SoftI2C
from machine import Pin
from machine import sleep
import mpu6050

def obt_val ():
    

    i2c = SoftI2C(scl=Pin(21), sda=Pin(22))     #initializing the I2C method for ESP32
    mpu= mpu6050.accel(i2c)
    sleep(10)
    base = mpu.get_values()
    basval = []
    suma = 0
    for y in base:
        for n in range(100):
            base = mpu.get_values()
            basval.append(base[y])
            suma += basval[n]
            sleep(15)
        promedio = suma/100
        base[y] = promedio
    print (base)
    while True:
        actual = mpu.get_values()
        for x in actual:
            if not x == "GyX" or not x == "GyY" or not x == "GyZ":
                if abs(actual[x]) >= 250 and abs(actual[x]) < 1000:
                    base[x] = abs(actual [x])
            actual[x] = abs(actual[x] - base[x])
            if not x == "GyX" or not x == "GyY" or not x == "GyZ":
                if abs(actual[x]) >= 250 and abs(actual[x]) < 1000:
                    print("flag")
        print(actual) 
        sleep(500)
obt_val()