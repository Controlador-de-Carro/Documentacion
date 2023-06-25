from machine import Pin, SoftI2C, sleep

i2c = SoftI2C(scl = Pin(18), sda = Pin(19), freq= 100000) #Establecer pines para sda y scl junto con frecuencia
i2c.init(scl = Pin(18), sda = Pin(19), freq= 100000)
i2c.start()
print(i2c.scan()) # Escanear dispositivos

print(i2c.readfrom(104, 8))

sleep(1)
print(i2c.readfrom(104, 8))