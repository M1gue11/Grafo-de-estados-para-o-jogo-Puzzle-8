from models import Grafo, Cfg
# Main com testes #

teste1 = Cfg([1,2,3,4,5,6,7,8,0])

teste2 = Cfg([8,7,6,5,4,3,2,1,0])

grafo = Grafo()
grafo.adicionar_no(teste1)
grafo.adicionar_no(teste2)
grafo.adicionar_aresta(teste1, teste2)

print(grafo.get_id_by_cfg(teste2))

# print(grafo.grafo)
# print(grafo._cfg_map)
# print(grafo._cfg_id_vet)


