import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int result = 0;
		
		boolean[][] arr = new boolean[101][101];
		
		for(int i = 0; i < num; i++) {
			int num1 = sc.nextInt();
			int num2 = sc.nextInt();
			
			for(int j = num1; j < num1 + 10; j++) {
				for(int k = num2; k < num2 + 10; k++) {
					if(!arr[j][k]) {
						arr[j][k] = true;
						result++;
					}
				}
			}
		}
		System.out.println(result);
		sc.close();
		
	}

}
