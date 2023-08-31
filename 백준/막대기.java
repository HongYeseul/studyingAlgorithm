package 백준;
// #1094  막대기 (https://www.acmicpc.net/problem/1094)

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;

public class 막대기 {
    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(br.readLine());

        ArrayList<Integer> stickArr = new ArrayList<Integer>();
        stickArr.add(64);
        int stickSum = 64;

        while(stickSum > x){ // 막대길이 총합 > x
            // sum(길이 짧은것 절반 자른 값이 더해짐) > x
            int sum = 0;
            stickArr.sort(Comparator.reverseOrder()); // stickArr 내림차순 정렬
            int smallSize = stickArr.get( stickArr.size()-1);
            
            for(int i=0;i<stickArr.size()-1; i++){
                sum+=stickArr.get(i);
            } sum+=(smallSize/2);

            if(sum >= x){ 
                // 한개를 버린다(기존값 지우고 2나누기 한 값 넣음)
                stickArr.remove(stickArr.size()-1);
                stickArr.add(smallSize/2);
                
            }else{ // false: 버리지 않고 둘 다 가진다
                stickArr.remove(stickArr.size()-1);
                stickArr.add(smallSize/2);
                stickArr.add(smallSize/2);
            }

            // stickSum = stickArr 총합(막대길이 총합)
            stickSum = 0;
            for(int i=0; i<stickArr.size(); i++){
                stickSum += stickArr.get(i);
            }
        }

        System.out.println(stickArr.size());
    }
}
