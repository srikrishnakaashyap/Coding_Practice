import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Question1 {

    static class S {
        int bs = 0;
        public int getbS() {
            return bs;
        }
        public void setbS(int sum) {
            bs = sum;
        }
        int si = 0;
        public int getsI() {
            return si;
        }
        public void setsI(int id) {
            si = id;
        }
        int ii = 0;
        public int getiI() {
            return ii;
        }
        public void setiI(int id) {
            ii = id;
        }

    }
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int D = Integer.parseInt(br.readLine().trim());

        List < Integer > xi = Stream.of(br.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        List < Integer > vi = Stream.of(br.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        br.close();
        int ans = 0;
        List < Integer > x = new ArrayList < > ();
        int[] v = new int[xi.get(xi.size() - 1) + 1];
        for (int i = 0; i < v.length; i++) {
            v[i] = 0;
        }
        for (int i = 0; i < xi.size(); i++) {
            v[xi.get(i)] = vi.get(i);
        }
        S[] dpArray = new S[xi.get(xi.size() - 1) + 1];
        dpArray[0] = new S();
        dpArray[0].setbS(v[0]);
        dpArray[0].setsI(0);
        dpArray[0].setiI(0);

        for (int i = 1; i < dpArray.length; i++) {
            dpArray[i] = new S();
            if (i - D >= 0) {
                if (dpArray[i - D].getbS() + v[i] > dpArray[i - 1].getbS()) {
                    dpArray[i].setsI(dpArray[i - D].getiI());
                    dpArray[i].setiI(i);
                    dpArray[i].setbS(dpArray[i - D].getbS() + v[i]);
                } else {
                    dpArray[i].setsI(dpArray[i - 1].getsI());
                    dpArray[i].setiI(dpArray[i - 1].getiI());
                    dpArray[i].setbS(dpArray[i - 1].getbS());
                }

            } else {
                if (v[i] > dpArray[i - 1].getbS()) {
                    dpArray[i].setsI(i);
                    dpArray[i].setiI(i);
                    dpArray[i].setbS(v[i]);
                } else {
                    dpArray[i].setsI(dpArray[i - 1].getsI());
                    dpArray[i].setiI(dpArray[i - 1].getiI());
                    dpArray[i].setbS(dpArray[i - 1].getbS());
                }
            }

        }
        System.out.println(dpArray[dpArray.length - 1].getbS());
        StringBuilder stringbuilder = new StringBuilder();
        int t = dpArray.length - 1;
        while (dpArray[t].getsI() != dpArray[t].getiI()) {
            stringbuilder.append(xi.indexOf(dpArray[t].getiI()) + 1);
            stringbuilder.append(" ");
            t = dpArray[t].getsI();
        }
        stringbuilder.append(xi.indexOf(dpArray[t].getiI()) + 1);
        System.out.println(stringbuilder.substring(0, stringbuilder.length()).toString());

    }

}