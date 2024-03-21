import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        Deque<Integer> deque = new ArrayDeque<>();

        for (int i = 0; i<N; i++) {
            String input = br.readLine();
            if (input.contains("push_back")) {
                String[] split = input.split(" ");
                deque.add(Integer.parseInt(split[1]));
            }
            else if (input.contains("push_front")) {
                String[] num = input.split(" ");
                deque.addFirst(Integer.parseInt(num[1]));
            }
            else if (input.contains("pop_front")) {
                if (deque.isEmpty()) System.out.println("-1");
                else System.out.println(deque.pollFirst());
            }
            else if (input.contains("pop_back")) {
                if (deque.isEmpty()) System.out.println("-1");
                else System.out.println(deque.pollLast());
            }
            else if (input.contains("size")) {
                System.out.println(deque.size());
            }
            else if (input.contains("empty")) {
                if (deque.isEmpty()) System.out.println(1);
                else System.out.println(0);
            }
            else if (input.contains("front")) {
                if (deque.isEmpty()) System.out.println("-1");
                else System.out.println(deque.getFirst());
            }
            else if (input.contains("back")) {
                if (deque.isEmpty()) System.out.println("-1");
                else System.out.println(deque.getLast());
            }
        }
    }
}
