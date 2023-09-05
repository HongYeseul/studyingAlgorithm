package 백준.그리디;
// #1246 온라인판매(https://www.acmicpc.net/problem/1246)

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class 온라인판매 {
    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int eggCnt = Integer.parseInt(st.nextToken());
        int customer = Integer.parseInt(st.nextToken());

        Integer [] auction = new Integer[customer];

        for(int i=0; i<customer; i++){
            st = new StringTokenizer(br.readLine());
            auction[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(auction, Collections.reverseOrder()); // 높은 순 정렬

        int sum = 0;
        int price = 0, i = 0;
        while((i+1)<=eggCnt && i<customer){ // 높은 순으로 값을 계산 해 봄
            int temp = auction[i]*(i+1);
            if(sum<temp){ // 만약 가격을 낮게 책정했는데도 더 높은 sum을 낼 수 있다면 채택
                sum = temp;
                price = auction[i];
            }
            i++;
        }

        System.out.println(price + " " + sum);
    }
}
