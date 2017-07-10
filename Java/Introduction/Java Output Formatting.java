import java.io.*;

class hack2 {

    public static void main(String[] args)throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	String s[] = new String [3];
	String st[] = new String [3];
	String x[] = new String[3];
	char q;
	int l,i,j,k;
	for(i=0;i<3;i++)
	{
		s[i]=br.readLine();
	}
	System.out.println("================================");
	for(i=0;i<3;i++)
	{
		StringBuffer a = new StringBuffer(s[i]);
		l=a.length();
		for(j=0;j<l;j++)
		{
			q=a.charAt(j);
			if(q==' ')
			{	
				x[i] = a.substring(j+1,l);
				for(k=j;k<15;k++)
				{
					a.insert(j," ");
				}
				st[i]=a.substring(0,15);
				break;
			}
			
		}
	}
	for(i=0;i<3;i++)
	{
		StringBuffer a = new StringBuffer(x[i]);
		l=a.length();
		if(l<3)
		{
			for(j=l;j<3;j++)
			{
				a.insert(0,"0");;
			}
		}
		x[i]=a.substring(0,3);
	}
	for(i=0;i<3;i++)
	{
		System.out.println(""+st[i]+""+x[i]);
	}
	System.out.println("================================");
}
}