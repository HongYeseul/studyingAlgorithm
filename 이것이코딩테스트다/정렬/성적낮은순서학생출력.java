package 이것이코딩테스트다.정렬;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 성적낮은순서학생출력 {

    public static void sortFunc(String[] name, Integer[] grade){
        for(int i=0; i<name.length; i++){
            for(int j=0; j<name.length; j++){
                if(grade[i] < grade[j]){
                    int temp = grade[i];
                    grade[i] = grade[j];
                    grade[j] = temp;

                    String tempS = name[i];
                    name[i] = name[j];
                    name[j] = tempS;
                }
            }
        }
    }
    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // Student[] student = new Student[n];
        String [] name = new String [n];
        Integer [] grade = new Integer[n];

        for(int i=0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            name[i] = st.nextToken();
            grade[i] = Integer.parseInt(st.nextToken());
        }

        sortFunc(name, grade);

        for(int i=0; i<n; i++)
            System.out.println(name[i]+grade[i]);
    }
}
