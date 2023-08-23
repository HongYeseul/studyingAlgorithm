package 백준;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;
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
        
        int [] classArr = new int[10];
        int [] stuArr = new int[n+1];

        // 학년별 반에 대한 인원수 종합
        for(int i=0; i<5; i++){
            for(int j=0; j<n; j++){
                // System.out.print(data[j][i]);
                classArr[data[j][i]]++;
            }

            // 가장 많은 사람이 있었던 반에 소속 됐던 학생 기록
            int maxIdx = Arrays.stream(classArr).max().getAsInt();

            int maxClass=0;
            for(int j=0; j<10; j++) 
                if(classArr[j] == maxIdx){
                    maxClass = j; break;
                }

            for(int j=0; j<10; j++) System.out.print(classArr[j]);
            System.out.println();

            System.out.println("최대값: "+maxIdx + " 많은 사람 있는 반: "+ maxClass );
            for(int j=0; j<n; j++){
                if(maxIdx == 1) break;
                if(data[j][i] == maxClass) stuArr[j]++;
            } classArr = new int[10];

            System.out.print("학생>> ");
            for(int j=0; j<(n+1); j++) System.out.print(stuArr[j]);
            System.out.println();
        }

        // stuArr에서 가장 높은 값 가지고 있는 학생 찾기
        int maxIdx = Arrays.stream(stuArr).max().getAsInt();

        int result=0;
        for(int j=0; j<10; j++) 
            if(stuArr[j] == maxIdx){
                result = j; break;
            }
        
        System.out.println(result+1);
    }
}
