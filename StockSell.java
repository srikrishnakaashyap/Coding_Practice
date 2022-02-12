public class StockSell {

    public int maxProfit(int[] prices) {
        int length = prices.length;
        int maxProfit = 0;
        int minTillHere = 100000;
        if (length == 1) {
            return 0;
        }

        for (int i = 0; i < length; i++) {
            minTillHere = Math.min(minTillHere, prices[i]);
            // System.out.println("MIN: " + minTillHere);
            maxProfit = Math.max(prices[i] - minTillHere, maxProfit);
            // System.out.println("MAX: " + maxProfit);
        }

        return maxProfit;

    }

    public static void main(String args[]) {

        StockSell ss = new StockSell();
        int[] prices = { 1, 2 };
        System.out.println(ss.maxProfit(prices));
    }
}