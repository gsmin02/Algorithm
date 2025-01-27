import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String arr = sc.next();
		
		int chk = 1;
		
		for(int i = 0; i < arr.length() / 2; i++) {
			if(arr.charAt(i) != arr.charAt(arr.length() - i - 1)) {
				chk = 0;
				break;
			}
		}
		
		System.out.println(chk);
		
		sc.close();
	}

}