import matplotlib.pyplot as plt

def solve_maze(maze, row, col):
    nrows = len(maze)
    ncols = len(maze[0])
    
    if row < 0 or row >= nrows or col < 0 or col >= ncols:
        return False
   
    if maze[row][col] == "E":
        return True  
    
    if maze[row][col] == " " or maze[row][col] == "S":
        
        maze[row][col] = "."
        
        plot_maze(maze)
        if solve_maze(maze, row - 1, col):  # Up
            return True
        if solve_maze(maze, row + 1, col):  # Down
            return True
        if solve_maze(maze, row, col - 1):  # Left
            return True
        if solve_maze(maze, row, col + 1):  # Right
            return True
       
        maze[row][col] = " "
        return False
    return False

def plot_maze(maze):
    nrows = len(maze)
    ncols = len(maze[0])

    plt.clf()
    plt.xlim(0, ncols)
    plt.ylim(0, nrows)
    plt.gca().set_aspect("equal")
    plt.axis("off")

    for row in range(nrows):
        for col in range(ncols):
            cell = maze[row][col]
            if cell == "#":
                plt.fill([col, col + 1, col + 1, col], [nrows - row, nrows - row, nrows - row + 1, nrows - row + 1], "black")
            elif cell == "S":
                plt.fill([col, col + 1, col + 1, col], [nrows - row, nrows - row, nrows - row + 1, nrows - row + 1], "green")
            elif cell == "E":
                plt.fill([col, col + 1, col + 1, col], [nrows - row, nrows - row, nrows - row + 1, nrows - row + 1], "red")
            elif cell == ".":
                plt.fill([col, col + 1, col + 1, col], [nrows - row, nrows - row, nrows - row + 1, nrows - row + 1], "purple")
    plt.pause(0.001)

def read_maze_from_file(file):
    with open(file, "r") as f:
        maze = [list(line.strip()) for line in f]
    return maze

maze_file = "maze.txt"
maze = read_maze_from_file(maze_file)

solved_maze = [row[:] for row in maze]

for row in range(len(solved_maze)):
    for col in range(len(solved_maze[row])):
        if solved_maze[row][col] == "S":
            start_row = row
            start_col = col
            break

nrows = len(maze)
ncols = len(maze[0])
plt.figure(figsize=(15, 15))

solve_maze(solved_maze, row=start_row, col=start_col)

for row in solved_maze:
    print("".join(row))
