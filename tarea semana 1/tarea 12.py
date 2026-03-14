capital = float(input("ingrese su capital:"))
tasa = float(input("ingrese la tasa (%):"))
años = float(input("ingrese los años:"))
tasa = tasa / 100
interes = capital * tasa * años
montototal = capital + interes
print ("su interes es de",interes,"y su monto total es",montototal)
