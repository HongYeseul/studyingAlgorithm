import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        Stack<int[]> stack = new Stack<>(); // [index, value]

        // 탑 높이 입력 받기
        st = new StringTokenizer(br.readLine());
        for(int i = 1; i<=N; i++){
            int input = Integer.parseInt(st.nextToken());

            while (!stack.isEmpty()) {
                // 만약 들어온 수가 top이하의 값일 때 top의 index값 출력(push 하지 않음)
                if (stack.peek()[1] >= input) {
                    System.out.print(stack.peek()[0] + " ");
                    break;
                }
                // 만약 들어온 수가 top값보다 크면 pop()
                stack.pop();
            }

            // stack이 비어있다면 0 출력
            if (stack.isEmpty()) {
                System.out.print("0 ");
            }

            // 들어온 수가 top보다 클 때 push 됨
            stack.push(new int[] {i, input});
        }
    }
}
