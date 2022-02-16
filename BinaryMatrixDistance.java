import java.lang.*;

public class BinaryMatrixDistance {

    public int getDistance(int[][] mat, int row, int column) {
        System.out.println(row + ", " + column);
        if (row >= 0 && column >= 0 && row < mat.length && column < mat[0].length) {
            if (mat[row][column] == 0) {
                return 0;
            } else {
                return 1 + Math.min(this.getDistance(mat, row - 1, column), Math.min(
                        this.getDistance(mat, row, column - 1),
                        Math.min(this.getDistance(mat, row, column + 1), this.getDistance(mat, row + 1, column))));
            }
        } else {
            return 100000;
        }

    }

    public int[][] updateMatrix(int[][] mat) {

        int ans[][] = new int[mat.length][mat[0].length];

        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[0].length; j++) {

                if (mat[i][j] != 0) {

                    ans[i][j] = this.getDistance(mat, i, j);
                }
            }
        }

        return ans;
    }

    public static void printArray(int[][] array) {
        for (int row = 0; row < array.length; row++) {
            for (int col = 0; col < array[0].length; col++) {

                System.out.print(array[row][col] + " ");

            }
            System.out.println();
        }
    }

    public static void main(String args[]) {

        int mat[][] = { { 0, 0, 0 }, { 0, 1, 0 }, { 1, 1, 1 } };

        BinaryMatrixDistance bmd = new BinaryMatrixDistance();

        printArray(bmd.updateMatrix(mat));

    }

}
