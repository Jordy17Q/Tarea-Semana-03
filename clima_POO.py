class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def agregar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def calcular_promedio(self):
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

# Programa principal
def main():
    clima = ClimaSemanal()
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        clima.agregar_temperatura(temp)

    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

main()