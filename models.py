class Cfg():

    #contador para termos os ids dos estados
    id_cfg = 1

    def incrementa_id():
        Cfg.id_cfg+=1

    def __init__(self, estado: list):
        self.estado = estado
        self.id = Cfg.id_cfg
        Cfg.incrementa_id()

    def to_string(self) -> str:
        string = "[ "
        for i in range(len(self.estado)):
            if i == 2 or i == 5 or i == 8:
                string += f"{self.estado[i]} ]"
                if i < 8:
                    string += "\n[ "
            else:
                string += f"{self.estado[i]}, "
        return f"Id: {self.id} Estado:\n{string}"


class Grafo():

    def __init__(self):
        self.grafo = {}
        self._cfg_map: dict[Cfg, int] = {}
        self._cfg_id_vet: list[Cfg] = []

    def adicionar_no(self, no: Cfg):
        if no.id not in self.grafo:
            self.grafo[no.id] = []
            self._cfg_map[no] = no.id
            self._cfg_id_vet.append(no)
    
    def adicionar_aresta(self, no1: Cfg, no2: Cfg):
        g = self.grafo
        if no1.id not in self.grafo:
            raise Exception(f"Nó id: {no1.id} não está no grafo")
        if no2.id not in self.grafo:
            raise Exception(f"Nó id: {no2.id} não está no grafo")
        if no2 in g[no1.id]:
            raise Exception(f"A aresta já está no grafo")
        
        g[no1.id].append(no2.id)
        g[no2.id].append(no1.id)
    
    def get_cfg_by_id(self, id) -> Cfg:
        return self._cfg_id_vet[id-1]

    def get_id_by_cfg(self, no: Cfg) -> int:
        return self._cfg_map[no]