import csv
import os


def registrar_venta():
    venta = {
        'id_producto': input('ID del producto: '),
        'celular': input('Celular del cliente: '),
        'cantidad': input('Cantidad: '),
        'precio_venta': input('Precio de venta: '),
        'fecha_pedido': input('Fecha del pedido (YYYY-MM-DD): ')
    }
    return venta


def main():
    archivo_existe = os.path.isfile('ventas.csv')
    with open('ventas.csv', 'a', newline='', encoding='utf-8') as csvfile:
        campos = ['id_producto', 'celular', 'cantidad', 'precio_venta', 'fecha_pedido']
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        if not archivo_existe:
            writer.writeheader()

        while True:
            venta = registrar_venta()
            writer.writerow(venta)
            mas = input('¿Registrar otra venta? (s/n): ')
            if mas.lower() != 's':
                break


if __name__ == '__main__':
    main()
