import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());

        int result = solve(N, x, y);
        bw.write(result + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

    private static int solve(int N, int x, int y) {
        int result = 0;

        while (N != 0) {
            N--;

            int powOfN = (int)Math.pow(2, N);
            if (x < powOfN && y < powOfN) { // 1사분면
                result += 0;
            }
            else if (x < powOfN && y >= powOfN) {
                // 2사분면: y가 클 때
                result += (powOfN * powOfN) * 1;
                y -= powOfN;
            }
            else if (x >= powOfN && y < powOfN) { 
                // 3사분면: x가 클 때
                result += (powOfN * powOfN) * 2;
                x -= powOfN;
            }
            else { // 4사분면
                result += (powOfN * powOfN) * 3;
                x -= powOfN;
                y -= powOfN;
            }
        }

        return result;
    }
}
