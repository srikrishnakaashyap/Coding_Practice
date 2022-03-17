import java.util.LinkedList;
import java.util.Queue;
import java.util.Arrays;
public class GraphM {

    int n;
    int[][] graph;

    GraphM(int n) {
        this.n = n;
        graph = new int[n + 1][n + 1];
    }

    public void addEdge(int source, int destination) {
        // Undirected
        this.graph[source][destination] = 1;
        this.graph[destination][source] = 1;
    }

    public void printGraph(){

        for(int i = 1; i <= this.n; i++) {
            System.out.print("Vertex "+i+": ");

            for(int j = 1; j <= this.n; j++){
                if(this.graph[i][j] == 1){
                    System.out.print(j + " ");
                }
                
            }

            System.out.println();
        }
    }

    public void bfshelper(int source){

        int[] visited = new int[this.n+1];
        Queue<Integer> q = new LinkedList<>();

        visited[source] = 1;
        q.add(source);

        this.bfs(source, visited, q);
        for(int i = 1; i <= this.n; i++) {
            if(visited[i] == 0) {
                q.add(i);
                visited[i] = 1;
                this.bfs(i, visited, q);

            }
        }

    }

    public void bfs(int source, int[] visited, Queue<Integer> q) {

        while(!q.isEmpty()) {

            int vertex = q.poll();

            System.out.println(vertex);

            int[] neighbours = this.graph[vertex];

            for(int j = 1; j <=this.n ; j++) {
                if(neighbours[j] == 1){

                    if(visited[j] == 0){
                        visited[j] = 1;
                        q.add(j);
                    }
                }
            }
        }
    }

    public static void main(String args[]) {

        GraphM g = new GraphM(6);

        // g.addEdge(1, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 4);
        g.addEdge(5, 2);
        g.addEdge(3, 5);
        g.addEdge(4, 5);
        g.addEdge(4, 6);
        g.addEdge(5, 6);

        g.printGraph();

        g.bfshelper(2);


    }

    
}
