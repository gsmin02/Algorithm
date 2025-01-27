import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int size = 20;
		long[] arr = new long[size + 1];

		for(int i = 1; i <= size; i++) {
			if(i == 1) arr[i - 1] = i;
			
			arr[i] = arr[i - 1] * i;
		}
		
		int num = Integer.parseInt(br.readLine());
		System.out.println(arr[num]);
		
	}

}
