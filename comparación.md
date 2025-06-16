# Comparación entre Programación Tradicional y Programación Orientada a Objetos (POO) en Python

## 🧠 Objetivo
Evaluar las diferencias prácticas y estructurales entre los paradigmas de programación tradicional y programación orientada a objetos, utilizando como ejemplo un programa que calcula el promedio semanal del clima.

---

## 🔹 Programación Tradicional

- **Estructura basada en funciones**: se divide el código en bloques funcionales como `ingresar_temperaturas()` y `calcular_promedio()`.
- **Lógica lineal**: los datos fluyen en una secuencia de pasos clara y directa.
- **Menor reutilización**: para ampliar funcionalidades, a menudo es necesario duplicar o modificar funciones existentes.
- **Útil para problemas simples** y scripts rápidos.

---

## 🔸 Programación Orientada a Objetos (POO)

- **Basada en clases y objetos**: se crea una clase `ClimaSemanal` para encapsular datos y comportamientos.
- **Encapsulamiento**: los datos (temperaturas) y las funciones asociadas (cálculo del promedio) se agrupan de forma coherente.
- **Escalabilidad**: es más fácil extender el código con herencia y polimorfismo (por ejemplo, subclases para diferentes regiones climáticas).
- **Ideal para aplicaciones complejas** y mantenimiento a largo plazo.

---

## 📊 Comparación Directa

| Aspecto                   | Programación Tradicional                  | Programación Orientada a Objetos               |
|--------------------------|-------------------------------------------|------------------------------------------------|
| Enfoque                  | Funcional                                 | Basado en objetos                              |
| Reutilización            | Limitada                                  | Alta mediante herencia y clases                |
| Claridad                 | Alta en programas cortos                  | Alta en programas grandes o modulares          |
| Escalabilidad            | Baja                                      | Alta                                            |
| Ejemplo en este proyecto | Uso de funciones simples                  | Uso de clase `ClimaSemanal` y sus métodos      |

---

## ✅ Conclusión

Ambos enfoques permiten resolver el problema planteado de manera efectiva. Sin embargo, la POO ofrece una base más sólida para extender el programa, aplicar buenas prácticas de mantenimiento y modelar situaciones del mundo real con mayor fidelidad.

---

*Autor: Jordy  
Fecha: Junio de 2025*