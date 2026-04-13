from pyamaze import maze, COLOR, agent

def h(a,b):
    #heurística de Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_path(m,a):
    '''
        lógica do algoritmo:
        A* é um algoritmo de busca heurística que utiliza uma função de avaliação para determinar a ordem de exploração dos nós. 
        Ele combina o custo do caminho percorrido até o nó atual (g(n)) com uma estimativa do custo restante para alcançar o objetivo (h(n)). 
        O agente começa na posição inicial e explora os nós com o menor valor de f(n) = g(n) + h(n) primeiro, onde g(n) é o custo do caminho percorrido até o nó n e h(n) é a heurística que estima o custo restante para alcançar o objetivo.
    '''
    #fronteira ← fila de prioridade ordenada por f (n) = g (n) + h(n)
    fronteira = []
    for vizinho in m.maze_map[(a.x, a.y)]:
        fronteira.append((vizinho, 1 + abs(vizinho[0] - m._goal[0]) + abs(vizinho[1] - m._goal[1])))
    
    return {}



if __name__ == "__main__":
    # cria environment
    my_maze = maze(20, 15)
    # lê labirinto do exercício
    my_maze.CreateMaze(theme=COLOR.light)
    # cria agente
    my_agent = agent(my_maze, 3, 3, shape="arrow", filled=True, footprints=True)
    # calcula passos que o agente seguirá para sair do labirinto

    my_path = astar_path(my_maze, my_agent)
    # executa os passos calculados
    my_maze.tracePath({my_agent: my_path}, delay=100, kill=False)
    # roda a animação mostrando o movimento do agente
    my_maze.run()