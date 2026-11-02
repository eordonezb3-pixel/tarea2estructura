from datetime import date
from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()


def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f'  Debe ser mayor o igual a {minimo}.')
                continue
            return valor
        except ValueError:
            print('  Debe ser un número entero.')


def leer_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print('  Este campo no puede estar vacío.')


def leer_fecha():
    while True:
        valor = leer_texto('  Fecha de vuelo (AAAA-MM-DD): ')
        try:
            date.fromisoformat(valor)
            return valor
        except ValueError:
            print('  Fecha inválida. Utiliza AAAA-MM-DD.')


def leer_pasajero():
    numero = leer_entero('  N.º de pasajero: ', 1)
    nombre = leer_texto('  Nombre: ')
    cedula = leer_texto('  Cédula: ')
    edad = leer_entero('  Edad: ', 0)
    fecha = leer_fecha()
    destino = leer_texto('  Destino: ')
    asiento = leer_texto('  Asiento: ').upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def cargar_datos_prueba(lista):
    datos = (
        (1005, 'Diana', '0923456789', 22, '2026-11-15', 'Quito', '12A'),
        (1002, 'Ana', '0912345678', 28, '2026-11-15', 'Lima', '03C'),
        (1009, 'Luis', '0987654321', 35, '2026-11-20', 'Bogotá', '18F'),
        (1004, 'Beto', '0934567890', 16, '2026-11-20', 'Quito', '07B'),
        (1001, 'Elena', '0901234567', 41, '2026-11-22', 'Lima', '01A'),
    )
    agregados = 0
    for valores in datos:
        if lista.añadir(Pasajero(*valores)):
            agregados += 1
    print(f'  ✓ {agregados} pasajeros cargados; total: {lista.longitud()}')
####

def mostrar_opciones(titulo, extras=False):
    print(f'\n========== {titulo} ==========')
    print(' 1. Añadir           2. Listar            3. Insertar en posición')
    print(' 4. Buscar (lineal)  5. Buscar (binaria)  6. Modificar')
    print(' 7. Eliminar por posición                 8. Eliminar por número')
    print(' 9. Ordenar asc     10. Ordenar desc     11. Reversar')
    print('12. Copiar          13. Longitud')
    if extras:
        print('14. Filtrar por destino                  15. Mayores de edad')
    print(' C. Cargar datos de prueba                0. Volver')


def mostrar_encontrado(lista, posicion):
    if posicion == -1:
        print('  No existe')
    elif isinstance(lista, MiLista):
        print(f'  Encontrado en [{posicion}]: {lista.datos[posicion]}')
    else:
        print(f'  Encontrado en [{posicion}]: {lista.pasajeros[posicion]}')


def esta_ordenada_asc(lista):
    # La búsqueda binaria requiere orden ascendente.
    anterior = None
    if isinstance(lista, MiLista):
        for i in range(lista.cantidad):
            actual = lista.datos[i].numero
            if anterior is not None and actual < anterior:
                return False
            anterior = actual
    else:
        for p in lista.pasajeros:
            if anterior is not None and p.numero < anterior:
                return False
            anterior = p.numero
    return True


def ejecutar_menu(lista, titulo, extras=False):
    while True:
        mostrar_opciones(titulo, extras)
        op = input('Opción: ').strip().upper()
        if op == '0':
            break
        elif op == 'C':
            cargar_datos_prueba(lista)
        elif op == '1':
            p = leer_pasajero()
            print('  ✓ Pasajero añadido' if lista.añadir(p) else '  ⚠ Número duplicado o lista llena')
        elif op == '2':
            lista.listar()
        elif op == '3':
            pos = leer_entero('  Posición: ')
            if pos < 0 or pos > lista.longitud():
                print('  ⚠ Posición fuera de rango')
                continue
            p = leer_pasajero()
            print('  ✓ Insertado' if lista.insertar(pos, p) else '  ⚠ Número duplicado o lista llena')
        elif op == '4':
            numero = leer_entero('  Número a buscar: ')
            mostrar_encontrado(lista, lista.buscar(numero))
        elif op == '5':
            if not esta_ordenada_asc(lista):
                print('  ⚠ Primero ordena ascendentemente (opción 9).')
                continue
            numero = leer_entero('  Número a buscar: ')
            mostrar_encontrado(lista, lista.buscar_binaria(numero))
        elif op == '6':
            numero = leer_entero('  Número a modificar: ')
            if lista.buscar(numero) == -1:
                print('  No existe')
                continue
            destino = leer_texto('  Nuevo destino: ')
            asiento = leer_texto('  Nuevo asiento: ').upper()
            print('  ✓ Modificado' if lista.modificar(numero, destino, asiento) else '  No existe')
        elif op == '7':
            pos = leer_entero('  Posición a eliminar: ')
            eliminado = lista.eliminar_por_posicion(pos)
            print(f'  ✓ Eliminado: {eliminado}' if eliminado is not None else '  ⚠ Posición fuera de rango')
        elif op == '8':
            numero = leer_entero('  Número a eliminar: ')
            print('  ✓ Eliminado' if lista.eliminar_por_valor(numero) else '  No existe')
        elif op == '9':
            lista.ordenar_asc()
            print('  ✓ Orden ascendente:')
            lista.listar()
        elif op == '10':
            lista.ordenar_desc()
            print('  ✓ Orden descendente:')
            lista.listar()
        elif op == '11':
            lista.reversar()
            print('  ✓ Lista reversada:')
            lista.listar()
        elif op == '12':
            copia = lista.copiar()
            print('  Copia original:')
            copia.listar()
            copia.reversar()
            print('  Copia reversada:')
            copia.listar()
            print('  Lista original (sin cambios):')
            lista.listar()
        elif op == '13':
            print(f'  Longitud: {lista.longitud()}')
        elif op == '14' and extras:
            destino = leer_texto('  Destino a filtrar: ')
            resultados = lista.filtrar_por_destino(destino)
            if not resultados:
                print('  Sin coincidencias')
            for p in resultados:
                print(f'  {p}')
        elif op == '15' and extras:
            resultados = lista.mayores_de_edad()
            if not resultados:
                print('  Sin coincidencias')
            for p in resultados:
                print(f'  {p}')
        else:
            print('  Opción no válida')


def menu_lista1():
    ejecutar_menu(lista1, 'MENÚ 1 · MiLista')


def menu_lista2():
    ejecutar_menu(lista2, 'MENÚ 2 · list de Python', extras=True)


def main():
    while True:
        print('\n===== TAREA LISTAS · PASAJEROS ✈ =====')
        print('1. Menú 1 · MiLista')
        print('2. Menú 2 · list de Python')
        print('3. Salir')
        op = input('Opción: ').strip()
        if op == '1':
            menu_lista1()
        elif op == '2':
            menu_lista2()
        elif op == '3':
            print('¡Hasta pronto!')
            break
        else:
            print('Opción no válida')


if __name__ == '__main__':
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print('\nPrograma finalizado.')
