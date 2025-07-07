from analise.sistema import SistemaAnaliseEngajamento
 
def main():
    sistema = SistemaAnaliseEngajamento()
    sistema._carregar_interacoes_csv("interacoes_globo.csv")
    sistema.processar_interacoes()
    sistema.gerar_relatorio_top_conteudos()
    sistema.gerar_relatorio_top_usuarios()
 
if __name__ == "__main__":
    main()