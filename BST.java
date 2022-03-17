class TreeNode {

  int data;
  TreeNode left;
  TreeNode right;
  TreeNode parent;

  TreeNode(int data) {
    this.data = data;
    this.left = this.right = this.parent = null;
  }
}

public class BST {

  TreeNode root;
  int lheight;
  int rheight;

  BST() {
    root = null;
    this.lheight = 0;
    this.rheight = 0;
  }

  public void insert(int data) {
    if (this.root == null) {
      this.root = new TreeNode(data);
      return;
    }
    this.root = this.insertHelper(this.root, data);
  }

  public TreeNode insertHelper(TreeNode root, int data) {
    if (root == null) {
      return new TreeNode(data);
    }

    if (root.data < data) {
      // root.right = this.insertHelper(root.right, data);
      root.right = this.insertHelper(root.right, data);
      root.right.parent = root;
    } else {
      root.left = this.insertHelper(root.left, data);
      root.left.parent = root;
    }
    return root;
  }

  public TreeNode searchHelper(TreeNode root, int data) {
    if (root == null) {
      return null;
    }
    if (root.data == data) {
      return root;
    } else {}
    if (root.data < data) {
      return this.searchHelper(root.right, data);
    }
    return this.searchHelper(root.left, data);
  }

  public TreeNode search(int data) {
    TreeNode answer = this.searchHelper(this.root, data);

    if (answer == null) {
      return null;
    }
    return answer;
  }

  public void preorder() {
    this.preorderhelper(this.root);
  }

  public void preorderhelper(TreeNode root) {
    if (root == null) {
      return;
    }

    this.preorderhelper(root.left);

    if (root.parent != null) System.out.println(
      root.data + " " + root.parent.data
    ); else System.out.println(root.data);
    this.preorderhelper(root.right);
  }

  public static void main(String args[]) {
    BST bst = new BST();

    bst.insert(50);
    bst.insert(30);
    bst.insert(20);
    bst.insert(40);
    bst.insert(70);
    bst.insert(60);
    bst.insert(80);

    bst.preorder();
    // System.out.println(bst.root.left.data);

  }
}
