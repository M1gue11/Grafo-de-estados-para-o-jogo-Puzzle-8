class No():

    #contador para termos os ids dos estados
    id_cfg = 1

    def incrementa_id():
        No.id_cfg+=1

    def __init__(self, estado: tuple):
        self.estado = estado
        self.id = No.id_cfg
        No.incrementa_id()

    def movimentos_validos(self) -> list:
        # retorna uma lista com indices das peças que podem ser movimentadas
        index_0 = self.estado.index(0)
        posicoes = [-1, 1, -3, 3]
        ret = []
        for i in range(len(posicoes)):
            idx_final = index_0 + posicoes[i]
            if idx_final >= 0 and idx_final < len(self.estado):
                linha_0 = index_0 // 3
                linha_final = idx_final // 3
                # print(f"linha_0: {linha_0} linha_final: {linha_final} posicao[i]: {posicoes[i]}")
                if posicoes[i] in [-1, 1] and linha_0 != linha_final:
                    pass
                else:
                    ret.append(posicoes[i])
        return ret
    
    def move_peca(self, offset: int) -> tuple:
        if offset not in [-1, 1, -3, 3]:
            raise Exception(f"Offset inválido!")
        
        novo_estado = list(self.estado).copy()
        zero_idx = novo_estado.index(0)
        novo_estado[zero_idx], novo_estado[zero_idx + offset] = novo_estado[zero_idx + offset], novo_estado[zero_idx]
        return tuple(novo_estado)

    
    def to_string(self) -> str:
        string = "[ "
        estado_list = list(self.estado)
        for i in range(len(estado_list)):
            num = '-' if estado_list[i] == 0 else estado_list[i]
            if i == 2 or i == 5 or i == 8:
                string += f"{num} ]"
                if i < 8:
                    string += "\n[ "
            else:
                string += f"{num}, "
        return f"Id: {self.id} Estado:\n{string}"


class Grafo():

    def __init__(self):
        self.grafo: dict[int, list[int]] = {}
        self._cfg_map: dict[tuple, No] = {}
        self._cfg_id_vet: list[No] = []

    def adicionar_no(self, no: No):
        if no.id not in self.grafo:
            self.grafo[no.id] = []
            self._cfg_map[no.estado] = no
            self._cfg_id_vet.append(no)
    
    def adicionar_aresta(self, no1: No, no2: No):
        g = self.grafo
        if no1.id not in self.grafo:
            raise Exception(f"Nó id: {no1.id} não está no grafo")
        if no2.id not in self.grafo:
            raise Exception(f"Nó id: {no2.id} não está no grafo")
        
        if no2.id in g[no1.id]:
            # print(f"A aresta {no1.id} -> {no2.id} já está no grafo")
            return
        
        g[no1.id].append(no2.id)
        g[no2.id].append(no1.id)
    
    def get_no_by_id(self, id) -> No:
        try:
            return self._cfg_id_vet[id-1]
        except:
            # print(f"Id {id} não encontrado!")
            return None

    def get_no_by_cfg(self, estado: tuple) -> No:
        try:
            return self._cfg_map[estado]
        except:
            # print(f"Configuração {estado} não encontrada!")
            return None
    
    def to_string(self) -> str:
        s = ""
        for key, value in self.grafo.items():
            if key % 3 == 0 :
                s += "\n"
            s += f"{key} : {value}; "
        return s


    def BFS_alg(self, no: No) -> list:
        L: list[list[No]] = []
        queue: list[No] = []
        visited: list[No] = []

        L.append([])
        L[0].append(no)
        queue.append(no)
        layer = 1
        while queue:
            L.append([])
            current_no = queue.pop(0)
            visited.append(current_no)
            for vizinho in self.grafo[current_no]:
                if vizinho not in visited:
                    queue.append(vizinho)
                    visited.append(vizinho)
                    L[layer].append(vizinho)
            if len(L[layer]) == 0:
                return L
            layer+=1

