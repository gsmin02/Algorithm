import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int input = sc.nextInt();
		int count = 1;
		int sum = 0;
		
		while(true) {
			if(input <= sum + count) {
				if(count % 2 == 1) {
					System.out.println((count - (input - sum - 1)) + "/" + (input - sum));
					break;
				}
				else {
					System.out.println((input - sum)+"/"+(count - (input - sum - 1)));
					break;
				}
			}
			else {
				sum += count;
				count++;
			}
		}
		
		sc.close();
	}
}
