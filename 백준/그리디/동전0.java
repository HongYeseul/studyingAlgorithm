package 백준.그리디;

import java.io.*;
import java.util.*;

public class 동전0 {
    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        int [] n = new int[2];
        for(int i=0; i<2; i++)
            n[i] = Integer.parseInt(st1.nextToken());
            
        int [] money = new int[ n[0] ];
        for(int i=0; i<n[0]; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            money[i] = Integer.parseInt(st.nextToken());
        }

        int cnt = 0;

        for(int i=(n[0]-1); i>=0; i--){
            if(n[1] / money[i] >= 1){
                int temp = (n[1] / money[i]);
                cnt += temp;
                n[1] -= (money[i]*temp);
            }
        }
        System.out.println(cnt);
    }
}
