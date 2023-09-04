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
            if(data[i] == x){
                System.out.println("0");
                return;
            }else if(data[i] < x && x < data[i+1]){
                smallest = data[i]; highest = data[i+1];
                break;
            }
        }
        if(data[0]>x) highest = data[0];

        System.out.println(smallest +" "+ highest + " x = " + x);
        System.out.println("========계산========");

        int sum = 0;
        for(int i=(smallest+1); i<=x; i++){
            System.out.println("i= " + i + " highest= "+(highest-1)+ " x = "+ x);
            System.out.println("sum: "+ sum);
            sum+=( (highest-1) -i);
        }

        System.out.println(sum);
    }
}
