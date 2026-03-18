from pyamaze import maze, COLOR, agent

if __name__ == "__main__":
    # cria environment
    my_maze = maze(5, 5)
    # inicializa environment
    # my_maze.CreateMaze(5, 5, pattern="V", theme=COLOR.light) # já dando posição do target
    my_maze.CreateMaze(saveMaze=False, pattern="V", theme=COLOR.light)
    # cria agente
    # a = agent(my_maze, x=1, y=1, shape="arrow", filled=True, footprints=True) # já dando posição do agente
    a = agent(my_maze, shape="arrow", filled=True, footprints=True)
    # imprime o caminho ótimo
    print(my_maze.path)
    # faz o agente andar pelo caminho ótimo
    my_maze.tracePath({a: my_maze.path}, delay=200, kill=False)
    # executa tudo
    my_maze.run()
