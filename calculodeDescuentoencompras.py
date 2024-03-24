# Definición de la función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la función proporcionando solo el monto total de la compra
descuento1 = calcular_descuento(100)
monto_final1 = 100 - descuento1
print("Descuento aplicado:", descuento1)
print("Monto final a pagar:", monto_final1)

# Llamada a la función proporcionando tanto el monto total de la compra como el porcentaje de descuento
descuento2 = calcular_descuento(200, 15)
monto_final2 = 200 - descuento2
print("Descuento aplicado:", descuento2)
print("Monto final a pagar:", monto_final2)