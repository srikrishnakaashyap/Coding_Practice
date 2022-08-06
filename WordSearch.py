class WordSearch:

    def dfs(self, i, j, board, visited, word, wordIndex):

        if wordIndex == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False

        answer = False

        xrow = [1, 0, -1, 0]
        yrow = [0, 1, 0, -1]

        for a in range(4):
            if 0 <= i + xrow[a] < len(board) and 0 <= j + yrow[a] < len(board[0]) and not visited[i + xrow[a]][j + yrow[a]] and board[i + xrow[a]][j + yrow[a]] == word[wordIndex]:
                visited[i + xrow[a]][j + yrow[a]] = True
                answer = answer or self.dfs(
                    i + xrow[a], j + yrow[a], board, visited, word, wordIndex+1)
                visited[i + xrow[a]][j + yrow[a]] = False

        return answer

    def wordSearch(self, board, word):

        m = len(board)
        n = len(board[0])

        visited = [[False for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and not visited[i][j]:
                    visited[i][j] = True
                    if self.dfs(i, j, board, visited, word, 1):
                        return True
                    visited[i][j] = False

        return False


if __name__ == "__main__":

    ws = WordSearch()

    board = [["A", "B", "C", "E"], [
        "S", "F", "C", "S"], ["A", "D", "E", "E"]]

    word = "ABCCED"

    print(ws.wordSearch(board, word))
