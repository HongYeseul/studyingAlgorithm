import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Integer> [] node;
    static boolean[] visited;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int nodeN = Integer.parseInt(st.nextToken());
        int endgeN = Integer.parseInt(st.nextToken());
        int result = 0;

        node = new ArrayList[nodeN + 1];
        visited = new boolean[nodeN + 1];

        for (int i = 1; i<nodeN+1; i++){ // 초기화
            node[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i<endgeN; i++) { // 양방향 노드 추가
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            node[start].add(end);
            node[end].add(start);
        }

        for (int i = 1; i<=nodeN; i++) {
            if (!visited[i]) { // 방문하지 않은 노드 방문
                result++;
                dfs(i);
            }
        }

        System.out.println(result);
    }

    static void dfs(int v){
        if (visited[v]){ // 방문한 노드라면 return
            return;
        }
        visited[v] = true;
        // 방문하지 않은 노드 방문
        for (int i: node[v]) {
            if (!visited[i]) {
                dfs(i);
            }
        }
    }
}
