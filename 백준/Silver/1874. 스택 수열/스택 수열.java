import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer result = new StringBuffer();

        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();
        StringTokenizer st;
        int[] arr = new int[n];

        // 수열 입력 받기
        for(int i = 0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int standard = 1; // 기준값 선언
        for(int i = 0; i<n;i++) { // 수열 판단 하기
            // 기준값 <= 수열[i]라면 수열 값까지 push
            if (standard <= arr[i]){
                while (standard <= arr[i]) {
                    stack.push(standard++);
                    result.append("+").append("\n");
                }
                stack.pop();
                result.append("-").append("\n");
            }
            else { // pop만 하는 부분
                
                // 만약 스택의 최상단값 > 수열[i]라면 출력할 수 없음
                int num = stack.pop();
                if (num > arr[i]) {
                    System.out.println("NO");
                    return;
                }
                result.append("-").append("\n");
            }
        }

        System.out.print(result);
    }
}
