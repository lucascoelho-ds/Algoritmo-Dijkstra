# Sistema de Mapeamento de Rotas (Algoritmo de Dijkstra)

Implementação em Python do algoritmo de **Dijkstra** para encontrar o caminho de menor custo entre dois pontos em um grafo direcionado e ponderado — útil para problemas de logística e roteirização.

## Como funciona

### 1. Estrutura do grafo (`Grafo`)

O grafo é representado como um **dicionário de adjacências**, onde cada vértice aponta para outro dicionário com seus vizinhos e o peso (custo) da aresta até eles:

```python
{
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    ...
}
```

- `adicionar_vertice(vertice)`: cria uma entrada para o vértice, caso ainda não exista.
- `adicionar_aresta(origem, destino, peso)`: cria os vértices de origem e destino (se necessário) e registra uma aresta **direcionada** entre eles com o peso informado. Ou seja, uma aresta `A -> B` não implica automaticamente `B -> A`.

### 2. Algoritmo de Dijkstra (`dijkstra`)

Calcula o caminho de menor custo entre um vértice de início e um de fim:

1. Inicializa a distância de todos os vértices como infinita, exceto o vértice inicial (distância 0).
2. A cada iteração, seleciona o vértice não visitado com a menor distância acumulada conhecida.
3. Para cada vizinho desse vértice, verifica se passar por ele resulta em um caminho mais curto do que o já registrado (*relaxamento de arestas*). Se sim, atualiza a distância e guarda o vértice atual como antecessor.
4. Remove o vértice da lista de não visitados e repete até que todos tenham sido processados.
5. Reconstrói o caminho percorrendo os antecessores do vértice final até o inicial.

Retorna uma tupla `(caminho, custo_total)`, onde `caminho` é a lista ordenada de vértices percorridos e `custo_total` é a soma dos pesos das arestas.

> ⚠️ **Nota de implementação**: esta é a versão didática/simplificada do Dijkstra — a busca pelo vértice de menor distância é feita com um laço `for` percorrendo todos os não visitados (complexidade O(V²)), em vez de uma fila de prioridade (`heapq`), que seria mais eficiente (O((V+E) log V)) para grafos grandes.

### 3. Programa principal (`main`)

- Monta um grafo de exemplo com 5 vértices (`A` a `E`) e 7 arestas com pesos fixos, simulando uma malha logística.
- Solicita ao usuário, via terminal, o ponto de partida e o ponto de chegada.
- Valida se ambos os vértices existem no grafo.
- Executa o Dijkstra e exibe o caminho mais curto e o custo total, ou uma mensagem informando que não há rota entre os pontos.

## Como executar

```bash
python nome_do_arquivo.py
```

Exemplo de uso:

```
--- Sistema de Mapeamento de Rotas ---
Digite o ponto de partida (ex: A): A
Digite o ponto de chegada (ex: E): E

Caminho mais curto: A -> C -> E
Custo total: 5
```

## Grafo de exemplo utilizado

| Origem | Destino | Peso |
|--------|---------|------|
| A      | B       | 4    |
| A      | C       | 2    |
| B      | C       | 5    |
| B      | D       | 10   |
| C      | E       | 3    |
| D      | E       | 4    |
| E      | A       | 7    |

Como as arestas são **direcionadas**, por exemplo `E -> A` existe, mas `A -> E` não existe diretamente — o caminho de A até E precisa passar por outro vértice (como `C`).

## Limitações conhecidas

- **Sem tratamento de arestas de peso negativo**: o Dijkstra não funciona corretamente com pesos negativos; o código não valida isso.
- **Sem tratamento de entrada inválida**: se o usuário digitar um vértice que não seja uma letra maiúscula única (ou algo fora do grafo), o programa apenas informa que os vértices não foram encontrados — não há validação mais detalhada.
- **Desempenho O(V²)**: adequado para grafos pequenos (como o exemplo com 5 vértices), mas ineficiente para grafos grandes. Para esses casos, recomenda-se usar `heapq` (fila de prioridade).
- **Grafo fixo no código**: os vértices e arestas estão *hardcoded* em `main()`. Para um uso mais flexível, seria interessante carregar o grafo de um arquivo externo (CSV, JSON) ou permitir que o usuário cadastre arestas interativamente.

## Possíveis melhorias

- Implementar a versão otimizada com `heapq` para grafos maiores.
- Permitir carregar o grafo a partir de um arquivo de configuração.
- Adicionar suporte a grafos não direcionados (aresta bidirecional automática).
- Validar entradas do usuário (verificar se é uma única letra, tratar minúsculas/maiúsculas antes da consulta, etc.).
- Exibir visualmente o grafo e o caminho encontrado (ex.: com `networkx` + `matplotlib`).
