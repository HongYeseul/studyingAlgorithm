import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

// 풀이 참고: https://lotuslee.tistory.com/105

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());

        Stack<Pair> stack = new Stack<>();
        long cnt = 0;

        for (int i = 0; i<N; i++){
            Pair input = new Pair(Integer.parseInt(br.readLine()), 1);

            while (!stack.empty() && stack.peek().height <= input.height) {
                Pair top = stack.pop();
                cnt += top.cnt;

                if (top.height == input.height) {
                    input.cnt += top.cnt;
                }
            }

            if (!stack.empty()) {
                cnt++;
            }
            stack.push(input);
        }
        
        bw.write(cnt + "\n");
        bw.flush();
    }

    static class Pair {
        int height;
        int cnt;

        Pair(int height, int cnt) {
            this.height = height;
            this.cnt = cnt;
        }
    }
}
