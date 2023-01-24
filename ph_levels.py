ph = int(input("dime el nivel de ph (0 y 14)"))
if ph > 7:
    print("básico")
elif ph < 7:
    print("ácido")
else:
    print("Neutral")