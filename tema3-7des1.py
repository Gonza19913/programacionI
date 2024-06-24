inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brocoli", "cebolla", "kiwis"]

#Gestión del inventario
#Un cliente viene y compra todas las bananas.
#Pregunta 3: ¿Cómo actualizarías el inventario después de la venta?

inventario.remove("bananas")
print(inventario)

#Ahora recibes un envío de nuevos productos: "frutillas", "apio" y "papas".
#Pregunta 4: ¿Cómo añadirías estos productos al inventario?

inventario.append("frutillas")
inventario.append("apio")
inventario.append("papas")
print(inventario)

