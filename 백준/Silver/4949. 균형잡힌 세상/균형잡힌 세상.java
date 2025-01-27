import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while(true) {
			String str = br.readLine();
			if(str.equals(".")) {
				break;
			}
			
			Stack<Character> stack = new Stack<>();
			boolean chk = true;
			
			for(char ch : str.toCharArray()) {
				if(ch == '(' || ch == '[') {
					stack.push(ch);
				} else if(ch == ')' || ch == ']') {
					if(stack.isEmpty()) {
						chk = false;
						break;
					}
					
					char top = stack.pop();
					if((ch == ')' && top != '(') || (ch == ']' && top != '[')) {
						chk = false;
						break;
					}
				}
			}
			
			if(!stack.isEmpty()) {
				chk = false;
			}
			
			if(chk) {
				System.out.println("yes");
			} else {
				System.out.println("no");
			}
		}
	}

}
