from conversor_unidades import ConversorUnidades

conversor = ConversorUnidades()

metros_a_p = conversor.metros_a_pies(10)
kilos_a_lb = conversor.kilogramos_a_libras(5)
celsius_a_f = conversor.celsius_a_fahrenheit(25)

print(f"10 metros son {metros_a_p} pies")
print(f"5 kilogramos son {kilos_a_lb} libras")
print(f"25 °C son {celsius_a_f} °F")