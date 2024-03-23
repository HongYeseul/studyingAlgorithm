import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayDeque<Integer> deque;
        
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i<N; i++) {
            // 수행할 함수
            String[] func = br.readLine().split("");
            // 배열에 들어있는 수의 개수
            Integer num = Integer.parseInt(br.readLine());
            // 배열에 들어있는 정수
            StringTokenizer st = new StringTokenizer(br.readLine(), "[],");

            deque = new ArrayDeque<>();
            for (int j = 0; j<num; j++) {
                deque.addLast(Integer.parseInt(st.nextToken()));
            }

            boolean order = true;
            boolean isError = false;
            for (int j = 0; j<func.length; j++) {
                if (func[j].equals("R")) {
                    // 순서 뒤집기
                    order = !order;
                }
                else if (func[j].equals("D")) {
                    // 첫번째 수 버리기
                    if (deque.isEmpty()) {
                        System.out.println("error");
                        isError = true;
                        break;
                    }
                    if (order)
                        deque.removeFirst();
                    else
                        deque.removeLast();
                }
            }

            if(!isError) System.out.print("[");
            while (!deque.isEmpty()) {
                if (order) {
                    if (deque.size() != 1)
                        System.out.print(deque.removeFirst() + ",");
                    else
                        System.out.print(deque.removeFirst());
                }
                else {
                    if (deque.size() != 1)
                        System.out.print(deque.removeLast() + ",");
                    else
                        System.out.print(deque.removeLast());
                }
            }
            if(!isError) System.out.println("]");

        }

        br.close();
        bw.close();
    }
}
