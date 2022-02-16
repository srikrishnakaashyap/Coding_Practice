import java.util.LinkedList;

public class MaxAreaOfIsland {

    static boolean[][] visited;

    public int dfs(int[][] grid, int row, int column) {
        int size = 0;

        LinkedList<String> queue = new LinkedList<>();

        queue.add(row + "," + column);

        int[] addRow = { -1, 1, 0, 0 };
        int[] addCol = { 0, 0, -1, 1 };

        while (!queue.isEmpty()) {

            int currRow = Integer.parseInt(queue.peek().split(",")[0]);
            int currCol = Integer.parseInt(queue.peek().split(",")[1]);

            if (currRow > -1 && currCol > -1 && currRow < grid.length && currCol < grid[0].length) {
                if (!visited[currRow][currCol]) {
                    visited[currRow][currCol] = true;
                    size++;

                    for (int ctr = 0; ctr < 4; ctr++) {

                        int newRow = currRow + addRow[ctr];
                        int newCol = currCol + addCol[ctr];

                        if (newRow >= 0 && newRow < grid.length && newCol >= 0 && newCol < grid[0].length
                                && grid[newRow][newCol] == 1) {
                            queue.add(newRow + "," + newCol);
                        }

                    }
                }
            }

            queue.pop();

        }

        return size;

    }

    public int maxArea(int[][] grid) {
        int maximumArea = 0;

        visited = new boolean[grid.length][grid[0].length];

        for (int row = 0; row < grid.length; row++) {
            for (int column = 0; column < grid[0].length; column++) {
                if (!visited[row][column] && grid[row][column] == 1) {

                    // System.out.println(row + " " + column);

                    maximumArea = Math.max(maximumArea, this.dfs(grid, row, column));

                }
            }
        }

        return maximumArea;
    }

    public static void main(String args[]) {

        MaxAreaOfIsland ma = new MaxAreaOfIsland();

        int grid[][] = { { 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0 },
                { 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0 },
                { 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 } };

        // int grid[][] = { { 0, 0, 0, 0, 0, 0, 0, 0 } };

        System.out.println(ma.maxArea(grid));
        // ma.maxArea(grid);

    }
}
