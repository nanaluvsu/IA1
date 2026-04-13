# estudando implementação de bfs
from pyamaze import maze, COLOR, agent


class NoBinario:
    def __init__(self, estado, pai=None):
        self.estado = estado
        self.pai = pai
        self.filho_esquerdo = None
        self.irmao_direito = None


def bfs(ambiente, agente):
    '''
        lógica do algoritmo:
        BFS utiliza fila FIFO para a exploração. O agente começa na posição inicial e explora todos os nós vizinhos antes de avançar para os próximos níveis.
        O agente mantém uma lista de nós a serem explorados (fronteira) e uma lista de nós já explorados (explorado) para evitar ciclos. 
        O algoritmo continua até encontrar o nó objetivo ou esgotar todas as possibilidades.
    '''
    inicio = (agente.x, agente.y) # posição inicial do agente
    raiz = NoBinario(inicio)
    fronteira = [raiz] # fila FIFO de nós da árvore
    explorado = [inicio] # conjunto de posições já visitadas

    no_objetivo = None
    
    while len(fronteira) > 0: # enquanto houver nós a serem explorados
        no_atual = fronteira.pop(0) # remove o primeiro nó da fronteira (FIFO)
        estado_atual = no_atual.estado
        
        if estado_atual == ambiente._goal: # se o nó atual for o objetivo, constrói o caminho percorrido
            no_objetivo = no_atual
            break # sai do loop para construir o caminho percorrido
        ambiente.maze_map[estado_atual] # obtém os vizinhos do nó atual
        
        for vizinho in ambiente.maze_map[estado_atual]: # para cada vizinho do nó atual
            if vizinho not in explorado:
                explorado.append(vizinho)
                no_filho = NoBinario(vizinho, no_atual) # cria um novo nó para o vizinho
                if no_atual.filho_esquerdo is None: 
                    no_atual.filho_esquerdo = no_filho 
                else:
                    no_irmao = no_atual.filho_esquerdo
                    while no_irmao.irmao_direito is not None:
                        no_irmao = no_irmao.irmao_direito
                    no_irmao.irmao_direito = no_filho
                fronteira.append(no_filho) # adiciona o nó filho à fronteira
                bfs_path = {}
        if no_objetivo is None:
            return {}
        else:
            #reconstrói o caminho percorrido do nó objetivo até a raiz
            bfs_path = {}
            no_atual = no_objetivo
            while no_atual.pai is not None:
                pai = no_atual.pai
                bfs_path[pai.estado] = no_atual.estado
                no_atual = pai

    return bfs_path
        
            
    
    
    
if __name__ == "__main__":
    # cria environment
    my_maze = maze(20, 15)
    # lê labirinto do exercício
    my_maze.CreateMaze(theme=COLOR.light)
    # cria agente
    my_agent = agent(my_maze, 3, 3, shape="arrow", filled=True, footprints=True)
    # calcula passos que o agente seguirá para sair do labirinto
    my_path = bfs(my_maze, my_agent)
    # executa os passos calculados
    my_maze.tracePath({my_agent: my_path}, delay=100, kill=False)
    # roda a animação mostrando o movimento do agente
    my_maze.run()
