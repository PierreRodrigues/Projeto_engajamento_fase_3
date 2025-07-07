class Fila:
    def __init__(self):
        self._dados = []
 
    def enfileirar(self, item):
        self._dados.append(item)
 
    def desenfileirar(self):
        if not self.esta_vazia():
            return self._dados.pop(0)
        return None
 
    def esta_vazia(self):
        return len(self._dados) == 0