from pasajero import Pasajero


class MiLista:
    """Lista de capacidad fija, con operaciones implementadas manualmente."""
    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def añadir(self, pasajero):
        if self.cantidad == self.capacidad or self.buscar(pasajero.numero) != -1:
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad += 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print('  (lista vacía)')
        for i in range(self.cantidad):
            print(f'  [{i}] {self.datos[i]}')

    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > self.cantidad or self.cantidad == self.capacidad:
            return False
        if self.buscar(pasajero.numero) != -1:
            return False
        i = self.cantidad
        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i -= 1
        self.datos[posicion] = pasajero
        self.cantidad += 1
        return True

    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def buscar_binaria(self, numero):
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.datos[medio].numero == numero:
                return medio
            if self.datos[medio].numero < numero:
                izq = medio + 1
            else:
                der = medio - 1
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            return None
        eliminado = self.datos[posicion]
        i = posicion
        while i < self.cantidad - 1:
            self.datos[i] = self.datos[i + 1]
            i += 1
        self.cantidad -= 1
        self.datos[self.cantidad] = None
        return eliminado

    def eliminar_por_valor(self, numero):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.eliminar_por_posicion(pos)
        return True

    def ordenar_asc(self):
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero > self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def ordenar_desc(self):
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero < self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def reversar(self):
        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq += 1
            der -= 1

    def copiar(self):
        nueva = MiLista(self.capacidad)
        for i in range(self.cantidad):
            p = self.datos[i]
            nueva.añadir(Pasajero(p.numero, p.nombre, p.cedula, p.edad,
                                  p.fecha_vuelo, p.destino, p.asiento))
        return nueva

    def longitud(self):
        return self.cantidad
