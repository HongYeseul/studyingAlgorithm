import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer command;
        
        int N = Integer.parseInt(br.readLine());

        Deque<Integer> queue = new ArrayDeque<>();

        for (int i = 0; i<N; i++) {
            command = new StringTokenizer(br.readLine(), " ");
            switch (command.nextToken()) {
                case "push":
                    queue.offer(Integer.parseInt(command.nextToken()));
                    break;
            
                case "pop":
                    Integer item = queue.poll();
                    if (item == null) bw.write("-1" + "\n");
                    else bw.write(item + "\n");
                    break;
                
                case "size" :
                    bw.write(queue.size() + "\n");
                    break;

                case "empty" :
                    if (queue.isEmpty()) bw.write("1" + "\n");
                    else bw.write("0" + "\n");
                    break;

                case "front" :
                    Integer frontItem = queue.peek();
                    if (frontItem == null) bw.write("-1" + "\n");
                    else bw.write(frontItem + "\n");
                    break;
                
                case "back" :
                    Integer backItem = queue.peekLast();
                    if (backItem == null) bw.write("-1" + "\n");
                    else bw.write(backItem + "\n");
                    break;
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
