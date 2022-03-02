public class PowerOfTwo {

    public boolean powerOfTwo(int n) {

        if (n == 0) {
            return false;
        }
        if (n == 1) {
            return true;
        }
        if (n % 2 == 0) {

            return this.powerOfTwo(n / 2);
        } else {
            return false;
        }

    }

    public static void main(String args[]) {

        PowerOfTwo pot = new PowerOfTwo();

        int n = 4;
        System.out.println(pot.powerOfTwo(n));
        // pot.powerOfTwo(n);

    }
}