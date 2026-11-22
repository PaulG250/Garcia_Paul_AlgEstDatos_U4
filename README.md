# Laboratorio de eficiencia - Unidad 4

**Paul Garcia** · Algoritmos y Estructuras de Datos · Calificación de la actividad: 9 puntos.

Repositorio: https://github.com/PaulG250/Garcia_Paul_AlgEstDatos_U4

## Ejecución

Se necesita Python 3.8 o posterior. El programa utiliza únicamente la biblioteca
estándar y no necesita instalar paquetes.

```console
python verificar.py
python main.py
```

En Windows también puede usarse `py` si Python está instalado con ese lanzador.
La ejecución completa puede tomar algunos minutos por selección y las repeticiones.
`main.py` muestra la tabla de los cuatro algoritmos y sobrescribe `resultados.csv`
con tiempos, razones y las cinco muestras de cada medición. Los tiempos cambian
según el equipo y su carga. El PDF conserva la ejecución usada para el informe;
una nueva ejecución no actualiza automáticamente ese PDF.

## Algoritmos y método

- Selección: Θ(n²), espacio auxiliar O(1), modifica la lista recibida.
- Merge Sort: Θ(n log n), espacio auxiliar O(n), devuelve una nueva lista.
- Búsqueda lineal: peor caso Θ(n), espacio auxiliar O(1).
- Búsqueda binaria iterativa: peor caso O(log n), espacio auxiliar O(1).

Tamaños: 1.000, 2.000, 4.000 y 8.000. Se generan enteros positivos entre 1 y
1.000.000 con `random.Random(42)`. Ambos ordenamientos reciben copias de los
mismos datos. Se usa `time.perf_counter()` y la mediana de cinco repeticiones.
Las copias y las verificaciones quedan fuera del intervalo medido.

Ambas búsquedas usan la misma lista ordenada con nuestro Merge Sort, cuyo coste
no se incluye en la búsqueda. Se consulta -1 (ausente) para controlar el caso
estudiado: recorrido completo en lineal y reducción sucesiva en binaria.
Cada muestra de búsqueda realiza 2.000 consultas y divide el tiempo por 2.000.
El tiempo incluye el pequeño coste del bucle y la llamada, sin restarlo. El lote
reduce el ruido del reloj, pero no elimina costes fijos ni interferencias del sistema.

La razón es `tiempo_actual / tiempo_del_tamaño_anterior` para cada algoritmo;
el primer tamaño no tiene razón. Se esperan ≈4, ≈2,2, ≈2 y ≈1,1 respectivamente.
Estas razones son referencias de crecimiento, no valores exactos garantizados.

## Archivos

- `analisis_previo.txt`: R1 escrito y registrado en Git antes de medir, sin cambios posteriores.
- `algoritmos.py`: implementaciones y complejidades.
- `main.py`: medición, tabla y exportación de muestras.
- `verificar.py`: validación con listas vacías, repetidos, negativos, listas ordenadas,
  inversas y aleatorias; búsquedas presentes y ausentes.
- `resultados.csv`: mediciones reales de la ejecución del informe.
- `resultados_primera_ejecucion.csv`: primera corrida conservada para documentar
  las variaciones del entorno. La tabla del informe usa la segunda corrida completa.
- `entorno_medicion.txt`: versión de Python y sistema usado en las mediciones.
- `informe.txt`: contenido del informe en formato editable.

La Tabla 16 de la Clase 12, facilitada después de medir, confirma las predicciones
de R1: O(n²) ≈4; O(n log n) algo más de 2; O(n) ≈2; O(log n) apenas mayor que 1.

