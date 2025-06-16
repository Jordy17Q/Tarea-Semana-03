# Función para ingresar temperaturas
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

main()