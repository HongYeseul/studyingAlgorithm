package 백준.그리디;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 보물 {
    
    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st1 = new StringTokenizer(br.readLine());
        int [] A = new int[n];
        for(int i=0; i<n; i++)
            A[i] = Integer.parseInt(st1.nextToken());
            
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        int [] B = new int[n];
        for(int i=0; i<n; i++)
            B[i] = Integer.parseInt(st2.nextToken());
        
        Arrays.sort(A);
        Arrays.sort(B);

        int j=n-1;
        int sum = 0; // A는 최소*B는 최대
        for(int i=0; i<n; i++){
            sum+=(A[i]*B[j--]);
        }
        
        System.out.println(sum);
    }
}
