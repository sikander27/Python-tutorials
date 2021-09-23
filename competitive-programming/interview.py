"""
Game of life

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using
the following four rules:

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its
current state. The next state is created by applying the above rules simultaneously to
every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
"""


class Solution:

    def run(self, board):
        """ Modifies the board in-place.  Does not return anything.
        """
        rows = len(board)
        col = len(board[0])
        new_board = []
        for i in range(rows):
            n_row = []
            for j in range(columns):
                k = knock_neighbour(board,i,j)
             
                n_row.append()

    def knock_neighbour(self,board,i,j):
        #ld,t,rd,r,brd,b,bld,l
        neighbours = []
        if i==0:
            if j==0:
                if board[i][j]:
                    r = board[i][j+1] #0
                    b = board[i+1][j] #1
                    brd = board[i+1][j+1] #0
                    neigbours.extend((r,b,brd))
        else:
            neigbours.extend((board[i][j+1]))
                
                
                
        if i == rows-1:
            
        
    
    
    
    
    
    
    