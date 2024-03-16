import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;

        int [] arr = new int[N];
        for (int i = 0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int [] result = new int [N];
        for (int i = 0; i<N-1; i++) {
            for (int j = i+1; j<N; j++) {
                if (arr[i] > arr[j]) {
                    result[i]++;
                }
                else break;
            }
        }
        long answer = 0;
        for (int i = 0; i<N; i++) {
            // System.out.print(result[i] + " ");
            answer += result[i];
        }
        System.out.println(answer);
    }
}
