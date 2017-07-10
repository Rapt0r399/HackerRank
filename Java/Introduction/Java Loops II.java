import java.util.*;
import java.io.*;
import java.lang.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        double arr[][] = new double[t][15];
        int l[] = new int[t];
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            arr[i][0]=a+b;
            for(int j=1;j<n;j++)
                {
                arr[i][j]=arr[i][j-1]+Math.pow(2,j)*b;
            }
            l[i] = n;
        }
        in.close();
        for(int i=0; i<t; i++)
            {
            for(int j=0;j<l[i];j++)
                System.out.print((int)arr[i][j] + " " );
            System.out.println();
        }
    }
}
