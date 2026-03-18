from pyamaze import maze, COLOR, agent


def bfs_path(my_maze, my_agent):
    ini = (my_agent.x, my_agent.y)
    explored = [ini]
    fronteira = [ini]  
    bfs_path = {}
    while (len(fronteira) > 0):
        
    return "NNNN"

def ids_path(my_maze, my_agent):
    """
    Exercício 2:
    Implemente um algoritmo de busca de aprofundamento iterativo, 
    que encontre o caminho que o agente deve percorrer para encontrar a 
    saída do labirinto.

    Dicas:
    - Use o atributo my_maze.maze_map para checar os movimentos possíveis.
    - Use o atributo my_agent.position para saber a posição do agente.
    - Verifique os formatos adequados para um caminho nesse post do
    Towards Data Science, feito pelo autor do pacote:
    https://towardsdatascience.com/a-python-module-for-maze-search-algorithms-64e7d1297c96
    """
    # print(my_maze.maze_map)
    # print(my_agent.position)
    return "NNNN"



def dfs_path(m, a):
    """
    Implementação do algoritmo de busca por profundidade para encontrar o caminho
    de saída do labirinto.

    Args:
        m (pyamaze.maze): labirinto.
        a (pyamaze.agent): agente.

    Returns:
        forward_path (dict): caminho que leva o agente para fora do labirinto. 
    """
    start = (a.x, a.y)  # celula do estado inicial
    explored = [start]  # List para nós explorados 
    frontier = [start]  # List para a fronteira
    dfsPath = {}  # Vou utilizar o formato de dicionário para o retorno. 
    while len(frontier) > 0: # enquanto a fronteira não estiver vazia
        currCell = frontier.pop()
        if currCell == m._goal: # verifica objetivo
            break
        # Explora cada direção possível (ações)
        for direction in "WNSE":
            if m.maze_map[currCell][direction]:
                if direction == "E":
                    childCell = (currCell[0], currCell[1] + 1)
                elif direction == "W":
                    childCell = (currCell[0], currCell[1] - 1)
                elif direction == "S":
                    childCell = (currCell[0] + 1, currCell[1])
                elif direction == "N":
                    childCell = (currCell[0] - 1, currCell[1])
                # se celula já foi explorada, continua... 
                if childCell in explored:
                    continue  # Do nothing
                # Adiciona celular a fronteira e aos nós explorados
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell] = currCell
    forward_path = {}
    cell = m._goal  # destino
    while cell != start:
        # pega uma celula do caminho e coloca como chave no dict de caminho
        forward_path[dfsPath[cell]] = (
            cell  # o valor é a chave do caminho dfs
        )
        cell = dfsPath[
            cell
        ]  # operação termina assim que chegar no início, que é o destino.
    return forward_path


if __name__ == "__main__":
    # cria environment
    my_maze = maze(20, 15)
    # lê labirinto do exercício
    my_maze.CreateMaze(theme=COLOR.light)
    # cria agente
    my_agent = agent(my_maze, 3, 3, shape="arrow", filled=True, footprints=True)
    # calcula passos que o agente seguirá para sair do labirinto
    my_path = dfs_path(my_maze, my_agent)
    # executa os passos calculados
    my_maze.tracePath({my_agent: my_path}, delay=100, kill=False)
    # roda a animação mostrando o movimento do agente
    my_maze.run()
