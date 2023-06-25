from machine import Pin
from machine import PWM
from time import sleep

pwm23 = PWM(Pin(23))
#Acá cambien el pin por el pin que estén usando

freq = pwm23.freq()
pwm23.freq(1000)
#Definir frecuencia

def loopie (t, mx, c,s):
    i = 0
    while i < t:
        pwm23.duty(int(c/t))
        pwm23.deinit()
        sleep(s/t)
        pwm23.init()
        c = c*2
        i = i +1
loopie(24,1020,1,5)