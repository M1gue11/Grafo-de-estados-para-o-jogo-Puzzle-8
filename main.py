# Miguel Angelus Araruna de Aquino
# Bruno Miksucas Pimenta

from models import Grafo, No
import itertools
from tqdm import tqdm

# Item 1 - Montando o Grafo
pecas = (1,2,3,4,5,6,7,8,0)
permutacoes_tuplas = list(itertools.permutations(pecas))

grafo = Grafo()
for tupla in tqdm(permutacoes_tuplas):
    no = grafo.get_no_by_cfg(tupla)
    if no == None:
        no = No(tupla)

    grafo.adicionar_no(no)
    movimentos = no.movimentos_validos()
    # print(no.to_string())

    for movimento_idx in movimentos:
        novo_estado = no.move_peca(movimento_idx)
        novo_no = grafo.get_no_by_cfg(novo_estado)

        if novo_no == None:
            novo_no = No(novo_estado)

        grafo.adicionar_no(novo_no)
        grafo.adicionar_aresta(no, novo_no)

# print(grafo.to_string())
print('Há', grafo.quantidade_de_nos(), 'nós no grafo do espaço de estados')
print('Há', grafo.quantidade_de_arestas(), 'arestas no grafo do espaço de estados')

# Fim item 1

# Item 2 - Bfs e contando componentes conexos

visitados = set()
id_no_inicio = 1
componentes_conexos = grafo.BFS(visitados, id_no_inicio)
print("Quantidade de nos visitados", len(visitados))
print("Quantidade de componentes conexos", len(componentes_conexos))

for idx, componente in enumerate(componentes_conexos):
    print(f"Componente conexo {idx+1}")
    for idx, layer in enumerate(componente):
        print(f"Layer {idx}:")
        s = ""
        for no in layer:
            s += grafo.get_no_by_id(no).to_string() + "\n"
        print(s)
        

# Fim item 2

# Item 3 - Caminho mais curto

print("No de inicio:", grafo.get_no_by_id(id_no_inicio).to_string())
print(f"No(s) com maior distancia ({len(componentes_conexos[0])-1} passos) para o no de inicio:")
for no in componentes_conexos[0][len(componentes_conexos[0])-1]:
    print(grafo.get_no_by_id(no).to_string())

# Fim item 3

# Testes
# op = input("Digite:")
# while(op != "stop"):
#     # l = []
#     # for c in op:
#     #     l.append(int(c))
#     estado = int(op)
#     no = grafo.get_no_by_id(estado)
#     print("No encontrado!", no.to_string())
#     for no_id in grafo.grafo[no.id]:
#         print(grafo.get_no_by_id(no_id).to_string())

#     op = input("Digite:")