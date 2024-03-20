// 우선순위 큐 사용

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> queue = new PriorityQueue<>((o1, o2) -> {
            int first_abs = Math.abs(o1);
            int second_abs = Math.abs(o2);
            if (first_abs == second_abs)
                return o1 > o2 ? 1 : -1;
            else
                return first_abs - second_abs;
        });

        for (int i = 0; i<N; i++) {
            int input = Integer.parseInt(br.readLine());
            if (input == 0) {
                if (queue.isEmpty()) System.out.println("0");
                else System.out.println(queue.poll());
            }
            else queue.add(input);
        }
    }
}
