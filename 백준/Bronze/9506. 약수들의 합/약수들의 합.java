import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			int num = sc.nextInt();
			
			if(num == -1)
				break;
			
			int[] arr = new int[num];
			int cnt = 0;
			int result = 0;
			
			for(int i = 1; i < num; i++) {
				if(num % i == 0) {
					arr[cnt] = i;
					cnt++;
					result += i;
				}
			}
			if(result == num) {
				System.out.print(num + " = 1");
				for(int i = 1; i < cnt; i++) {
					System.out.print(" + " + arr[i]);
				}
			}
			else {
				System.out.print(num + " is NOT perfect.");
			}
			System.out.println();
			
		}
		sc.close();
	}
}
