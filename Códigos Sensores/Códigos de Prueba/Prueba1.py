from machine import Pin
from machine import PWM

pwm23 = PWM(Pin(23))
#Acá cambien el pin por el pin que estén usando

freq = pwm23.freq()
pwm23.freq(1000)
#Definir frecuencia
duty = pwm23.duty()
pwm23.duty(512)
#Definir porcentaje sobre 1023 (512 es 50%)
pwm23.init()