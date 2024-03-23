import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        // N과 M 입력
        int[] meta = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] position = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        LinkedList<Integer> deque = new LinkedList<>();

        for (int i = 1; i<=meta[0]; i++) {
            deque.add(i);
        }

        bw.write(String.valueOf(solve(deque, position)));
		bw.newLine();
		
		br.close();
		bw.close();
    }

    private static int solve(LinkedList<Integer> deque, int[] position) {
        int cnt = 0;

        for (int i = 0; i<position.length; i++) {

            if ((deque.size() / 2) >= deque.indexOf(position[i])) {
                // 왼쪽으로 돌리기
                while (deque.getFirst() != position[i]) {
                    deque.addLast(deque.removeFirst());
                    cnt++;
                }
            }
            else {
                // 오른쪽으로 돌리기
                while (deque.getFirst() != position[i]) {
                    deque.addFirst(deque.removeLast());
                    cnt++;
                }
            }
            deque.removeFirst();
        }

        return cnt;
    }
}
