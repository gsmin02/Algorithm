import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int num = Integer.parseInt(br.readLine());
        int arrX[] = new int[num];
        int arrY[] = new int[num];

        StringTokenizer st;
        for (int i = 0; i < num; i++) {
        	st = new StringTokenizer(br.readLine());
            arrX[i] = Integer.parseInt(st.nextToken());
            arrY[i] = Integer.parseInt(st.nextToken());
        }

        Sort(arrX, arrY, 0, num - 1);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < num; i++) {
        	sb.append(arrX[i]).append(' ').append(arrY[i]).append('\n');
        }
        System.out.println(sb);
    }

    private static void Sort(int[] arrX, int[] arrY, int min, int max) {
    	while (min < max) {
            int mid = Cut(arrX, arrY, min, max);
            if (mid - min < max - mid) {
            	Sort(arrX, arrY, min, mid - 1);
            	min = mid + 1;
            } else {
            	Sort(arrX, arrY, mid + 1, max);
            	max = mid - 1;
            }
        }
    }

    private static int Cut(int[] arrX, int[] arrY, int min, int max) {
        int mid = min + (max - min) / 2;
        int pX = arrX[mid];
        int pY = arrY[mid];
        Swap(arrX, arrY, mid, max);
        int save = min;

        for (int i = min; i < max; i++) {
            if (arrX[i] < pX || (arrX[i] == pX && arrY[i] < pY)) {
            	Swap(arrX, arrY, i, save);
                save++;
            }
        }
        Swap(arrX, arrY, save, max);
        return save;
    }

    private static void Swap(int[] arrX, int[] arrY, int i, int j) {
        int tempX = arrX[i];
        int tempY = arrY[i];
        arrX[i] = arrX[j];
        arrY[i] = arrY[j];
        arrX[j] = tempX;
        arrY[j] = tempY;
    }
}
