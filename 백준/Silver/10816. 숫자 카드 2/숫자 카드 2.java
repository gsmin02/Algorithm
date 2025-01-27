import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		Map<Integer, Integer> map = new HashMap<>();
		
		int num1 = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < num1; i++ ) {
			int val = Integer.parseInt(st.nextToken());
			if(map.containsKey(val)) {
				map.put(val, map.get(val) + 1);
			}
			else {
				map.put(val, 1);
			}
		}
		
		int num2 = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < num2; i++ ) {
			int val = Integer.parseInt(st.nextToken());
			if(map.containsKey(val)) {
				sb.append(map.get(val)).append(' ');
			}
			else {
				sb.append(0).append(' ');
			}
		}
		
		System.out.println(sb.toString());
	}

}
