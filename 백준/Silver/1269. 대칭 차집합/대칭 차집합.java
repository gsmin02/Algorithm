import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int num1 = Integer.parseInt(st.nextToken());
		int num2 = Integer.parseInt(st.nextToken());
		
		Set<Integer> setA = new HashSet<>();
		Set<Integer> setB = new HashSet<>();
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < num1; i++) {
			int num = Integer.parseInt(st.nextToken());
			setA.add(num);
		}
		st = new StringTokenizer(br.readLine());
		for(int i = 0; i < num2; i++) {
			int num = Integer.parseInt(st.nextToken());
			setB.add(num);
		}
		
		Set<Integer> set_all = new HashSet<>(setA);
		set_all.addAll(setB);
		Set<Integer> set_ret = new HashSet<>(setA);
		set_ret.retainAll(setB);
		
		System.out.println(set_all.size() - set_ret.size());
	}

}
