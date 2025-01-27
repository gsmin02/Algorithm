import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int num = Integer.parseInt(br.readLine());
		int arr[] = new int[num];
		
		for(int i = 0; i < num; i++)
			arr[i] = Integer.parseInt(br.readLine());
		
		int min = 0;
		
		for(int i = 1; i < num; i++) {
			int diff = arr[i] - arr[i-1];
			min = gcd(diff, min);
		}
		
		int count = 0;
		
		for(int i = 1; i < num; i++) {
			count += ((arr[i] - arr[i-1]) / min) -1;
		}
		
		System.out.println(count);
	}
	public static int gcd(int a, int b) {
		if(b == 0) {
			return a;
		}
		return gcd(b, a % b);
	}
}
