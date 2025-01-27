import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int num = Integer.parseInt(br.readLine());
        Deque<Balloon> deque = new ArrayDeque<>();
		
        st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= num; i++) {
            int move = Integer.parseInt(st.nextToken());
            deque.addLast(new Balloon(i, move));
        }
        
        Balloon current = deque.removeFirst();
        sb.append(current.index).append(' ');
		
        while (!deque.isEmpty()) {
        	int move = current.move;

            if (move > 0) {
            	for (int i = 0; i < move - 1; i++) {
                    deque.addLast(deque.removeFirst());
                }
                current = deque.removeFirst();
            } else {
                for (int i = 1; i < -move; i++) {
                    deque.addFirst(deque.removeLast());
                }
                current = deque.removeLast();
            }

            sb.append(current.index).append(' ');
        }

        System.out.println(sb.toString());
    }
	
}
class Balloon {
    int index;
    int move;

    Balloon(int index, int move) {
        this.index = index;
        this.move = move;
    }
}


