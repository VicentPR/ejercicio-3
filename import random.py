import random
import math

# Lista de vendedores
vendedores = [
    "Camila Soto", "Esteban Ruiz", "Daniela Pérez", "Jorge Vargas",
    "Soledad Acuña", "Felipe Campos", "Laura Silva", "Marcelo Torres"
]

# Diccionario para almacenar las ventas mensuales
ventas = {}

# Función 1: Generar ventas aleatorias
def generar_ventas():
    for vendedor in vendedores:
        ventas[vendedor] = random.randint(200000, 2000000)
    print("\nVentas generadas correctamente.")

# Función 2: Clasificar ventas
def clasificar_ventas():
    if not ventas:
        print("Primero debe generar las ventas.")
        return

    print("\nClasificación de Ventas:")
    for vendedor, monto in ventas.items():
        if monto < 500000:
            categoria = "Menores a $500.000"
        elif 500000 <= monto <= 1200000:
            categoria = "Entre $500.000 y $1.200.000"
        else:
            categoria = "Mayores a $1.200.000"
        print(f"{vendedor}: ${monto} → {categoria}")

# Función 3: Estadísticas generales
def estadisticas():
    if not ventas:
        print("Primero debe generar las ventas.")
        return

    valores = list(ventas.values())
    max_venta = max(valores)
    min_venta = min(valores)
    promedio = sum(valores) / len(valores)

    producto = 1
    for v in valores:
        producto *= v
    media_geom = producto ** (1 / len(valores))

    print("\nEstadísticas de Ventas:")
    print(f"Venta máxima: ${max_venta}")
    print(f"Venta mínima: ${min_venta}")
    print(f"Promedio de ventas: ${promedio:.2f}")
    print(f"Media geométrica: ${media_geom:.2f}")

# Función 4: Reporte completo de comisiones
def reporte_comisiones():
    if not ventas:
        print("Primero debe generar las ventas.")
        return

    print("\nReporte Completo de Comisiones:")
    for vendedor, monto in ventas.items():
        comision = monto * 0.10
        impuesto = monto * 0.08
        venta_neta = monto + comision - impuesto

        print(f"\n{vendedor}")
        print(f"  Venta bruta: ${monto}")
        print(f"  Comisión (10%): ${comision:.2f}")
        print(f"  Impuesto (8%): ${impuesto:.2f}")
        print(f"  Venta neta final: ${venta_neta:.2f}")

# Función 5: Finalizar programa mostrando datos personales
def finalizar():
    print("\nNombre: Juan Pérez")
    print("RUT: 12.345.678-9")
    print("Carrera: Ingeniería en Informática")
    print("Gracias por usar el sistema.")

# Menú principal
def menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Generar Ventas Aleatorias")
        print("2. Clasificar Ventas")
        print("3. Estadísticas Generales")
        print("4. Reporte Completo de Comisiones")
        print("5. Finalizar Programa")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            generar_ventas()
        elif opcion == "2":
            clasificar_ventas()
        elif opcion == "3":
            estadisticas()
        elif opcion == "4":
            reporte_comisiones()
        elif opcion == "5":
            finalizar()
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
