import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int n1 = Integer.parseInt(st.nextToken());
		int n2 = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int n3 = Integer.parseInt(st.nextToken());
		int n4 = Integer.parseInt(st.nextToken());
		
		int num1 = (n1 * n4) + (n2 * n3);
		int num2 = n2 * n4;
		
		int result = gcd(num1, num2);
		num1 /= result;
		num2 /= result;
		
		System.out.println(num1 + " " + num2);
	}
	public static int gcd(int a, int b) {
		if(a % b == 0) {
			return b;
		}
		return gcd(b, a % b);
	}

}
