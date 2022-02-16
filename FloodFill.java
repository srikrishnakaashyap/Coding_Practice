import java.util.LinkedList;

public class FloodFill {

    public int[][] floodFill(int[][] image, int sr, int sc, int newColour) {

        LinkedList<String> queue = new LinkedList<>();
        boolean[][] visited = new boolean[image.length][image[0].length];

        int colour = image[sr][sc];

        queue.add(sr + "," + sc);

        int[] addRow = { -1, 1, 0, 0 };
        int[] addCol = { 0, 0, -1, 1 };

        while (!queue.isEmpty()) {
            int row = Integer.parseInt(queue.peek().split(",")[0]);
            int column = Integer.parseInt(queue.peek().split(",")[1]);

            if (row > -1 && column > -1 && row < image.length && column < image[0].length) {
                if (!visited[row][column]) {
                    visited[row][column] = true;
                    if (image[row][column] == colour) {
                        image[row][column] = newColour;

                        for (int index = 0; index < 4; index++) {
                            int newRow = row + addRow[index];
                            int newCol = column + addCol[index];
                            queue.add(newRow + "," + newCol);
                        }
                    }

                }

                queue.pop();

            } else {
                queue.pop();
            }
        }

        return image;
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

        int[][] image = { { 1, 1, 1 }, { 1, 1, 0 }, { 1, 0, 1 } };
        int sr = 1;
        int sc = 1;
        int newColour = 2;

        FloodFill ff = new FloodFill();
        printArray(ff.floodFill(image, sr, sc, newColour));

        // ff.floodFill(image, sr, sc, newColour);

    }

}
