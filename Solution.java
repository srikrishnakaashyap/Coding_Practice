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



public class Solution {
    static class Ct {
        int s;
        int m;
        String d;
    }
    static class Dims {
        int l;
        int b;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] firstMultipleInput = br.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int m = Integer.parseInt(firstMultipleInput[1]);

        br.close();
        if (n == m) {
            System.out.println("0");
            return;
        }
        Ct[][] dparr = new Ct[n+1][m+1];
        for (int ctr1 = 0; ctr1 <= n ; ctr1++) {
            for (int ctr2 = 0; ctr2 <= m ; ctr2++) {
                dparr[ctr1][ctr2] = new Ct();
                if (ctr1==0 || ctr2==0)
                    dparr[ctr1][ctr2].m = 0;
                else if (ctr1 == ctr2)
                {
                    dparr[ctr1][ctr2].m = 0;   
                }
                else{
                    dparr[ctr1][ctr2].m = 214748364;
                }
            }
        }
        
        for (int ctr1 = 0; ctr1 <= n ; ctr1++) {
            for (int ctr2 = 0; ctr2 <= m ; ctr2++) {
                    for (int ctr3 = 0; ctr3 <= ctr1/2; ctr3++) 
                    {
                        if (1 + dparr[ctr3][ctr2].m + dparr[ctr1-ctr3][ctr2].m < dparr[ctr1][ctr2].m)
                        {
                            dparr[ctr1][ctr2].m = 1 + dparr[ctr3][ctr2].m + dparr[ctr1-ctr3][ctr2].m;
                            dparr[ctr1][ctr2].d = "H";
                            dparr[ctr1][ctr2].s = ctr3;
                        }
                    }
                    for (int ctr4 = 0; ctr4 <= ctr2/2; ctr4++) 
                    {
                        if (1 + dparr[ctr1][ctr4].m + dparr[ctr1][ctr2-ctr4].m < dparr[ctr1][ctr2].m)
                        {
                            dparr[ctr1][ctr2].m = 1 + dparr[ctr1][ctr4].m + dparr[ctr1][ctr2-ctr4].m;
                            dparr[ctr1][ctr2].d = "V";
                            dparr[ctr1][ctr2].s = ctr4;
                        }
                    }
                        
                }
                
            }
                     
        System.out.println(dparr[n][m].m);
        // System.out.println(dparr);
        // System.out.println(dparr[0]);
        int l = n; int w = m;
        Stack<Dims> lstdms = new Stack<>();
        Dims d0 = new Dims();
        d0.l = n;
        d0.b = m;
        lstdms.add(d0);  

        while(lstdms.size()>0){
            Dims dim = lstdms.pop();
            l = dim.l;
            w = dim.b;
            System.out.print(dparr[l][w].d);
            System.out.print(" "+l+"x"+w);
            System.out.print(" --> ");
            if(dparr[l][w].d == "V")
            {
                System.out.print(l + "x"+dparr[l][w].s+ " " + l+ "x"+(w-dparr[l][w].s));
                if(l != w - dparr[l][w].s) {
                Dims d1 = new Dims();
                d1.l = l;
                d1.b = w - dparr[l][w].s;
                lstdms.push(d1);  
                }
                if(l != dparr[l][w].s) {
                Dims d = new Dims();
                d.l = l;
                d.b = dparr[l][w].s;
                lstdms.push(d);  
                }
                 
            }
            else if(dparr[l][w].d == "H") {
                System.out.print(dparr[l][w].s + "x"+w+ " " + (l-dparr[l][w].s)+ "x"+w);
                if(l - dparr[l][w].s != w) {
                Dims d1 = new Dims();
                d1.l = l - dparr[l][w].s;
                d1.b = w;
                lstdms.push(d1);  
                }
                if(dparr[l][w].s != w) {
                Dims d = new Dims();
                d.l = dparr[l][w].s;
                d.b = w;
                lstdms.push(d);  
                }
            }
            System.out.println();
            
        }
    }
}