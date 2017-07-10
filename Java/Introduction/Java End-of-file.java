import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner (System.in);
        int n =0;
        ArrayList<String> mylist = new ArrayList<String>();
        while (sc.hasNext() == true ){
            mylist.add(sc.nextLine());
            n++;
        }
        for(int i=0;i<n;i++) {
            System.out.println(i+1+" " + mylist.get(i));
        }
    }
}