import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int input_x = sc.nextInt();
		int input_y = sc.nextInt();
		int input_w = sc.nextInt();
		int input_h = sc.nextInt();
		
		int min_x = (input_x * 2 > input_w) ? input_w - input_x : input_x;
		int min_y = (input_y * 2 > input_h) ? input_h - input_y : input_y;
		
		System.out.println((min_x > min_y) ? min_y : min_x);
		sc.close();
	}

}
