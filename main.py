# Miguel Angelus Araruna de Aquino
# Bruno Miksucas Pimenta

from models import Grafo, No
import itertools
from tqdm import tqdm

# Main #

pecas = (1,2,3,4,5,6,7,8,0)
permutacoes_tuplas = list(itertools.permutations(pecas))
total_nos = len(permutacoes_tuplas)
total_arestas = 0
print('Há', total_nos, 'nós no grafo do espaço de estados')


grafo = Grafo()
for tupla in tqdm(permutacoes_tuplas):
    no = grafo.get_no_by_cfg(tupla)
    if no == None:
        no = No(tupla)

    grafo.adicionar_no(no)
    movimentos = no.movimentos_validos()
    total_arestas += len(movimentos)
    # print(no.to_string())

    for movimento_idx in movimentos:
        novo_estado = no.move_peca(movimento_idx)
        novo_no = grafo.get_no_by_cfg(novo_estado)

        if novo_no == None:
            novo_no = No(novo_estado)

        grafo.adicionar_no(novo_no)
        grafo.adicionar_aresta(no, novo_no)

print('Há', total_arestas, 'arestas no grafo do espaço de estados')
# print(grafo.to_string())
print(grafo.grafo.__len__())

op = input("Digite:")
while(op != "stop"):
    # l = []
    # for c in op:
    #     l.append(int(c))
    estado = int(op)
    no = grafo.get_no_by_id(estado)
    print("No encontrado!", no.to_string())
    for no_id in grafo.grafo[no.id]:
        print(grafo.get_no_by_id(no_id).to_string())

    op = input("Digite:")

L: list[list[No]] = grafo.BFS_alg(grafo.get_no_by_id(0))