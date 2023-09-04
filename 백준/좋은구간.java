package 백준;
// #1059 좋은구간(https://www.acmicpc.net/problem/1059)

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 좋은구간 {
    
    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Integer [] data = new Integer[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=0; i<n; i++)
            data[i] = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(br.readLine());

        Arrays.sort(data);

        
        int smallest = 0, highest = 0;
        
        for(int i=0; i<n; i++){
            if(data[i]<x) smallest = data[i];
            else if(data[i]>x && highest == 0) highest = data[i];
            else if(data[i] == x){ System.out.println(0); return; }
        }

        smallest++; highest--;

        // (highest-x) : x ~ highest 범위의 경우의 수
        // (x-smallest)*(highest-x+1) : smallest ~ x ~ heighest 범위의 경우의 수
        int result = (highest - x) + (x-smallest)*(highest-x+1);

        System.out.println(result);
    }
}
