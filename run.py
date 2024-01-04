import search
import time

problems = [
    ('Camino de A a B', search.GPSProblem('A', 'B', search.romania)),
    ('Camino de O a E', search.GPSProblem('O', 'E', search.romania)),
    ('Camino de G a Z', search.GPSProblem('G', 'Z', search.romania)),
    ('Camino de N a D', search.GPSProblem('N', 'D', search.romania)),
    ('Camino de M a F', search.GPSProblem('M', 'F', search.romania))
]

for title, problem in problems:
    print(f'\n\033[1m{title}\033[0m')
    start_time = time.time()
    
    print('\nBúsqueda en anchura')
    result = search.breadth_first_graph_search(problem).path()
    elapsed_time = time.time() - start_time
    print(result)
    print(f"Tiempo de ejecución: {elapsed_time:.10f} seconds.")

    print('\nBúsqueda en profundidad')
    start_time = time.time()
    result = search.depth_first_graph_search(problem).path()
    elapsed_time = time.time() - start_time
    print(result)
    print(f"Tiempo de ejecución: {elapsed_time:.10f} seconds.")

    print('\nBúsqueda de ramificación y salto')
    start_time = time.time()
    result = search.ramificacion_salto(problem).path()
    elapsed_time = time.time() - start_time
    print(result)
    print(f"Tiempo de ejecución: {elapsed_time:.10f} seconds.")

    print('\nBúsqueda de ramificación y salto con subestimación')
    start_time = time.time()
    result = search.ramificacion_salto_acotacion(problem).path()
    elapsed_time = time.time() - start_time
    print(result)
    print(f"Tiempo de ejecución: {elapsed_time:.10f} seconds.")

    print('\n-------------------------------------------------------------------------')
