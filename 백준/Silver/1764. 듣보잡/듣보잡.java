import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		TreeSet<String> set = new TreeSet<>();
		TreeSet<String> result = new TreeSet<>();
		
		st = new StringTokenizer(br.readLine());
		int num1 = Integer.parseInt(st.nextToken());
		int num2 = Integer.parseInt(st.nextToken());
		
		for(int i = 0; i < num1; i++) {
			set.add(br.readLine());
		}
		for(int i = 0; i < num2; i++) {
			String str = br.readLine();
			if(set.contains(str)) {
				result.add(str);
			}
		}
		System.out.println(result.size());
		for(String str : result) {
			sb.append(str).append('\n');
		}
		System.out.println(sb.toString());
	}

}
