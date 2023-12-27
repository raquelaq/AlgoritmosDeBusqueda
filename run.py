# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print('\nBreath First Graph Search')
print(search.breadth_first_graph_search(ab).path())  #hace una llamada a la función breadth_first_graph_search (search.breadth_first_graph_search) BUSQUEDA AMPLITUD
print('\nDepth First Graph Search')
print(search.depth_first_graph_search(ab).path()) #BUSQUEDA PROFUNDIDAD

print('\nRAMIFICACIÓN Y SALTO (Búsqueda no informada)')
print(search.ramificacion_salto(ab).path())
print('\nRAMIFICACIÓN Y SALTO CON SUBESTIMACIÓN (Búsqueda informada)')
print(search.ramificacion_salto_acotacion(ab).path())


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
