import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		int[][] arr = new int[num][2];
		
		for(int i = 0; i < num; i++) {
			arr[i][1] = sc.nextInt();
			arr[i][0] = sc.nextInt();
		}
		
		Arrays.sort(arr, (a, b) -> {
			if(a[0] == b[0]) {
				return a[1] - b[1];
			} else {
				return a[0] - b[0];
			}
		});
		
		for(int i = 0; i < num; i++) {
			System.out.println(arr[i][1] + " " + arr[i][0]);
		}
		sc.close();
    }
}
