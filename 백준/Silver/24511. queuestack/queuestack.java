import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        Deque<Integer> deque = new ArrayDeque<>();
        
        int num1 = Integer.parseInt(br.readLine());
        int[] arr = new int[num1];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < num1; i++){
        	arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < num1; i++){
            int in = Integer.parseInt(st.nextToken());
            if(arr[i] == 0){
                deque.addFirst(in);
            }
        }
        int num2 = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());     
        for(int i = 0; i < num2; i++) {
        	int in = Integer.parseInt(st.nextToken());
            deque.addLast(in);
            sb.append(deque.pollFirst()).append(' ');
        }
        
        System.out.println(sb.toString());
    }
}
