from maze_generator import Maze
from time import sleep

def solve_maze(size = 12, delay=0.25):
    '''Solve a generated maze'''
    m = Maze(size)
    for position in m.visited:
        if m.start == m.end:
            break
        m.flip(*m.start, 1)
        m.start = m.connect_neighbour(m.start, position, value='@')
        m.display()
        sleep(delay)
        m.move(*position)
        m.display()
        sleep(delay)


if __name__ == '__main__':
    solve_maze(12)
