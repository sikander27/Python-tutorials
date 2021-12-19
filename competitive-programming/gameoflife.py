class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid_neigh(x, y):
            return x < len(board) and x >= 0 and y < len(board[0]) and y >= 0
        
        class_x = [0, 0, 1, 1, 1, -1, -1, -1]
        class_y = [1, -1, 1, -1, 0, 0, 1, -1]
        
        # for row in range(len(board)):
        #     for col in range(len(board[0])):
                         
        #                  live_count = 0
        #                  for i in range(8):
        #                     curr_x, curr_y = row + class_x[i], col + class_y[i]
        #                     if is_valid_neigh(curr_x, curr_y) and abs(board[curr_x][curr_y]) == 1:
        #                         # print(live_count)
        #                         live_count += 1
                               
                         
        #                  if board[row][col] == 1 and (live_count < 2 or live_count > 3):
        #                     # print("dead")
        #                     board[row][col] == -1
                         
        #                  if board[row][col] == 0 and live_count == 3:
        #                     # print("live")
        #                     board[row][col] == 2
                         
        for row in range(len(board)):
            for col in range(len(board[0])):
                
                # Loop to count all live neighbors
                count_live_neighbors = 0
                for i in range(8):
                    curr_x, curr_y = row + ways_x[i], col + ways_y[i]
                    if isValidNeighbor(curr_x, curr_y) and abs(board[curr_x][curr_y]) == 1:
                        count_live_neighbors+=1
                
                # Rules 1 and 3: -1 indicates a cell that was live but now is dead.
                if board[row][col] == 1 and (count_live_neighbors < 2 or count_live_neighbors > 3):
                    board[row][col] = -1
                    
                # Rule 4: 2 indicates a cell that was dead but now is live.
                if board[row][col] == 0 and count_live_neighbors == 3:
                    board[row][col] = 2
        for row in range(len(board)):
            for col in range(len(board[0])):
                         if board[row][col] >= 1:
                            # print("live")
                            board[row][col] = 1
                         
                         else:
                            # print("dead")
                            board[row][col] = 0
                            
                            
                            