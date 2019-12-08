def get_neighbour_pos(row, column, max_row, max_column):
    neighbours_pos = [[row-1,column], [row-1,column-1],[row-1,column+1],[row,column-1],[row,column+1],[row+1,column],
                     [row+1,column-1],[row+1,column+1]]
    el_to_remove = []

    #remove cell positions that are out of bounds
    for i in range(len(neighbours_pos)):
        if neighbours_pos[i][0] < 0 or neighbours_pos[i][0] >= max_row  or neighbours_pos[i][1] < 0 or neighbours_pos[i][1] >= max_column:
            el_to_remove.append(neighbours_pos[i])

    new_list = []
    for e in neighbours_pos:
        if e not in el_to_remove:
            new_list.append(e)

    neighbours_pos = new_list

    return neighbours_pos


class LiveCell:
    def __init__(self):
        self.value = '1'
        self.neighbours = 0
        self.x = 0
        self.y = 0

    def update_pos(self, row, column):
        self.x = column
        self.y = row

    def get_neighbours(self,grid):
        self.neighbours = 0
        n_pos = get_neighbour_pos(self.y, self.x, grid.num_rows, grid.num_columns)

        for pos in n_pos:
            if grid.is_cell(pos[0],pos[1]):
                self.neighbours += 1


class Grid:
    def __init__(self,columns, rows):
        self.num_columns = columns
        self.num_rows = rows
        self.grid = []

    def create_grid(self):
        for row in range(self.num_rows):
            self.grid.append([])
            for column in range(self.num_columns):
                self.grid[row].append('0')
        return self.grid

    def add_cell(self, row, column, cell):
        self.grid[row][column] = cell
        cell.update_pos(row, column)

    def is_cell(self, row, column):
        if isinstance(self.grid[row][column], LiveCell):
            return True
        else:
            return False

    def get_cell(self, row, column):
        if self.is_cell(row,column):
            return self.grid[row][column]

    def remove_cell(self, row, column):
        self.grid[row][column] = '0'


    #determine if empty cell has 3 live cell neighbours
    def neighbours_of_empty(self, row, column):
        count = 0
        n_pos = get_neighbour_pos(row, column, self.num_rows, self.num_columns)
        for pos in n_pos:
            if self.is_cell(pos[0],pos[1]):
                count += 1

        if count == 3:
            return True

    def print_board(self):
        for row in range(self.num_rows):
            temp_arr = []
            for column in range(self.num_columns):
                if self.is_cell(row,column):
                     temp_arr.append(self.grid[row][column].value)
                else:
                    temp_arr.append(self.grid[row][column])
            print(temp_arr)
            print('\n')


def check_state(grid):
    cells = []
    emptyToFill = []

    for row in range(grid.num_rows):
        for column in range(grid.num_columns):
            if grid.is_cell(row,column):
                cell = grid.get_cell(row,column)
                cell.get_neighbours(grid)
                cells.append(cell)

            else:
                 if grid.neighbours_of_empty(row, column):
                     emptyToFill.append([row,column])

    for pos in emptyToFill:
        grid.add_cell(pos[0], pos[1], LiveCell())


    for cell in cells:
         if cell.neighbours < 2 or cell.neighbours > 3:
             grid.remove_cell(cell.y, cell.x)


def main(grid):
    print("initial state:")
    grid.print_board()
    for i in range(5):
        print("iteration " + str((i+1)) +'\n')
        check_state(g)
        g.print_board()
        print('\n')





g = Grid(5,5)
g.create_grid()
cell = LiveCell()
cell2 = LiveCell()
cell3 = LiveCell()
g.add_cell(2,1,cell)
g.add_cell(2,2,cell2)
g.add_cell(2,3,cell3)
print('\n')

main(g)
