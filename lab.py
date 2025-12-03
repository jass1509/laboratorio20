# --- ENTRADAS ---
salario_base = float(input("Salario base: "))
horas_extras = float(input("Horas extras trabajadas: "))
pago_hora_extra = float(input("Pago por hora extra: "))
bono = float(input("Bono: "))
afp = float(input("Porcentaje AFP: "))
salud = float(input("Porcentaje Salud: "))

# --- CÁLCULOS ---
salario_bruto = salario_base + (horas_extras * pago_hora_extra) + bono

descuento_afp = salario_base * (afp / 100)
descuento_salud = salario_base * (salud / 100)
descuentos_totales = descuento_afp + descuento_salud

salario_neto = salario_bruto - descuentos_totales

# --- RESULTADOS ---
print("\n--- RESULTADOS ---")
print(f"Salario Bruto: ${salario_bruto:.2f}")
print(f"Descuentos Totales: ${descuentos_totales:.2f}")
print(f"Salario Neto: ${salario_neto:.2f}")
