import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Queue<Integer> queue = new LinkedList<>();

        for (int i = 0; i<N; i++) {
            String input = br.readLine();
            if (input.contains("push")) {
                queue.add(Integer.parseInt(input.split(" ")[1]));
            }
            if (input.contains("pop")) {
                if (queue.isEmpty()) System.out.println("-1");
                else System.out.println(queue.poll());
            }
            if (input.contains("size")) {
                System.out.println(queue.size());
            }
            if (input.contains("empty")) {
                System.out.println(queue.isEmpty() ? 1 : 0);
            }
            if (input.contains("front")) {
                if (queue.isEmpty()) System.out.println("-1");
                else System.out.println(queue.peek());
            }
            if (input.contains("back")) {
                if (queue.isEmpty()) System.out.println("-1");
                else {
                    int [] arr = queue.stream().mapToInt(x -> x).toArray();
                    System.out.println(arr[arr.length-1]);
                }
            }
        }
    }
}
