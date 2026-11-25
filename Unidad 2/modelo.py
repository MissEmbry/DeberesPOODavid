class Plato:
    def __init__(self, codigo, nombre, precio, porciones):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.porciones = porciones

    def servir(self, cantidad):
        if cantidad <= 0:
            return "cantidad_invalida"
        if cantidad > self.porciones:
            return "insuficiente"
        self.porciones -= cantidad
        return "ok"


class Lista_platos:
    def __init__(self):
        self.listaplatos = []
        self.cargar_datos()

    def cargar_datos(self):
        self.listaplatos.append(Plato(1, "Mote pillo", 3.50, 30))
        self.listaplatos.append(Plato(2, "Hornado", 6.00, 20))

    def registrar_plato(self, nombre, precio, porciones):
        codigo = len(self.listaplatos) + 1
        plato = Plato(codigo, nombre, precio, porciones)
        self.listaplatos.append(plato)
        return plato

    def buscar(self, codigo):
        for plato in self.listaplatos:
            if plato.codigo == codigo:
                return plato
        return None

    def mostrar_lista(self):
        return self.listaplatos