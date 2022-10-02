from maze_generator import Maze
from time import sleep

def solve_maze(size):

    m = Maze(size)
    for position in m.visited:
        if m.start == m.end:
            break
        m.flip(*m.start, 1)
        m.start = m.connect_neighbour(m.start, position, value='@')
        m.display()
        sleep(0.25)
        m.move(*position)
        m.display()
        sleep(0.25)


if __name__ == '__main__':
    solve_maze(10)
