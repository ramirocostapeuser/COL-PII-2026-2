# Ejercicio 8 - Pipeline de procesamiento de ventas

from ejercicio7 import mide_tiempo  # decorador del ejercicio 7

ventas = [
    {"producto": "Notebook", "monto": 450000, "region": "Norte"},
    {"producto": "Mouse", "monto": 3500, "region": "Sur"},
    {"producto": "Monitor", "monto": 120000, "region": "Centro"},
    {"producto": "Teclado", "monto": 4800, "region": "Norte"},
    {"producto": "Impresora", "monto": 85000, "region": "Sur"},
    {"producto": "Pendrive", "monto": 2500, "region": "Centro"},
    {"producto": "Tablet", "monto": 210000, "region": "Norte"},
    {"producto": "Auriculares", "monto": 25000, "region": "Sur"},
    {"producto": "Webcam", "monto": 32000, "region": "Centro"},
]


def generar_reporte(ventas_procesadas):
    """Generador que produce, una por una, las líneas del reporte."""
    yield "=" * 50
    yield f"{'PRODUCTO':<15}{'REGIÓN':<12}{'MONTO c/desc.':>20}"
    yield "-" * 50
    for venta in ventas_procesadas:
        yield f"{venta['producto']:<15}{venta['region']:<12}{venta['monto']:>20,.2f}"
    yield "=" * 50


@mide_tiempo
def procesar_ventas(ventas):
    # 1) Filtrar ventas significativas (monto > $5000)
    significativas = list(filter(lambda v: v["monto"] > 5000, ventas))

    # 2) Aplicar 5% de descuento a cada venta filtrada
    con_descuento = list(map(lambda v: {**v, "monto": v["monto"] * 0.95}, significativas))

    # 3) Total facturado por región (comprensión de diccionario)
    regiones = {v["region"] for v in con_descuento}
    total_por_region = {
        region: sum(v["monto"] for v in con_descuento if v["region"] == region)
        for region in sorted(regiones)
    }

    # 4) Reporte línea por línea con el generador
    for linea in generar_reporte(con_descuento):
        print(linea)

    return total_por_region


totales = procesar_ventas(ventas)

print("\nTotal facturado por región:")
for region, total in totales.items():
    print(f"  {region}: ${total:,.2f}")
