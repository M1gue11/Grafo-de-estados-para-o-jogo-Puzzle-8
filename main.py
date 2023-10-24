# Miguel Angelus Araruna de Aquino
# Bruno Mikmenta

from models import Grafo, Cfg
import itertools

# Main #

pecas = [1,2,3,4,0,5,6,7,8]#[0, 1, 2, 3, 4, 5, 6, 7, 8]

permutacoes_tuplas = list(itertools.permutations(pecas))

no = Cfg(pecas)
movimentos = no.movimentos_validos()
print(no.to_string())
print(movimentos)

for movimento_idx in permutacoes_tuplas:
    no = Cfg(tupla)
    movimentos = no.movimentos_validos()



