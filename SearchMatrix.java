public class SearchMatrix {

    public boolean searchMatrix(int[][] matrix, int target) {

        boolean isPresent = false;

        int nRows = matrix.length;
        int nCols = matrix[0].length;

        // System.out.println(nRows + " " + nCols);

        int rowCounter = 0;
        int colCounter = nCols - 1;

        while (rowCounter >= 0 && rowCounter < nRows && colCounter >= 0 && colCounter < nCols) {

            if (matrix[rowCounter][colCounter] == target) {
                isPresent = true;
                break;
            } else if (matrix[rowCounter][colCounter] < target) {
                rowCounter++;
            } else {
                colCounter--;
            }
        }

        return isPresent;
    }

    public static void main(String args[]) {

        int[][] matrix = { { 1, 3, 5, 7 },
                { 10, 11, 16, 20 },
                { 23, 30, 34, 60 } };

        int target = 13;

        SearchMatrix sm = new SearchMatrix();
        System.out.println(sm.searchMatrix(matrix, target));
    }

}
