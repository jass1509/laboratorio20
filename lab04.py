tramos = [
    (20000, 0.00),
    (50000, 0.10),
    (100000, 0.20),
    (float("inf"), 0.30)
]

ingreso_mensual = float(input("Ingrese el ingreso mensual: "))

ingreso_anual = ingreso_mensual * 14
print("\nIngreso anual calculado:", ingreso_anual, "\n")

impuesto_total = 0
limite_inferior = 0

for limite_superior, tasa in tramos:
    if ingreso_anual > limite_inferior:
        monto_tramo = min(ingreso_anual, limite_superior) - limite_inferior
        impuesto_tramo = monto_tramo * tasa
        impuesto_total += impuesto_tramo

        print(
            "Tramo [",
            limite_inferior, "-",
            limite_superior, "]",
            "Monto:", monto_tramo,
            "Tasa:", tasa * 100, "%",
            "Impuesto:", impuesto_tramo
        )

        limite_inferior = limite_superior

tasa_efectiva = (impuesto_total / ingreso_anual) * 100

print("\n--- RESULTADOS ---")
print("Total de impuestos:", impuesto_total)
print("Tasa efectiva real:", tasa_efectiva, "%")
