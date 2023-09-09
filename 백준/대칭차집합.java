package 백준;
// #1269 대칭 차집합 (https://www.acmicpc.net/problem/1269)

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class 대칭차집합 {
    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int aNum = Integer.parseInt(st.nextToken());
        int bNum = Integer.parseInt(st.nextToken());

        Set<Integer> setA = new HashSet<Integer>();
        Set<Integer> setB = new HashSet<Integer>();

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<aNum; i++){
            setA.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<bNum; i++){
            setB.add(Integer.parseInt(st.nextToken()));
        }

        int result = 0;

        for (Integer a : setA) {
            if(!setB.contains(a))
                result++;
        }

        for (Integer b : setB) {
            if(!setA.contains(b))
                result++;
        }

        System.out.println(result);
    }
}
