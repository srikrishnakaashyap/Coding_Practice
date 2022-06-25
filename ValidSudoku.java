public class ValidSudoku {

  public boolean isRowValid(char[][] board, int rowNumber) {
    boolean isValid = true;

    int arr[] = new int[10];

    for (int col = 0; col < 9; col++) {
      if (board[rowNumber][col] == '.') {
        continue;
      }

      if (arr[(int) board[rowNumber][col] - 48] == 1) {
        return false;
      }

      arr[(int) board[rowNumber][col] - 48] = 1;
    }

    return isValid;
  }

  public boolean isColValid(char[][] board, int colNumber) {
    boolean isValid = true;

    int arr[] = new int[10];

    for (int row = 0; row < 9; row++) {
      if (board[row][colNumber] == '.') {
        continue;
      }

      if (arr[(int) board[row][colNumber] - 48] == 1) {
        return false;
      }

      arr[(int) board[row][colNumber] - 48] = 1;
    }

    return isValid;
  }

  public boolean isBlockValid(char[][] board, int row, int col) {
    boolean isValid = true;

    return isValid;
  }

  public boolean isValid(char[][] board) {
    boolean isValid = true;

    boolean isRowValid = true;
    boolean isColValid = true;
    boolean isBlockValid = true;

    for (int index = 0; index < 9; index++) {
      isRowValid = this.isRowValid(board, index);
      if (isRowValid == false) {
        return false;
      }
      isColValid = this.isColValid(board, index);
      if (isColValid == false) {
        return false;
      }
    }

    return isValid;
  }

  public static void main(String args[]) {
    char[][] board = {
      { '5', '3', '.', '.', '7', '.', '.', '.', '.' },
      { '6', '.', '.', '1', '9', '5', '.', '.', '.' },
      { '.', '9', '8', '.', '.', '.', '.', '6', '.' },
      { '8', '.', '.', '.', '6', '.', '.', '.', '3' },
      { '4', '.', '.', '8', '.', '3', '.', '.', '1' },
      { '7', '.', '.', '.', '2', '.', '.', '.', '6' },
      { '.', '6', '.', '.', '.', '.', '2', '8', '.' },
      { '.', '.', '.', '4', '1', '9', '.', '.', '5' },
      { '.', '.', '.', '.', '8', '.', '.', '7', '9' },
    };

    ValidSudoku vs = new ValidSudoku();

    System.out.println(vs.isValid(board));
  }
}
