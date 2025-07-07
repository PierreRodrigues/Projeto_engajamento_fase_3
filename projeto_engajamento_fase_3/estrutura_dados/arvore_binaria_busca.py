class NoArvore:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.esquerda = None
        self.direita = None
 
class ArvoreBinariaBusca:
    def __init__(self):
        self._raiz = None
 
    def inserir(self, chave, valor):
        self._raiz = self._inserir_rec(self._raiz, chave, valor)
 
    def _inserir_rec(self, no, chave, valor):
        if no is None:
            return NoArvore(chave, valor)
        if chave < no.chave:
            no.esquerda = self._inserir_rec(no.esquerda, chave, valor)
        elif chave > no.chave:
            no.direita = self._inserir_rec(no.direita, chave, valor)
        return no
 
    def buscar(self, chave):
        return self._buscar_rec(self._raiz, chave)
 
    def _buscar_rec(self, no, chave):
        if no is None:
            return None
        if chave == no.chave:
            return no.valor
        elif chave < no.chave:
            return self._buscar_rec(no.esquerda, chave)
        else:
            return self._buscar_rec(no.direita, chave)
 
    def percurso_em_ordem(self):
        resultado = []
        self._percurso_rec(self._raiz, resultado)
        return resultado
 
    def _percurso_rec(self, no, resultado):
        if no:
            self._percurso_rec(no.esquerda, resultado)
            resultado.append(no.valor)
            self._percurso_rec(no.direita, resultado)