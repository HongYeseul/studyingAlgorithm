import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        bw.write((1 << n) - 1 + "\n");
        hanoi(n, 1, 2, 3);
        bw.write(sb.toString());

        bw.flush();
        br.close();
        bw.close();
    }

    private static void hanoi(int num, int start, int mid, int to) {
        if (num == 1) {
            sb.append(start + " " + to + "\n");
            return;
        }

        hanoi(num - 1, start, to, mid);
        sb.append(start + " " + to + "\n");
        hanoi(num - 1, mid, start, to);
    }
}
