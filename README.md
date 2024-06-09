# PRÁCTICA 1: ALGORITMOS DE BÚSQUEDA

![DALL·E 2024-01-11 18 14 21 - Create a more colorful image for a GitHub README for a Python project, focusing on designing various search algorithms to find different paths to a sp](https://github.com/raquelaq/AlgoritmosDeBusqueda/assets/117348659/9b4ecb1d-084b-44b9-9288-0cec42016bc3)


## Resumen del Proyecto
Este proyecto, desarrollado en el marco de la asignatura Fundamentos de los Sistemas Inteligentes, está titulado "Algoritmos de Búsqueda". Consiste en la implementación de diversos algoritmos de búsqueda utilizando el mapa de las ciudades de Rumanía, con el objetivo de encontrar la ruta más óptima entre ciudades según diferentes enfoques algorítmicos.

## Estructura
El proyecto está formado por tres archivos de Python, cada uno con una función específica:

- **run.py**: ejecuta los distintos métodos de búsqueda en grafos sobre el mapa de las ciudades de Rumanía.
- **search.py**: aquí se implementan los algoritmos de búsqueda en grafos. Incluye clases para definir problemas de búsqueda (Problem), nodos en un árbol de búsqueda (Node) y métodos para realizar diversas búsquedas. Además, contiene una estructura para representar grafos y una adaptación específica para el problema de las ciudades de Rumanía.
- **utils.py**: contiene estructuras de datos y funciones auxiliares para implementar algoritmos de búsqueda, así como otras operaciones matemáticas y estadísticas. Incluye definiciones para manejar diccionarios, colas (como pilas y colas FIFO), funciones para manipulación de secuencias y estadísticas, y una implementación básica de colas ordenadas para algoritmos de búsqueda.

## Tabla Comparativa de los Algoritmos de Búsqueda
<img width="630" alt="image" src="https://github.com/raquelaq/AlgoritmosDeBusqueda/assets/117348659/66ea5dea-df17-4e02-9a27-5fbe70419f06">
<img width="629" alt="image" src="https://github.com/raquelaq/AlgoritmosDeBusqueda/assets/117348659/14ef2998-2dac-4144-b4fd-6d968edeb04a">

## Descripción de Algoritmos
### SortedQueue
Esta función consiste en una cola FIFO que se utiliza para implementar algoritmos de búsqueda ordenada. Se ordena automáticamente en función del coste del camino (path_cost).
### SortedHQueue
Es similar a SortedQueue, pero incluye una heurística en su ordenación. 

## Bibliografía
- chat.openai.com
- PDF's Explicativos de la asignatura "Fundamentos de los Sistemas Inteligentes" de la ULPGC.
- Código base entregado por los profesores de la asignatura.
- https://www.youtube.com/watch?v=vz4Bo1MfhTM
  
## Autores
- Raquel Almeida Quesada
- Jorge Morales Llerandi
