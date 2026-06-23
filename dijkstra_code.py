class Grafo:
    def __init__(self):
        self.adjacencias = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = {}

    def adicionar_aresta(self, origem, destino, peso):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.adjacencias[origem][destino] = peso

    def dijkstra(self, inicio, fim):
        menor_distancia = {vertice: float('inf') for vertice in self.adjacencias}
        menor_distancia[inicio] = 0
        antecessor = {vertice: None for vertice in self.adjacencias}
        nao_visitados = list(self.adjacencias.keys())

        while nao_visitados:

            vertice_atual = None
            for v in nao_visitados:
                if vertice_atual is None or menor_distancia[v] < menor_distancia[vertice_atual]:
                    vertice_atual = v
            
            for vizinho, peso in self.adjacencias[vertice_atual].items():
                distancia_alternativa = menor_distancia[vertice_atual] + peso
                if distancia_alternativa < menor_distancia[vizinho]:
                    menor_distancia[vizinho] = distancia_alternativa
                    antecessor[vizinho] = vertice_atual

            nao_visitados.remove(vertice_atual)

        caminho = []
        atual = fim
        while atual is not None:
            caminho.insert(0, atual)
            atual = antecessor[atual]

        return caminho, menor_distancia[fim]

def main():
    
    logistica = Grafo()

    arestas = [
        ('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 5),
        ('B', 'D', 10), ('C', 'E', 3), ('D', 'E', 4), ('E', 'A', 7)
    ]
    
    for o, d, v in arestas:
        logistica.adicionar_aresta(o, d, v)

    print("--- Sistema de Mapeamento de Rotas ---")
    partida = input("Digite o ponto de partida (ex: A): ").upper()
    chegada = input("Digite o ponto de chegada (ex: E): ").upper()

    if partida in logistica.adjacencias and chegada in logistica.adjacencias:
        caminho, custo = logistica.dijkstra(partida, chegada)
        
        if custo != float('inf'):
            print(f"\nCaminho mais curto: {' -> '.join(caminho)}")
            print(f"Custo total: {custo}")
        else:
            print(f"\nNão existe rota entre {partida} e {chegada}.")
    
    else:
        print("\nVértices de partida ou chegada não encontrados no grafo.")

if __name__ == "__main__":
    main()