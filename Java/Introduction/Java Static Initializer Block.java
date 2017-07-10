//Write your code here
public static int B,H;
public static boolean flag;
static {
    Scanner scan = new Scanner(System.in);
    B = scan.nextInt();
    H = scan.nextInt();
    if(B<=0||H<=0){
        flag=false;
        System.out.print("java.lang.Exception: Breadth and height must be positive");
    }
    else {
        flag=true;
    }
}