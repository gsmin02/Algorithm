import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int num = Integer.parseInt(br.readLine());
		int result = 0;
		Stack<Integer> stack = new Stack<>();
		
		for(int i = 0; i < num; i++) {
			int in = Integer.parseInt(br.readLine());
			if(in == 0) {
				stack.pop();
			} else {
				stack.add(in);
			}
		}
		while(!stack.isEmpty()) {
			result += stack.pop();
		}
		System.out.println(result);
	}

}
