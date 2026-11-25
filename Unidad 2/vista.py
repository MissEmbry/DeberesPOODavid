class Vista_platillos:
    def mostrar_menu(self):
        print()
        print("MENÚ")
        print("1. Registrar plato")
        print("2. Mostrar platos")
        print("3. Servir platos")
        print("4. Salir")
        return input("Seleccione una opción: ").strip()

    def mostrar_mensaje(self, texto):
        print(texto)

    def mostrar_error(self, texto):
        print(f"Error: {texto}")

    def mostrar_platos(self, platos):
        print("Código  Nombre                  Precio            Porciones")
        for p in platos:
            print(p)

    def pedir_dato(self, mensaje):
        return input(mensaje)