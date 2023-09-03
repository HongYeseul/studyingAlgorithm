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

        if(n == 1 && data[0] != x){
            System.out.println(data[0]-x-1);
            return;
        }
        int a = 0, b = 0;
        for(int i=0; i<n; i++){
            if(data[i] == x){
                System.out.println("0");
                return;
            }else if(data[i] < x && x < data[i+1]){
                a = data[i]; b = data[i+1];
                break;
            }
        }
        System.out.println(a +" "+ b + " x = " + x);
        System.out.println("========계산========");

        int sum = 0;
        for(int i=(a+1); i<=x; i++){
            System.out.println("i= " + i + " x = "+ x);
            if(i<x){
                for(int j=(x); j<=(b-1); j++){
                    System.out.println("i= " + i + " j= "+j+ " x = "+ x);
                    sum++;
                }
            }else{
                for(int j=(x+1); j<=(b-1); j++){
                    System.out.println("i= " + i + " j= "+j+ " x = "+ x);
                    sum++;
                }
            }
            // if(i <= x){ //
            //     for(int j=i; j<x; j++){
            //         System.out.println("i= " + i + " j= "+j+ " x = "+ x);
            //         sum++;
            //     }System.out.println();
            // }
            // else{ 
            //     break;
            //     // for(int j=i; j<b; j++){
            //     //     System.out.println("i= " + i + " j= "+j+ " x = "+ x);
            //     //     sum++;
            //     // }System.out.println();
            // }
        }

        System.out.println(sum);
    }
}
