"""Comprueba casos límite y contrasta resultados con oráculos conocidos."""
import random
from algoritmos import seleccion, merge_sort, busqueda_lineal, busqueda_binaria


def verificar():
    generador = random.Random(7)
    casos = [[], [5], [2, 1], [3, 3, 3], [-4, 0, -4, 8],
             list(range(30)), list(range(30, -1, -1))]
    casos += [[generador.randint(-20, 20) for _ in range(n)] for n in range(70)]
    for datos in casos:
        esperado = sorted(datos)
        assert seleccion(list(datos)) == esperado
        assert merge_sort(datos) == esperado
        for funcion in (busqueda_lineal, busqueda_binaria):
            for objetivo in range(-22, 23):
                indice = funcion(esperado, objetivo)
                if objetivo in esperado:
                    assert 0 <= indice < len(esperado) and esperado[indice] == objetivo
                else:
                    assert indice == -1
    print(f'Correcto: {len(casos)} listas; ambos ordenamientos y ambas busquedas.')


if __name__ == '__main__':
    verificar()
