package 백준.그리디;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 설탕배달 {
    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // %5kg -> N
        int mod5 = n%5;

        // /5kg -> 개수
        int cnt5kg = n/5;

        // mod5%3kg -> return -1
        if(mod5 % 3 > 0 && n%3 != 0){ System.out.println(-1); return;} 

        // /3kg -> 개수
        if(mod5%3 > 0 && n%3 == 0){
            System.out.println(n/3);
        }else
            System.out.println(mod5/3 + cnt5kg);

    }
}
