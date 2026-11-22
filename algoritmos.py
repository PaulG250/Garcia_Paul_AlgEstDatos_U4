"""Algoritmos de la Unidad 4, implementados sin bibliotecas externas."""


def seleccion(datos):
    """Ordena in situ. Tiempo Θ(n²), espacio auxiliar O(1)."""
    for i in range(len(datos) - 1):
        minimo = i
        for j in range(i + 1, len(datos)):
            if datos[j] < datos[minimo]:
                minimo = j
        datos[i], datos[minimo] = datos[minimo], datos[i]
    return datos


def merge_sort(datos):
    """Devuelve una lista ordenada. Tiempo Θ(n log n), espacio O(n)."""
    if len(datos) <= 1:
        return list(datos)
    mitad = len(datos) // 2
    izquierda = merge_sort(datos[:mitad])
    derecha = merge_sort(datos[mitad:])
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def busqueda_lineal(datos, objetivo):
    """Índice o -1. Mejor Θ(1), promedio/peor Θ(n); espacio O(1)."""
    for indice, valor in enumerate(datos):
        if valor == objetivo:
            return indice
    return -1


def busqueda_binaria(datos, objetivo):
    """Exige datos ordenados. Mejor Θ(1), peor O(log n); espacio O(1)."""
    izquierda, derecha = 0, len(datos) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if datos[medio] == objetivo:
            return medio
        if datos[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
