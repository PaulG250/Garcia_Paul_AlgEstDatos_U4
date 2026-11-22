"""Laboratorio reproducible. Ejecutar: python main.py."""

import random
import time

from algoritmos import seleccion, merge_sort, busqueda_lineal, busqueda_binaria

TAMANOS = (1000, 2000, 4000, 8000)
REPETICIONES = 5
CONSULTAS = 2000
SEMILLA = 42


def mediana(valores):
    return sorted(valores)[len(valores) // 2]


def medir_ordenamiento(funcion, datos):
    muestras = []
    esperado = sorted(datos)  # Oráculo de validación; fuera del cronómetro.
    for _ in range(REPETICIONES):
        copia = list(datos)
        inicio = time.perf_counter()
        resultado = funcion(copia)
        muestras.append(time.perf_counter() - inicio)
        if resultado != esperado:
            raise RuntimeError('Ordenamiento incorrecto: ' + funcion.__name__)
    return mediana(muestras), muestras


def medir_busqueda(funcion, datos):
    muestras = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for _ in range(CONSULTAS):
            resultado = funcion(datos, -1)
        muestras.append((time.perf_counter() - inicio) / CONSULTAS)
        if resultado != -1:
            raise RuntimeError('Búsqueda incorrecta: ' + funcion.__name__)
    return mediana(muestras), muestras


def ejecutar():
    generador = random.Random(SEMILLA)
    filas = []
    anteriores = {}
    for n in TAMANOS:
        datos = [generador.randint(1, 10**6) for _ in range(n)]
        ordenados = merge_sort(datos)  # Preparación excluida de las búsquedas.
        for nombre, funcion in [('Seleccion', seleccion), ('Merge Sort', merge_sort),
                                ('Lineal', busqueda_lineal), ('Binaria', busqueda_binaria)]:
            if nombre in ('Seleccion', 'Merge Sort'):
                tiempo, muestras = medir_ordenamiento(funcion, datos)
            else:
                tiempo, muestras = medir_busqueda(funcion, ordenados)
            razon = tiempo / anteriores[nombre] if nombre in anteriores else None
            filas.append((nombre, n, tiempo, razon, muestras))
            anteriores[nombre] = tiempo
        print('Medido n =', n, flush=True)
    return filas


def guardar_y_mostrar(filas):
    print('\nMedianas de 5 repeticiones. Busquedas: segundos por consulta.')
    print(f"{'Algoritmo':<12} {'n':>6} {'Tiempo (s)':>14} {'Razon':>8}")
    with open('resultados.csv', 'w', encoding='utf-8') as archivo:
        archivo.write('algoritmo,n,tiempo_s,razon,muestra1_s,muestra2_s,muestra3_s,muestra4_s,muestra5_s\n')
        for nombre, n, tiempo, razon, muestras in filas:
            texto = '-' if razon is None else f'{razon:.3f}'
            print(f'{nombre:<12} {n:>6} {tiempo:>14.9f} {texto:>8}')
            razon_csv = '' if razon is None else f'{razon:.9f}'
            archivo.write(f'{nombre},{n},{tiempo:.12f},{razon_csv},' +
                          ','.join(f'{t:.12f}' for t in muestras) + '\n')
    print('\nResultados y muestras guardados en resultados.csv')


if __name__ == '__main__':
    guardar_y_mostrar(ejecutar())
