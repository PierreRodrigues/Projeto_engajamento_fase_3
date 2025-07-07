📊 Projeto Unificado - Fase 3: Análise de Engajamento de Mídias Globo com Estruturas de Dados

👥 Integrantes

Pierre
Maria
Beatriz
Nando

🎯 Objetivo

Aplicar os princípios fundamentais de Algoritmos e Estruturas de Dados na análise de engajamento de conteúdos da Globo, 
utilizando Fila, Árvore de Busca Binária e algoritmos de Ordenação (Quick Sort, Insertion Sort, Merge Sort) 
para organizar e processar dados de forma eficiente.

📁 Estrutura do Projeto

projeto_engajamento_fase_3/
│
├── main.py # Orquestrador principal
├── interacoes_globo.csv # Arquivo com interações brutas

├── entidades/ # Entidades do domínio
│   ├── conteudo.py # Classes Conteudo, Video, Podcast, Artigo
│   ├── interacao.py # Classe Interacao
│   ├── plataforma.py # Classe Plataforma
│   └── usuario.py  # Classe Usuario
│
├── estruturas_dados/ # Estruturas de dados
│   ├── fila.py # Implementação da Fila (FIFO)
│   └── arvore_binaria_busca.py # Implementação da Árvore de Busca Binária
│
├── analise/ # Módulo de análise e relatórios
│   └── sistema.py # SistemaAnaliseEngajamento: análise e ordenação
│
└── ordenacao/
    └── ordenacao.py # Algoritmos de ordenação: quick, merge e insertion

    
🧠 Estruturas Utilizadas

🔁 Fila (Queue)
Utilizada para leitura e processamento sequencial das linhas do CSV (First-In, First-Out).

Operações:

enfileirar(linha_csv)
desenfileirar()
esta_vazia()

🌳 Árvores de Busca Binária (BST)

Utilizadas para armazenar e recuperar eficientemente dados de Conteudo e Usuario.

Árvore de Conteúdos

Chave: _id_conteudo

Operações:

inserir_conteudo(conteudo)
buscar_conteudo(id)
remover_conteudo(id)
percurso_em_ordem()
Árvore de Usuários
Chave: _id_usuario

Operações análogas à árvore de conteúdos.

🧮 Algoritmos de Ordenação

Quick Sort: usado como padrão para listas grandes.
Insertion Sort: utilizado em listas pequenas (ex: resultados já quase ordenados).
Merge Sort: alternativa híbrida eficiente para casos intermediários.
Todos os algoritmos permitem ordenação por métrica (ex: calcular_total_interacoes)
ou por função chave (key_func), além de suporte para ordenação reversa (descendente).

📊 Relatórios Gerados

1. Ranking de Conteúdos Mais Consumidos
Ordenados por tempo total de consumo (watch_duration_seconds).

3. Usuários com Maior Tempo Total de Consumo
Soma do tempo de consumo em todas as interações.

5. Plataformas com Maior Engajamento
Interações do tipo view_start, like, share, comment agrupadas por plataforma.

7. Conteúdos Mais Comentados
Ranking de conteúdos com maior número de interações do tipo comment.

9. Total de Interações por Tipo de Conteúdo
Agrupamento por conteúdo e total de interações recebidas.

11. Tempo Médio de Consumo por Plataforma
Média dos tempos de consumo agrupados por plataforma.

13. Quantidade de Comentários por Conteúdo
Lista com os conteúdos e quantidade de comentários registrados.

⚙️ Execução

Coloque o arquivo interacoes_globo.csv na raiz do projeto.

Execute o projeto com:

python main.py
Acompanhe o processamento e geração de relatórios diretamente no terminal.

📈 Complexidade dos Algoritmos

Cada método implementado está documentado com suas análises de complexidade:

Fila:

Enfileirar/Desenfileirar → O(1)

Árvore BST:
Inserção/Busca/Remoção → O(log n) em média, O(n) no pior caso

Quick Sort:
Média → O(n log n)
Pior caso → O(n²)
Insertion Sort:
Melhor caso (quase ordenado) → O(n)
Pior caso → O(n²)

Merge Sort:
Sempre → O(n log n)


✅ Conclusão

O projeto integra os conceitos de estruturas de dados e algoritmos de ordenação aplicados à análise real de dados de engajamento. 
A escolha criteriosa das estruturas permitiu ganhos de performance no acesso, organização e visualização dos dados de forma eficiente e escalável.
