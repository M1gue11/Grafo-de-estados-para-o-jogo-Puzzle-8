class Cfg():

    #contador para termos os ids dos estados
    id_cfg = 1

    def incrementa_id():
        Cfg.id_cfg+=1

    def __init__(self, estado: tuple):
        self.estado = estado
        self.id = Cfg.id_cfg
        Cfg.incrementa_id()

    def movimentos_validos(self) -> list:
        # retorna uma lista com indices das peças que podem ser movimentadas
        index_0 = self.estado.index(0)
        posicoes = [-1, 1, -3, 3]
        ret = []
        for i in range(len(posicoes)):
            if index_0 + posicoes[i] >= 0 and index_0 + posicoes[i] < len(self.estado):
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
        self._cfg_map: dict[tuple, Cfg] = {}
        self._cfg_id_vet: list[Cfg] = []

    def adicionar_no(self, no: Cfg):
        if no.id not in self.grafo:
            self.grafo[no.id] = []
            self._cfg_map[no.estado] = no
            self._cfg_id_vet.append(no)
    
    def adicionar_aresta(self, no1: Cfg, no2: Cfg):
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
    
    def get_no_by_id(self, id) -> Cfg:
        try:
            return self._cfg_id_vet[id-1]
        except:
            # print(f"Id {id} não encontrado!")
            return None

    def get_no_by_cfg(self, estado: tuple) -> Cfg:
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

