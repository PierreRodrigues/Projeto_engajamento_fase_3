class Usuario:
    def __init__(self, id_usuario, nome):
        self._id_usuario = id_usuario
        self.nome = nome
        self._interacoes = []
 
    def registrar_interacao(self, interacao):
        self._interacoes.append(interacao)
 
    def calcular_tempo_total_consumo(self):
        return sum(i.tempo_consumo for i in self._interacoes if i.tempo_consumo)