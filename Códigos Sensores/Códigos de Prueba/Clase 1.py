from machine import Pin
from machine import PWM

pinNum = 2
pinNumD = 4

pwm0 = PWM(Pin(pinNum))
pwm0.freq(1000)

pwm1 = PWM(Pin(pinNumD))
pwm1.freq(1000)

#funcionalidad en porcentaje (Solo uno prendido a la vez, el otro en 0)
fep1 = int(0)
pwm0.duty(int(fep1/100 * 1023))

fep2 = int(50)
pwm1.duty(int(fep2/100 * 1023))

pwm0.init
pwm1.init