import java.util.HashSet;
import java.util.LinkedList;

class Edge {

  int weight;
  graphNode destVertex;

  Edge(graphNode vertex, int weight) {
    this.destVertex = vertex;
    this.weight = weight;
  }

  Edge(graphNode vertex) {
    this.destVertex = vertex;
    this.weight = 1;
  }
}

class graphNode {

  int name;
  LinkedList<Edge> edgeList;
  int previsit;
  int postvisit;

  public graphNode(int name) {
    this.name = name;
    edgeList = new LinkedList<>();
  }

  public LinkedList<Edge> getEdges() {
    return this.edgeList;
  }
}

public class GraphL {

  HashSet<graphNode> nodes;
  static int count;

  GraphL() {
    this.nodes = new HashSet<>();
  }

  public void addVertex(graphNode vertex) {
    this.nodes.add(vertex);
  }

  public void addEdge(graphNode vertex1, graphNode vertex2, int weight) {
    Edge e1 = new Edge(vertex2, weight);
    Edge e2 = new Edge(vertex1, weight);

    vertex1.getEdges().add(e1);
    vertex2.getEdges().add(e2);
  }

  public void printGraph() {
    for (graphNode v : this.nodes) {
      System.out.print(
        "Vertex: " + v.name + " " + v.previsit + " " + v.postvisit + " Edges: "
      );

      for (Edge v2 : v.getEdges()) {
        System.out.print(v2.destVertex.name + " ");
      }
      System.out.println();
    }
  }

  public void dfs() {
    int[] visited = new int[this.nodes.size()];
    // int count = 0;

    for (graphNode node : this.nodes) {
      if (visited[node.name] == 0) {
        this.explore(node, visited);
      }
    }
  }

  public void explore(graphNode node, int[] visited) {
    count++;
    node.previsit = count;

    visited[node.name] = 1;

    for (Edge e : node.edgeList) {
      if (visited[e.destVertex.name] == 0) {
        this.explore(e.destVertex, visited);
      }
    }
    count++;
    node.postvisit = count;
  }

  public static void main(String args[]) {
    GraphL graph = new GraphL();

    graphNode v0 = new graphNode(0);
    graphNode v1 = new graphNode(1);
    graphNode v2 = new graphNode(2);
    graphNode v3 = new graphNode(3);

    graph.addVertex(v0);
    graph.addVertex(v1);
    graph.addVertex(v2);
    graph.addVertex(v3);

    graph.addEdge(v0, v1, 1);
    graph.addEdge(v1, v2, 1);
    graph.addEdge(v2, v0, 1);
    graph.addEdge(v2, v3, 1);
    // graph.addEdge(v3, v2, 1);

    // graph.printGraph();

    graph.dfs();

    graph.printGraph();
  }
}
