import val1
i = 0
while True:
    Valores1 = val1.tomar_val(i)
    
    if Valores1["AcY"] > 1000:
        print("movimiento en y")
        
    if Valores1["AcX"] > 1000:
        print("movimiento en x")
        
    if Valores1["GyY"] > 1000:
        print("Giro izquierda")
    
    if Valores1["GyX"] > 1000:
        print("Giro abajo")
    
    if Valores1["GyX"] < -1000:
        print("Giro arriba")
    
    if Valores1["GyY"] < -1000:
        print("Giro derecha")
        
    print(Valores1)
    i = i+1