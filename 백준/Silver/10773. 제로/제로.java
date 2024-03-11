import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();
        StringTokenizer st;

        for (int i = 0; i<n; i++){
            st = new StringTokenizer(br.readLine());

            int input = Integer.parseInt(st.nextToken());

            if (input == 0) stack.pop();
            else stack.push(input);
        }

        int result = 0;
        while (!stack.isEmpty()){
            result += stack.pop();
        }

        System.out.println(result);
    }
}
