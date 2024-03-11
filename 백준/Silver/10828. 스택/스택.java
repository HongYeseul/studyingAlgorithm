import java.io.BufferedReader;
import java.io.InputStreamReader;
// boj 10828
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();
        StringTokenizer st;

        for(int i = 0; i< n; i++) {
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            if (str.equals("push")){
                stack.push(Integer.parseInt(st.nextToken()));
            }
            if (str.equals("pop")){
                if (stack.empty()) System.out.println("-1");
                else System.out.println(stack.pop());
            }
            if (str.equals("size")){
                System.out.println(stack.size());
            }
            if (str.equals("empty")){
                if (stack.empty()) System.out.println("1");
                else System.out.println("0");
            }
            if (str.equals("top")) {
                if (stack.empty()) System.out.println("-1");
                else System.out.println(stack.peek());
            }
        }
    }
}
