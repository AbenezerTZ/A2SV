class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        nums = ["1","2","3","4","5","6","7","8","9"]
        freq = {"1":[[],[]],'2':[[],[]],'3':[[],[]],'4':[[],[]],'5':[[],[]],'6':[[],[]],'7':[[],[]],'8':[[],[]],'9':[[],[]]}
        for i in range(9):
            for j in range(9):
                if board[i][j] in freq:
                    
                    if i in freq[board[i][j]][0] or j in freq[board[i][j]][1]:
                        return False
                    else:
                        freq[board[i][j]][0].append(i)
                        freq[board[i][j]][1].append(j)
                        
        for i in range(0,9,3): 
            for j in range(0,9,3): 
                temp = []
                for n in range(3):
                    if board[i][j+n] in nums:
                        if board[i][j+n] in temp:
                            print("first")
                            return False
                        else:
                            temp.append(board[i][j+n])
                for n in range(3):
                    if board[i+1][j+n] in nums:
                        if board[i+1][j+n] in temp:
                            print(temp)
                            print("second")
                            return False
                        else:
                            temp.append(board[i+1][j+n])
                for n in range(3):
                    if board[i+2][j+n] in nums:
                        if board[i+2][j+n] in temp:
                            print("third")
                            return False
                        else:
                            temp.append(board[i+2][j+n])
        return True