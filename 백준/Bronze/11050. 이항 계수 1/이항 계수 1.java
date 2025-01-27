import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		
		System.out.println(fac(num1)/(fac(num2) * fac(num1 - num2)));
		sc.close();
	}
	
	public static long fac(long num) {
		long result = 1;
		for(int i = 1; i <= num; i++)
			result *= i;
		return result;
	}

}
