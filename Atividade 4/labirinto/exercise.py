from pyamaze import maze, COLOR, agent

def child_cell(currCell, direction):
        if direction == "E":
            return (currCell[0], currCell[1] + 1)
        if direction == "W":
            return (currCell[0], currCell[1] - 1)
        if direction == "S":
            return (currCell[0] + 1, currCell[1])
        return (currCell[0] - 1, currCell[1])

def bfs_path(m, a):
    """
    Implementação do algoritmo de busca em largura (BFS) para encontrar o
    caminho de saída do labirinto.

    Args:
        m (pyamaze.maze): labirinto.
        a (pyamaze.agent): agente.

    Returns:
        forward_path (dict): caminho que leva o agente para fora do labirinto.
    """
    start = (a.x, a.y)
    frontier = [start]  # fronteira
    explored = [start]  # nós explorados
    bfsPath = {}  # mapa para reconstrução do caminho

    while len(frontier) > 0:
        currCell = frontier.pop(0)

        if currCell == m._goal:  # verifica objetivo
            break

        explored.append(currCell)

        # Explora cada direção possível (ações)
        for direction in "WNSE":
            if m.maze_map[currCell][direction]:
                if direction == "E":
                    childCell = child_cell(currCell, direction)
                elif direction == "W":
                    childCell = child_cell(currCell, direction)
                elif direction == "S":
                    childCell = child_cell(currCell, direction)
                else:
                    childCell = child_cell(currCell, direction)

                # se célula não foi explorada e não está na fronteira, adiciona. lógica do pseudocódigo visto em aula.
                if childCell not in explored and childCell not in frontier:
                    bfsPath[childCell] = currCell
                    explored.append(childCell)
                    frontier.append(childCell)
    forward_path = {}
    cell = m._goal  # destino
    while cell != start:
        # pega uma celula do caminho e coloca como chave no dict de caminho
        forward_path[bfsPath[cell]] = (
            cell  # o valor é a chave do caminho dfs
        )
        cell = bfsPath[
            cell
        ]  # operação termina assim que chegar no início, que é o destino.
    return forward_path

def ids_path(m, a):
    """
    Implementação do algoritmo de busca por aprofundamento iterativo (IDS)
    para encontrar o caminho de saída do labirinto.

    Args:
        m (pyamaze.maze): labirinto.
        a (pyamaze.agent): agente.

    Returns:
        forward_path (dict): caminho que leva o agente para fora do labirinto.
    """
    start = (a.x, a.y)
    goal = m._goal


    def dfs_com_limite(l):
        frontier = [(start, 0)]  # fronteira: (célula, profundidade)
        explored = [start]  # nós explorados nesta iteração
        parent = {}  # mapa para reconstrução do caminho

        while len(frontier) > 0:
            currCell, depth = frontier.pop()

            if currCell == goal:  # verifica objetivo
                return parent, True

            if depth == l:  # respeita o limite de profundidade atual
                continue

            # Explora cada direção possível (ações)
            for direction in "WNSE":
                if m.maze_map[currCell][direction]:
                    if direction == "E":
                        childCell = child_cell(currCell, direction)
                    elif direction == "W":
                        childCell = child_cell(currCell, direction)
                    elif direction == "S":
                        childCell = child_cell(currCell, direction)
                    else:
                        childCell = child_cell(currCell, direction)
                    newDepth = depth + 1
                    # se célula já foi explorada, continua...
                    if childCell in explored:
                        continue

                    explored.append(childCell)
                    parent[childCell] = currCell
                    frontier.append((childCell, newDepth))

        return parent, False

    max_depth = len(m.grid)  # limite máximo para iterações de profundidade

    # Incrementa o limite e executa DFS limitada até encontrar o objetivo
    for limit in range(max_depth + 1):
        idsPath, found = dfs_com_limite(limit)
        if found:
            forward_path = {}
            cell = goal
            while cell != start:
                # reconstrói o caminho do objetivo até o estado inicial
                forward_path[idsPath[cell]] = cell
                cell = idsPath[cell]
            return forward_path

    return


# preservando código original de dfs. sem implementação da função child_cell.
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
    #my_path = bfs_path(my_maze, my_agent)
    #my_path = dfs_path(my_maze, my_agent)
    my_path = ids_path(my_maze, my_agent)
    # executa os passos calculados
    my_maze.tracePath({my_agent: my_path}, delay=100, kill=False)
    # roda a animação mostrando o movimento do agente
    my_maze.run()
