from machine import Pin
from machine import PWM

pinNum = 2
pinNumD = 4

pwm0 = PWM(Pin(pinNum))
pwm0.freq(1000)

pwm1 = PWM(Pin(pinNumD))
pwm1.freq(1000)

#funcionalidad en porcentaje (Solo uno prendido a la vez, el otro en 0)
dut = pwm0.duty()
pwm0.duty(0)

dutty = pwm1.duty()
pwm1.duty(512)
    
pwm0.init
pwm1.init