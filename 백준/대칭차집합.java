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

        Integer [] a = new Integer[aNum];
        Integer [] b = new Integer[bNum];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<aNum; i++){
            a[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<bNum; i++){
            b[i] = Integer.parseInt(st.nextToken());
        }

        Set<Integer> setA = new HashSet<Integer>(Arrays.asList(a));
        Integer[] arrA = setA.toArray(new Integer[setA.size()]);

        Set<Integer> setB = new HashSet<Integer>(Arrays.asList(b));
        Integer[] arrB = setB.toArray(new Integer[setB.size()]);


        Arrays.sort(arrA);
        Arrays.sort(arrB);

        int result = 0;
        for(int i=0; i<arrA.length; i++){
            if(Arrays.binarySearch(arrB, arrA[i])>=0)
                result++;
        }
        for(int i=0; i<arrB.length; i++){
            if(Arrays.binarySearch(arrA, arrB[i])>=0)
                result++;
        }

        System.out.println(result);
    }
}
