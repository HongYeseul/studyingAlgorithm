package 백준.그리디;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 설탕배달 {
    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int cnt=0;
        // 5의 배수인가? 아니라면 -3 반복
        while(n!=0){
            if(n%5 == 0){
                n-=5;
                cnt++;
            }else if(n<0){
                System.out.println(-1); return;
            }else{
                n-=3;
                cnt++;
            }
        }
        System.out.println(cnt);

    }
}
