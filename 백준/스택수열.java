// 백준 #1974 스택수열 (https://www.acmicpc.net/problem/1874)

package 백준;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class 스택수열 {
    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        
        int [] data = new int[n];
        StringTokenizer st;

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            data[i] = Integer.parseInt(st.nextToken());
        }

        Stack<Integer> stack = new Stack<>(); //int형 스택 선언
        ArrayList<String> result = new ArrayList<String>();

        int index = 1;
        for(int i=0; i<n; i++){
            while(index<=data[i]){
                stack.push(index++);
                result.add("+");
                // System.out.println("+");
            }
            int s = -1;
            while(s!=data[i]){
                try{
                    s = stack.pop();
                    // System.out.println("-");
                    result.add("-");
                }catch(EmptyStackException e){
                    System.out.print("NO");
                    return;
                }
            }
        }

        for (String string : result) {
            System.out.println(string);
        }
    }
}
