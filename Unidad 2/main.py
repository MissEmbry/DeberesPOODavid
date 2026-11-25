from modelo import Lista_platos
from vista import Vista_platillos
from controlador import Controlador_platillos

modelo = Lista_platos()
vista = Vista_platillos()
controlador = Controlador_platillos(modelo, vista)
controlador.ejecutar()