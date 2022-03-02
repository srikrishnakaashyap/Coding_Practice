import copy
class NQueens:


    def solve(self, column, n, matrix, answer, rowHash, topDiag, bottomDiag):
        if column == n:
            # print(matrix)
            answer.append(copy.deepcopy(matrix))
            return
        
        for i in range(0, n):

            if rowHash[i] == 0 and topDiag[i + column] == 0 and bottomDiag[n - 1 + (column - i)] == 0:
                rowHash[i] = 1
                topDiag[i + column] = 1
                bottomDiag[n - 1 + (column - i)] = 1
                matrix[i][column] = 'Q'
                
                self.solve(column+1, n, matrix, answer, rowHash, topDiag, bottomDiag)

                rowHash[i] = 0
                topDiag[i + column] = 0
                bottomDiag[n - 1 + (column - i)] = 0
                matrix[i][column] = '.'

    def print_board(self, matrix):

        # print("FROM PRINTING")

        for i in range(len(matrix)):

            print("------------------GRID {}----------------".format(i))
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")
                print()
        

    def N_Queen(self, n):

        answer = []
        matrix = [["." for i in range(n)] for j in range (n)]  
        # print(matrix)
        rowHash = [0 for i in range(n)]
        topDiag = [0 for i in range((2*n) - 1)]
        bottomDiag = [0 for i in range((2*n) - 1)]

        self.solve(0, n, matrix, answer, rowHash, topDiag, bottomDiag)

        # print(answer[0])

        self.print_board(answer)


    
if __name__ == "__main__":

    n = 8
    ans = NQueens().N_Queen(n)
