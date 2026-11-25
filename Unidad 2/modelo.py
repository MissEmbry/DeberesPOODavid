class Plato:
    def __init__(self, codigo, nombre, precio, porciones):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.porciones = porciones

    def servir(self, cantidad):
        if cantidad <= 0:
            raise ValueError("la cantidad debe ser mayor que cero.")
        if cantidad > self.porciones:
            raise ValueError(f"solo hay {self.porciones} porciones.")
        self.porciones -= cantidad

    def __str__(self):
        return f"{self.codigo:<8}{self.nombre:<24}{self.precio:<18.2f}{self.porciones:<14}"


class Lista_platos:
    def __init__(self):
        self.lista = []
        self.siguiente_codigo = 1
        self.registrar("Mote pillo", 3.50, 30)
        self.registrar("Hornado", 6.00, 20)

    def registrar(self, nombre, precio, porciones):
        plato = Plato(self.siguiente_codigo, nombre, precio, porciones)
        self.lista.append(plato)
        self.siguiente_codigo += 1
        return plato

    def buscar(self, codigo):
        for plato in self.lista:
            if plato.codigo == codigo:
                return plato
        return None

    def listar(self):
        return self.lista
