"""
BUSCA GULOSA (BEST-FIRST SEARCH)
Algoritmo de busca informada que utiliza heurísticas para guiar a exploração
Problema: Encontrar o caminho de Arad até Bucareste no mapa da Romênia

Parâmetros:
- Grafo: representado como dicionário de adjacência com pesos (distâncias reais)
- Heurística: distância em linha reta até Bucareste (valor estimado)
- Estratégia: Always expand the node with the smallest heuristic value (h(n))
"""

import heapq
from collections import defaultdict
import sys

class BuscaGulosa:
    def __init__(self):
        """
        Inicializa a Busca Gulosa
        
        PARÂMETROS:
        - self.grafo: Dicionário representando o grafo de adjacência
          Formato: {cidade: [(vizinha, distancia_real), ...]}
        - self.h: Dicionário com heurísticas (distância reta até Bucareste)
          Formato: {cidade: distancia_heuristica}
        """
        # Definição do grafo (conexões entre cidades e distâncias reais)
        self.grafo = {
            'Arad': [('Sibiu', 140), ('Zerind', 75), ('Timisoara', 118)],
            'Zerind': [('Arad', 75), ('Oradea', 71)],
            'Oradea': [('Zerind', 71)],
            'Timisoara': [('Arad', 118), ('Lugoj', 111)],
            'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
            'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
            'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
            'Sibiu': [('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
            'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
            'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
            'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
            'Pitesti': [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Giurgiu', 90)],
            'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
            'Giurgiu': [('Pitesti', 90), ('Bucharest', 90)],
            'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vasui', 142)],
            'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
            'Eforie': [('Hirsova', 86)],
            'Vasui': [('Urziceni', 142), ('Iasi', 92)],
            'Iasi': [('Vasui', 92), ('Neamt', 87)],
            'Neamt': [('Iasi', 87)]
        }
        
        # HEURÍSTICA: Distância em linha reta até Bucareste
        # Esta é a função h(n) que estima o custo para alcançar o objetivo
        self.h = {
            'Oradea': 380,
            'Neamt': 234,
            'Zerind': 374,
            'Iasi': 226,
            'Arad': 366,
            'Fagaras': 178,
            'Timisoara': 329,
            'Lugoj': 244,
            'Mehadia': 241,
            'Vasui': 199,
            'Drobeta': 234,
            'Craiova': 160,
            'Pitesti': 98,
            'Sibiu': 253,
            'Rimnicu Vilcea': 193,
            'Bucharest': 0,
            'Giurgiu': 77,
            'Urziceni': 80,
            'Hirsova': 151,
            'Eforie': 199
        }
    
    def busca_gulosa(self, inicio, objetivo, verbose=True):
        """
        Executa o algoritmo de Busca Gulosa
        
        FUNCIONAMENTO:
        1. Inicializa a FRONTEIRA (fila de prioridade) com o nó inicial
        2. Mantém um conjunto de NÓS VISITADOS para evitar revisitar
        3. Enquanto houver nós para explorar:
           a. Seleciona o nó com o MENOR VALOR DE HEURÍSTICA (h(n))
           b. Se é o objetivo, retorna o caminho
           c. Caso contrário, expande o nó (adiciona vizinhos à fronteira)
        4. Retorna None se não encontrar solução
        
        PARÂMETROS:
        - inicio: nó de partida
        - objetivo: nó alvo
        - verbose: se True, imprime cada passo da busca
        
        ESTRUTURAS DE DADOS:
        - fronteira: heapq (fila de prioridade min-heap)
          Formato: (h(n), contador, nó, caminho)
          O contador evita conflitos de comparação entre nós com h(n) iguais
        - visitados: conjunto de nós já explorados
        - pai: dicionário para rastreamento do caminho
        """
        
        # INICIALIZAÇÃO da fronteira com o nó inicial
        # Formato: (valor_heuristica, contador, nó_atual, [caminho_até_aqui])
        fronteira = []
        h_valor = self.h[inicio]
        heapq.heappush(fronteira, (h_valor, 0, inicio, [inicio]))
        
        # Conjunto de NÓS VISITADOS (explorados)
        visitados = set()
        
        # Contador para desempate em caso de heurísticas iguais
        contador = 1
        
        if verbose:
            print(f"\n{'='*80}")
            print(f"BUSCA GULOSA: {inicio} → {objetivo}")
            print(f"{'='*80}\n")
            print(f"FASE 1: INICIALIZAÇÃO")
            print(f"  Nó inicial: {inicio}")
            print(f"  Nó objetivo: {objetivo}")
            print(f"  h({inicio}) = {h_valor} (distância reta ao objetivo)\n")
        
        passo = 1
        
        # LOOP PRINCIPAL da busca
        while fronteira:
            # Seleciona o nó com MENOR HEURÍSTICA
            h_atual, _, nodo_atual, caminho = heapq.heappop(fronteira)
            
            if verbose:
                print(f"PASSO {passo}: Expandindo nó '{nodo_atual}'")
                print(f"  h({nodo_atual}) = {h_atual}")
                print(f"  Caminho: {' → '.join(caminho)}")
                print(f"  Distância acumulada: {self._calcular_distancia_caminho(caminho)}")
            
            # VERIFICAÇÃO: Se é o objetivo, retorna o caminho
            if nodo_atual == objetivo:
                if verbose:
                    print(f"\n{'='*80}")
                    print(f"SUCESSO! Objetivo encontrado: {objetivo}")
                    print(f"{'='*80}")
                    print(f"\nCAMINHO FINAL: {' → '.join(caminho)}")
                    print(f"Comprimento do caminho: {len(caminho) - 1} cidades")
                    print(f"Distância total percorrida: {self._calcular_distancia_caminho(caminho)} km\n")
                
                return caminho, self._calcular_distancia_caminho(caminho)
            
            # Marca como visitado
            visitados.add(nodo_atual)
            
            # EXPANSÃO: Adiciona vizinhos à fronteira
            if verbose:
                print(f"  Vizinhos disponíveis:")
            
            vizinhos_info = []
            
            for vizinho, distancia in self.grafo[nodo_atual]:
                if vizinho not in visitados:
                    novo_caminho = caminho + [vizinho]
                    h_vizinho = self.h[vizinho]
                    heapq.heappush(fronteira, (h_vizinho, contador, vizinho, novo_caminho))
                    contador += 1
                    vizinhos_info.append((vizinho, h_vizinho, distancia))
                    
                    if verbose:
                        print(f"    - {vizinho}: h({vizinho}) = {h_vizinho}, " +
                              f"distância real = {distancia} km")
            
            if not vizinhos_info and verbose:
                print(f"    (nenhum vizinho novo para explorar)")
            
            print()
            passo += 1
        
        if verbose:
            print(f"{'='*80}")
            print("FALHA! Nenhum caminho encontrado para o objetivo.")
            print(f"{'='*80}\n")
        
        return None, float('inf')
    
    def _calcular_distancia_caminho(self, caminho):
        """
        Calcula a distância total de um caminho percorrido
        
        PARÂMETROS:
        - caminho: lista de nós [inicio, ..., fim]
        
        RETORNO:
        - distância total em km
        """
        distancia_total = 0
        for i in range(len(caminho) - 1):
            nodo_atual = caminho[i]
            proximo_nodo = caminho[i + 1]
            
            # Procura a distância na lista de adjacências
            for vizinho, dist in self.grafo[nodo_atual]:
                if vizinho == proximo_nodo:
                    distancia_total += dist
                    break
        
        return distancia_total
    
    def gerar_arvore_decisao(self, inicio, objetivo):
        """
        Gera uma representação da árvore de decisão da Busca Gulosa
        Mostra qual nó seria explorado em cada nível baseado na heurística
        """
        print(f"\n{'='*80}")
        print("ÁRVORE DE DECISÃO - BUSCA GULOSA")
        print(f"{'='*80}\n")
        
        # BFS para construir a árvore
        from collections import deque
        
        fila = deque([(inicio, [inicio])])
        nivel = 0
        nodos_por_nivel = {}
        visitados_arvore = set()
        
        while fila and nivel < 5:  # Limita a profundidade para visualização
            proximo_nivel = len(fila)
            nodos_por_nivel[nivel] = []
            
            for _ in range(proximo_nivel):
                nodo, caminho = fila.popleft()
                
                if nodo not in visitados_arvore:
                    visitados_arvore.add(nodo)
                    h_val = self.h[nodo]
                    nodos_por_nivel[nivel].append((nodo, h_val, caminho))
                    
                    if nodo != objetivo:
                        for vizinho, _ in self.grafo[nodo]:
                            if vizinho not in visitados_arvore:
                                fila.append((vizinho, caminho + [vizinho]))
            
            nivel += 1
        
        # Imprime a árvore
        for niv, nodos in nodos_por_nivel.items():
            print(f"\nNÍVEL {niv}:")
            print("-" * 80)
            
            # Ordena por heurística (como a Busca Gulosa faria)
            nodos_ordenados = sorted(nodos, key=lambda x: x[1])
            
            for nodo, h_val, caminho in nodos_ordenados:
                marca = " ← PRÓXIMO A EXPANDIR" if h_val == min(n[1] for n in nodos) else ""
                print(f"  {nodo}: h({nodo}) = {h_val}{marca}")
                print(f"    Caminho: {' → '.join(caminho)}")


def main():
    """
    Função principal para executar a Busca Gulosa
    """
    busca = BuscaGulosa()
    
    # Define problema: Arad → Bucharest
    inicio = 'Arad'
    objetivo = 'Bucharest'
    
    # Executa a Busca Gulosa
    caminho, distancia = busca.busca_gulosa(inicio, objetivo, verbose=True)
    
    # Gera a árvore de decisão
    busca.gerar_arvore_decisao(inicio, objetivo)
    
    # Resumo dos resultados
    print(f"\n{'='*80}")
    print("RESUMO DOS RESULTADOS")
    print(f"{'='*80}")
    if caminho:
        print(f"\nCaminho encontrado: {' → '.join(caminho)}")
        print(f"Número de cidades visitadas: {len(caminho)}")
        print(f"Distância total: {distancia} km")
    else:
        print("Nenhum caminho encontrado!")
    print()


if __name__ == "__main__":
    main()
