
library(graphics)

solveMaze <- function(maze, row, col) {
  nrows <- nrow(maze)
  ncols <- ncol(maze)
  
  if (row < 1 || row > nrows || col < 1 || col > ncols) {
    return(FALSE)
  }
  
  if (maze[row, col] == "E") {
    return(TRUE)
  }
  
  if (maze[row, col] == " " || maze[row, col] == "S") {
    
    maze[row, col] <- "."
    
    plotMaze(maze)
    
    if (solveMaze(maze, row - 1, col) == TRUE) {  # Up
      return(TRUE)
    }
    if (solveMaze(maze, row + 1, col) == TRUE) {  # Down
      return(TRUE)
    }
    if (solveMaze(maze, row, col - 1) == TRUE) {  # Left
      return(TRUE)
    }
    if (solveMaze(maze, row, col + 1) == TRUE) {  # Right
      return(TRUE)
    }
    
    maze[row, col] <- " "
    return(FALSE)
  }
  
  return(FALSE)
}

plotMaze <- function(maze) {
  nrows <- nrow(maze)
  ncols <- ncol(maze)
  
  plot.new()
  plot.window(xlim = c(0, ncols), ylim = c(0, nrows))
  box()
  
  for (row in 1:nrows) {
    for (col in 1:ncols) {
      cell <- maze[row, col]
      if (cell == "#") {
        rect(col - 1, nrows - row, col, nrows - row + 1, col = "black", border = NA)
      } else if (cell == "S") {
        rect(col - 1, nrows - row, col, nrows - row + 1, col = "green", border = NA)
      } else if (cell == "E") {
        rect(col - 1, nrows - row, col, nrows - row + 1, col = "red", border = NA)
      } else if (cell == ".") {
        rect(col - 1, nrows - row, col, nrows - row + 1, col = "blue", border = NA)
      }
    }
  }
  
  Sys.sleep(1.0)
}

maze <- matrix(c(
  " ", "#", "# ", "#", "#", "#", " ", "#", " ", 
  "#", "S", " ", " ", " ", " ", "#", " ", "#",
  "#", " ", " ", " ", " ", " ", "#", "#", " ",
  "#", " ", "#", " ", "#", " ", "#", "#", " ",
  "#", " ", "#", " ", " ", " ", " ", " ", "#",
  "#", " ", "#", "#", " ", " ", "#", " ", "#",
  "#", "#", "#", "#", "#", "#", "#", "E", "#"
), nrow = 7, byrow = TRUE)

solved_maze <- maze

start_pos <- which(solved_maze == "S", arr.ind = TRUE)
start_row <- start_pos[1, "row"]
start_col <- start_pos[1, "col"]

nrows <- nrow(maze)
ncols <- ncol(maze)
plot.new()
plot.window(xlim = c(0, ncols), ylim = c(0, nrows))
box()

solveMaze(solved_maze, row = start_row, col = start_col)

print(solved_maze)
