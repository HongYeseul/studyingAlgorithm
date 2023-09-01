package 백준;
// #1181 단어정렬(https://www.acmicpc.net/problem/1181)

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class 단어정렬 {
    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        String [] data = new String[n];
        StringTokenizer st;

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            data[i] = st.nextToken().toString();
        }


        // List를 다중조건으로 정렬하는 방법: Comparator & .thenComparing()의 사용 !
        Arrays.sort(data, Comparator.comparingInt(String::length).thenComparing(String::valueOf));
        // 다중조건 사용 x, 길이만으로 정렬
        // Arrays.sort(data, (a, b)->Integer.compare(a.length(), b.length()) );

        // System.out.println("** 출력");
        for(int i=0; i<n; i++){
            if(i!=(n-1) && data[i].equals(data[i+1]))
                continue;
            System.out.println(data[i]);
        }

    }
}
