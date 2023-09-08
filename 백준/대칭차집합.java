package 백준;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
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
        Arrays.sort(a);
        Arrays.sort(b);

        int result = 0;
        for(int i=0; i<aNum; i++){
            if(Arrays.binarySearch(b, a[i])>=0)
                result++;
        }
        for(int i=0; i<bNum; i++){
            if(Arrays.binarySearch(a, b[i])>=0)
                result++;
        }

        System.out.println(result);
    }
}
