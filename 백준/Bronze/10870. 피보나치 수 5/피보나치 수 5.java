import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int size = 20;
		int[] arr = new int[size + 1];
		
		arr[0] = 0;
		arr[1] = 1;
		for(int i = 2; i <= size; i++) {
			arr[i] = arr[i - 1] + arr[i - 2];
		}
		
		int num = Integer.parseInt(br.readLine());
		System.out.println(arr[num]);
		
	}

}
