package 백준;
// #1268 임시반장정하기(https://www.acmicpc.net/problem/1268)

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 임시반장정하기 {
    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int [][] data = new int[n][5];

        StringTokenizer st;
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<5; j++){
                data[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int [][] sameClass = new int[n][n]; // (가로)학생번호->(세로)학생번호
        // : ex.1번학생이 몇 번 학생과 같은 반을 했었는지 나타내는 테이블
        
        // 1. 1학년 기준 1번 학생부터 동일 값이 있는지 찾는다.
        for(int grade=0; grade<5; grade++){
            for(int stuNum=0; stuNum<n; stuNum++){
                // 2. '1.'학생과 같은 반이었던 학생에 표시한다.
                int stuClass = data[stuNum][grade];
                for(int j=0; j<n; j++){
                    if(stuNum!= j && stuClass == data[j][grade]){ // 자신의 반 번호는 무시
                        // sameClass에 저장
                        sameClass[stuNum][j] = 1;
                    }
                }
            }
        }

        // 가로를 기준으로 sameClass Sum값 구하기
        // = 같은 반이었던 학생 수
        int sum = 0;
        int result = 0; // 같은 반이었던 학생 수가 많은 학생 번호 넣을 곳
        for(int i=0; i<n; i++){
            int temp = 0;
            for(int j=0; j<n; j++){
                temp += sameClass[i][j];
            }
            if(sum<temp){
                sum = temp;
                result = i;
            }
        }

        System.out.println(result+1);
    }
}
