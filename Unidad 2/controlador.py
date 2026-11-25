class Controlador_platillos:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def leer_texto(self, mensaje):
        while True:
            texto = self.vista.pedir_dato(mensaje).strip()
            if texto != "":
                return texto
            self.vista.mostrar_error("el campo no puede estar vacío.")

    def leer_entero(self, mensaje, minimo=None):
        while True:
            try:
                valor = int(self.vista.pedir_dato(mensaje))
            except ValueError:
                self.vista.mostrar_error("ingrese solo números enteros.")
                continue
            if minimo is not None and valor < minimo:
                self.vista.mostrar_error(f"el valor debe ser mayor o igual a {minimo}.")
                continue
            return valor

    def leer_decimal(self, mensaje):
        while True:
            try:
                valor = float(self.vista.pedir_dato(mensaje).replace(",", "."))
            except ValueError:
                self.vista.mostrar_error("ingrese solo números, por ejemplo 1.25.")
                continue
            if valor <= 0 or valor > 1000000:
                self.vista.mostrar_error("el valor debe ser mayor que cero.")
                continue
            return valor

    def registrar_plato(self):
        nombre = self.leer_texto("Nombre: ")
        precio = self.leer_decimal("Precio: ")
        porciones = self.leer_entero("Porciones: ", 0)
        plato = self.modelo.registrar(nombre, precio, porciones)
        self.vista.mostrar_mensaje(f"Registrado con el código {plato.codigo}.")

    def mostrar_platos(self):
        self.vista.mostrar_platos(self.modelo.listar())

    def servir_plato(self):
        codigo = self.leer_entero("Código: ")
        plato = self.modelo.buscar(codigo)
        if plato is None:
            self.vista.mostrar_error("no existe ese código.")
            return
        cantidad = self.leer_entero("Cantidad: ")
        try:
            plato.servir(cantidad)
            self.vista.mostrar_mensaje(f"Listo. Quedan {plato.porciones} porciones.")
        except ValueError as e:
            self.vista.mostrar_error(str(e))

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()

            if opcion == "1":
                self.registrar_plato()
            elif opcion == "2":
                self.mostrar_platos()
            elif opcion == "3":
                self.servir_plato()
            elif opcion == "4":
                self.vista.mostrar_mensaje("Programa finalizado.")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida.")
