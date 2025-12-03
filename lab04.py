# Definición de tramos (límite superior y tasa)
tramos = [
    (20000, 0.00),
    (50000, 0.10),
    (100000, 0.20),
    (float("inf"), 0.30)
]

ingreso_mensual = float(input("Ingrese el ingreso mensual: "))

# Ingreso anual: 12 sueldos + 2 aguinaldos
ingreso_anual = ingreso_mensual * 14

print(f"\nIngreso anual calculado: ${ingreso_anual:.2f}\n")

impuesto_total = 0
ingreso_restante = ingreso_anual
limite_inferior = 0

for limite_superior, tasa in tramos:
    if ingreso_anual > limite_inferior:
        
        monto_tramo = min(ingreso_anual, limite_superior) - limite_inferior
        impuesto_tramo = monto_tramo * tasa
        impuesto_total += impuesto_tramo

        print(f"Tramo [{limite_inferior} - {limite_superior}] "
              f"→ Monto: ${monto_tramo:.2f} | Tasa: {tasa*100}% | Impuesto: ${impuesto_tramo:.2f}")

        limite_inferior = limite_superior

tasa_efectiva = (impuesto_total / ingreso_anual) * 100

print("\n--- RESULTADOS ---")
print(f"Total de impuestos: ${impuesto_total:.2f}")
print(f"Tasa efectiva real: {tasa_efectiva:.2f}%")
