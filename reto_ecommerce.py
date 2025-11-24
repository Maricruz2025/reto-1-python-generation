productos = [
    {"id": 1, "nombre": "Laptop Pro 14", "categoria": "Computo", "precio": 25000, "descuento": 0.10, "stock": 5},
    {"id": 2, "nombre": "Mouse Gamer X", "categoria": "Accesorios", "precio": 1200, "descuento": 0.15, "stock": 20},
    {"id": 3, "nombre": "Teclado Mecánico K1", "categoria": "Accesorios", "precio": 2200, "descuento": 0.05, "stock": 10},
    {"id": 4, "nombre": "Monitor 27'' 4K", "categoria": "Computo", "precio": 8000, "descuento": 0.20, "stock": 7},
    {"id": 5, "nombre": "Audífonos Bluetooth Z", "categoria": "Audio", "precio": 1500, "descuento": 0.0, "stock": 15},
]

ventas = [
    {"venta_id": 101, "producto_id": 1, "cantidad": 1, "cliente": "Ana"},
    {"venta_id": 102, "producto_id": 2, "cantidad": 2, "cliente": "Luis"},
    {"venta_id": 103, "producto_id": 4, "cantidad": 1, "cliente": "Sofía"},
    {"venta_id": 104, "producto_id": 2, "cantidad": 1, "cliente": "Carlos"},
    {"venta_id": 105, "producto_id": 5, "cantidad": 3, "cliente": "Ana"},
]
tienda_info = ("TechieStore", "Santiago", 2025)

#✅ 1. Mensaje de bienvenida

print(f"Bienvenido a {tienda_info[0]} en {tienda_info[1]} {tienda_info[2]}")

#✅ 2. Mostrar cuántos productos existen

print(f"Total de productos: {len(productos)}")

#✅ 3. Precio final con descuento (sin loops)

# Producto 1
precio_final_1 = 25000 - (25000 * 0.10)
print(f"Precio final Laptop Pro 14: {precio_final_1}")

# Producto 2
precio_final_2 = 1200 - (1200 * 0.15)
print(f"Precio final Mouse Gamer X: {precio_final_2}")

# Producto 3
precio_final_3 = 2200 - (2200 * 0.05)
print(f"Precio final Teclado Mecánico K1: {precio_final_3}")

# Producto 4
precio_final_4 = 8000 - (8000 * 0.20)
print(f"Precio final Monitor 27'' 4K: {precio_final_4}")

# Producto 5
precio_final_5 = 1500 - (1500 * 0.0)
print(f"Precio final Audífonos Bluetooth Z: {precio_final_5}")

#✅ 4. Total de cada venta (sin loops)

# Venta 101
total_101 = precio_final_1 * 1
print(f"Venta 101: Ana compró un Laptop Pro 14 y pagó: {total_101}")

# Venta 102
total_102 = precio_final_2 * 2
print(f"Venta 102: Luis compró dos Mouses Gamer X y pagó: {total_102}")

# Venta 103
total_103 = precio_final_4 * 1
print(f"Venta 103: Sofía compró un Monitor 27'' 4K y pagó: {total_103}")

# Venta 104
total_104 = precio_final_2 * 1
print(f"Venta 104: Carlos compró un Mouse Gamer X y pagó: {total_104}")

# Venta 105
total_105 = precio_final_5 * 3
print(f"Venta 105: Ana compró tres Audífonos Bluetooth Z y pagó: {total_105}")
 
 #✅ 5. Ingreso total de la tienda

ingreso_total = total_101 + total_102 + total_103 + total_104 + total_105
print(f"Ingreso total: {ingreso_total}")

