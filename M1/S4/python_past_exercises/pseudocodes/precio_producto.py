print("Ingrese el precio del producto")
precio_producto = int(input())
if precio_producto < 100:
    descuento = precio_producto * 0.02
else:
    descuento = precio_producto * 0.10
precio_producto_final = precio_producto - descuento
print(f"El precio final es: {precio_producto_final}")