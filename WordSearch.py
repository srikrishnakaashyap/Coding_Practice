class WordSearch:

    def dfs(self, i, j, board, word, visited):
        pass

    def wordSearch(self, board, word):

        m = len(board)
        n = len(board[0])

        visited = [[-1 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    return self.dfs(i, j, board, word, visited)


if __name__ == "__main__":

    ws = WordSearch()

    board = [["A", "B", "C", "E"], [
        "S", "F", "C", "S"], ["A", "D", "E", "E"]]

    word = "ABCCED"

    print(ws.wordSearch(board, word))
