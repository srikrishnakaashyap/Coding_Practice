public class Fibonacci {

    public int fib(int n) {

        // if (n == 0) {
        // return 0;
        // }
        if (n == 1) {
            return 0;
        }
        if (n == 2) {
            return 1;
        }
        return fib(n - 1) + fib(n - 2);

    }

    public static void main(String args[]) {

        Fibonacci f = new Fibonacci();

        System.out.println(f.fib(7));
        // f.fib(35);
    }

}
