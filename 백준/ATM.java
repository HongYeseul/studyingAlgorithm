package 백준;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class ATM {

    static int sum(int[] data){
        int sum = 0;
        
        for(int i=0; i<data.length; i++){
            for(int j=0; j<=i; j++){
                sum+=data[j];
            }
        }
        return sum;
    }

    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int [] data = new int[n];

        for(int i=0; i<n; i++)
            data[i] = Integer.parseInt(st.nextToken());


        // 정렬
        Arrays.sort(data);

        // 정렬한 값 재귀 적으로 덧셈
        int answer = sum(data);
        System.out.println(answer);

    }
}
