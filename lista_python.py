from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Lista de pasajeros utilizando las herramientas nativas de Python."""
    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):
        if self.buscar(pasajero.numero) != -1:
            return False
        self.pasajeros.append(pasajero)
        return True

    def listar(self):
        if not self.pasajeros:
            print('  (lista vacía)')
        for i, p in enumerate(self.pasajeros):
            print(f'  [{i}] {p}')

    def insertar(self, posicion, pasajero):
        if not 0 <= posicion <= len(self.pasajeros) or self.buscar(pasajero.numero) != -1:
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    def buscar(self, numero):
        posiciones = [i for i, p in enumerate(self.pasajeros) if p.numero == numero]
        return posiciones[0] if posiciones else -1

    def buscar_binaria(self, numero):
        numeros = [p.numero for p in self.pasajeros]
        pos = bisect_left(numeros, numero)
        if pos < len(numeros) and numeros[pos] == numero:
            return pos
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.pasajeros[pos].destino = nuevo_destino
        self.pasajeros[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if not 0 <= posicion < len(self.pasajeros):
            return None
        return self.pasajeros.pop(posicion)

    def eliminar_por_valor(self, numero):
        if self.buscar(numero) == -1:
            return False
        self.pasajeros = [p for p in self.pasajeros if p.numero != numero]
        return True

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva = ListaPython()
        nueva.pasajeros = [Pasajero(p.numero, p.nombre, p.cedula, p.edad,
                                   p.fecha_vuelo, p.destino, p.asiento)
                           for p in self.pasajeros.copy()]
        return nueva

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):
        return [p for p in self.pasajeros if p.destino.casefold() == destino.casefold()]

    def mayores_de_edad(self):
        return [p for p in self.pasajeros if p.es_mayor_de_edad()]
