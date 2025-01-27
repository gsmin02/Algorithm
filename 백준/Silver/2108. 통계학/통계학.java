import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int num = Integer.parseInt(br.readLine());
		int[] arr = new int[num];
		double sum = 0;
		
		for(int i = 0; i < num; i++) {
			arr[i] = Integer.parseInt(br.readLine());
			sum += arr[i];
		}
		
		Arrays.sort(arr);
		int cnt = 0;
		int max_cnt = -1;
		int fval = arr[0];
		boolean chk = false;
		
		for(int i = 0; i < num - 1; i++) {
			if(arr[i] == arr[i+1]) {
				cnt++;
			}
            else {
				cnt = 0;
			}
			
			if(max_cnt < cnt) {
				max_cnt = cnt;
				fval = arr[i];
				chk = true;
			}
			else if(max_cnt == cnt && chk == true) {
				fval = arr[i];
				chk = false;
			}
		}
		
		System.out.println(Math.round(sum / num));
		System.out.println(arr[(num-1) / 2]);
		System.out.println(fval);
		System.out.println(arr[num-1] - arr[0]);
	}

}
