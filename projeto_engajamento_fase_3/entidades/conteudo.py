class Conteudo:
    def __init__(self, id_conteudo, titulo, tipo):
        self._id_conteudo = id_conteudo
        self.titulo = titulo
        self.tipo = tipo
        self._interacoes = []
 
    def registrar_interacao(self, interacao):
        self._interacoes.append(interacao)
 
    def calcular_total_interacoes(self):
        return len(self._interacoes)
 
    def calcular_tempo_total_consumo(self):
        return sum(i.tempo_consumo for i in self._interacoes if i.tempo_consumo)
 
    def contar_comentarios(self):
        return sum(1 for i in self._interacoes if i.tipo_interacao == 'comment')
 
 
class Video(Conteudo):
    pass
 
 
class Podcast(Conteudo):
    pass
 
 
class Artigo(Conteudo):
    pass