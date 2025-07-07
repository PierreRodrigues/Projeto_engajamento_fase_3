class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        self._interacoes = []
 
    def registrar_interacao(self, interacao):
        self._interacoes.append(interacao)
 
    def total_interacoes(self):
        return len(self._interacoes)