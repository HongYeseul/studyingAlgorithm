// 백준 #16439 치킨치킨치킨 (https://www.acmicpc.net/problem/16439)
// 10월 1주차 알고리즘 스터디 과제용 문제1

package 백준.알고리즘_스터디.완전탐색_10월_1째주;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 치킨치킨치킨 {
    public static void main(String[] args) throws IOException {
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int [][] data = new int[N][M];
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++){
                data[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int result = 0;
        for(int i=0; i<M; i++){
            for(int j=0; j<M; j++){
                for(int k=0; k<M; k++){
                    
                    int maxResult = 0;

                    for(int m=0; m<N; m++){
                        int maxi = Math.max(data[m][i], data[m][j]);
                        maxi = Math.max(data[m][k], maxi);

                        maxResult += maxi;
                    }
                    result = Math.max(result, maxResult);
                }
            }
        }

        System.out.println(result);
    }
    
}
