from colorama import init, Fore
from random import randint, choice

class Maze:
    """Generate a size x size maze

    How to work with this class:
    self.start: initial position
    self.end: end position
    self.maze: the maze (2d matrix)
    
    self.is_wall(x, y): check if a position is a wall
    self.get_moves(x, y): get a list of all possible NEWS moves for a position
    self.display(): print the maze to terminal
    
    """

    def __init__(self, size = 5) -> None:

        self.size = size * 2 + 1
        self.visited = []
        self.moves = []
        wall = 0
        path = 1

        self.maze = [[wall] * self.size for _ in range(self.size)] # to fill the whole maze with walls

        for i in range(2, self.size):
            for j in range(2, self.size, 2):
                if i % 2 == 0:
                    self.flip(j, i)
                else:
                    if j != 2:
                        self.flip(j-1, i)    

        self.generate()
        # choose a random start and end
        start = choice(self.visited)
        end = choice(self.visited)
        while end == start:
            end = choice(self.visited)

        self.flip(*start, '@')
        self.flip(*end, 'e')

        self.start = start
        self.end = end
       
    def move(self, x, y):
        '''Move the player to the given location'''
        self.flip(x, y, value='@')
        self.flip(*self.start, value = 1)
        self.start = (x, y)

    def get_moves(self, x, y):
        '''Get all possible moves for a position
        return a tuple of all possible positions
        '''
        adj = [(x - 1, y),
               (x + 1, y),
               (x, y + 1),
               (x, y - 1),
               ]      
        return tuple(
            cell for cell in adj
            if not self.is_wall(*cell)
        )

    def generate(self):
        '''Generate a maze'''
        cell = self.first_cell()

        def remove_wall(cell1):
            cell2 = self.get_neighbour(*cell1)
            if cell2:
                self.connect_neighbour(cell1, cell2)
                remove_wall(cell2)
            else:
                return

        remove_wall(cell)

    def first_cell(self):
        '''Get a random cell that is not a wall'''

        x = randint(2, self.size - 1)
        y = randint(2, self.size - 1)

        while self.is_wall(x, y):
            x = randint(2, self.size - 1)
            y = randint(2, self.size - 1)
        
        return (x, y)

    def get_neighbour(self, x, y):
        '''Get the NWES neighours of a cell'''
        adj = [(x - 2, y),
               (x + 2, y),
               (x, y + 2),
               (x, y - 2),
               ]
        neighbours = [
            cell for cell in adj
            if not self.is_wall(*cell) and cell not in self.visited
        ]
        if neighbours:
            cell = choice(neighbours)
            self.visited.append(cell)
            return cell
        else:
            return None

    def connect_neighbour(self, cell1, cell2, value=None):
        '''Connect 2 cells separated by a wall'''
        if cell1[0] == cell2[0]:
            if cell1[1] > cell2[1]:
                x, y = cell1[0], cell1[1] - 1
            else:
                x, y = cell1[0], cell1[1] + 1
        else:
            if cell1[0] > cell2[0]:
                x, y = cell1[0] - 1, cell1[1]
            else:
                x, y = cell1[0] + 1, cell1[1]

        self.flip(x, y, value)
        return (x, y)

    def flip(self, x, y, value=None):
        '''Flip the value of a maze cell between 1 and 0
        0 < x, y <= size
        '''
        # we need to consider the case when x,y = 0 because then x = x  - 1 = -1
        x = x - 1 # list starts at index 0 so we subtract 1 
        y = y - 1
        if value is None:
            self.maze[x][y] = int(not self.maze[x][y])
        else:
            self.maze[x][y] = value

    def is_wall(self, x, y):
        '''Check if a cell if a wall'''
        x = x - 1
        y = y - 1
        try:
            return not self.maze[x][y]
        except:
            return True

    def display(self):
        '''Print the maze in color'''
        init()
        for i in range(self.size):
            for j in range(self.size):
                x = str(self.maze[j][i])
                if self.maze[j][i] == 'e':
                    color = Fore.BLUE
                elif self.maze[j][i] == '@':
                    color = Fore.YELLOW
                elif self.maze[j][i]:
                    color = Fore.WHITE
                elif not self.maze[j][i]:
                    color = Fore.RED
                print(color, x, end = "")
            print('\n')

if __name__ == "__main__":

    m = Maze(11)
    m.display()
    # print(m.get_moves(*m.start))
