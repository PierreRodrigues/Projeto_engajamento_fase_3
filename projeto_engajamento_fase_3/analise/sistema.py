from estrutura_dados.fila import Fila
from estrutura_dados.arvore_binaria_busca import ArvoreBinariaBusca
from entidades.plataforma import Plataforma
from entidades.conteudo import Video, Podcast, Artigo
from entidades.usuario import Usuario
from entidades.interacao import Interacao
import csv
 
class SistemaAnaliseEngajamento:
    def __init__(self):
        self._fila_interacoes_brutas = Fila()
        self._arvore_conteudos = ArvoreBinariaBusca()
        self._arvore_usuarios = ArvoreBinariaBusca()
        self._plataformas = {}
 
    def _carregar_interacoes_csv(self, caminho_arquivo):
        with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self._fila_interacoes_brutas.enfileirar(row)
 
    def processar_interacoes(self):
        while not self._fila_interacoes_brutas.esta_vazia():
            linha = self._fila_interacoes_brutas.desenfileirar()
            id_usuario = int(linha['id_usuario'])
            id_conteudo = int(linha['id_conteudo'])
            tipo_conteudo = linha['tipo_conteudo']
            nome_usuario = linha['nome_usuario']
            titulo = linha['titulo']
            plataforma_nome = linha['plataforma']
            tipo_interacao = linha['tipo_interacao']
            tempo_consumo = int(linha.get('tempo_consumo', 0))
 
            if plataforma_nome not in self._plataformas:
                self._plataformas[plataforma_nome] = Plataforma(plataforma_nome)
            plataforma = self._plataformas[plataforma_nome]
 
            conteudo = self._arvore_conteudos.buscar(id_conteudo)
            if not conteudo:
                if tipo_conteudo == 'video':
                    conteudo = Video(id_conteudo, titulo, tipo_conteudo)
                elif tipo_conteudo == 'podcast':
                    conteudo = Podcast(id_conteudo, titulo, tipo_conteudo)
                else:
                    conteudo = Artigo(id_conteudo, titulo, tipo_conteudo)
                self._arvore_conteudos.inserir(id_conteudo, conteudo)
 
            usuario = self._arvore_usuarios.buscar(id_usuario)
            if not usuario:
                usuario = Usuario(id_usuario, nome_usuario)
                self._arvore_usuarios.inserir(id_usuario, usuario)
 
            interacao = Interacao(usuario, conteudo, plataforma, tipo_interacao, tempo_consumo)
 
            plataforma.registrar_interacao(interacao)
            conteudo.registrar_interacao(interacao)
            usuario.registrar_interacao(interacao)
 
    # ----------- Algoritmo Merge Sort -----------
    def merge_sort(self, lista, chave_func):
        if len(lista) <= 1:
            return lista
        meio = len(lista) // 2
        esquerda = self.merge_sort(lista[:meio], chave_func)
        direita = self.merge_sort(lista[meio:], chave_func)
        return self._merge(esquerda, direita, chave_func)
 
    def _merge(self, esquerda, direita, chave_func):
        resultado = []
        i = j = 0
        while i < len(esquerda) and j < len(direita):
            if chave_func(esquerda[i]) > chave_func(direita[j]):
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        return resultado
 
    # ----------- Algoritmo Insertion Sort -----------
    def insertion_sort(self, lista, chave_func):
        for i in range(1, len(lista)):
            atual = lista[i]
            j = i - 1
            while j >= 0 and chave_func(lista[j]) < chave_func(atual):
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = atual
        return lista
 
    # ----------- Relatórios usando Merge Sort -----------
    def gerar_relatorio_top_conteudos(self, n=5):
        conteudos = self._arvore_conteudos.percurso_em_ordem()
        ordenados = self.merge_sort(conteudos, lambda c: c.calcular_tempo_total_consumo())
        print("\nTop Conteúdos por Consumo (Merge Sort):")
        for c in ordenados[:n]:
            print(f"- {c.titulo}: {c.calcular_tempo_total_consumo()}s")
 
    # ----------- Relatórios usando Insertion Sort -----------
    def gerar_relatorio_top_usuarios(self, n=5):
        usuarios = self._arvore_usuarios.percurso_em_ordem()
        ordenados = self.insertion_sort(usuarios, lambda u: u.calcular_tempo_total_consumo())
        print("\nTop Usuários por Consumo (Insertion Sort):")
        for u in ordenados[:n]:
            print(f"- {u.nome}: {u.calcular_tempo_total_consumo()}s")