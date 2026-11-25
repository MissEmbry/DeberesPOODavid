def mostrar_menu():
    print()
    print("MENÚ")
    print("1. Registrar plato")
    print("2. Mostrar platos")
    print("3. Servir platos")
    print("4. Salir")


def pedir_opcion():
    return input("Seleccione una opción: ").strip()


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: el campo no puede estar vacío.")


def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Error: ingrese solo números enteros.")
            continue
        if minimo is not None and valor < minimo:
            print(f"Error: el valor debe ser mayor o igual a {minimo}.")
            continue
        return valor


def leer_decimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje).replace(",", "."))
        except ValueError:
            print("Error: ingrese solo números, por ejemplo 1.25.")
            continue
        if valor <= 0 or valor > 1000000:
            print("Error: el valor debe ser mayor que cero.")
            continue
        return valor


def pedir_datos_plato():
    nombre = leer_texto("Nombre: ")
    precio = leer_decimal("Precio: ")
    porciones = leer_entero("Porciones: ", 0)
    return nombre, precio, porciones


def mostrar_platos(platos):
    print("Código  Nombre                  Precio            Porciones")
    for p in platos:
        print(f"{p.codigo:<8}{p.nombre:<24}{p.precio:<18.2f}{p.porciones:<14}")


def mostrar_mensaje(texto):
    print(texto)