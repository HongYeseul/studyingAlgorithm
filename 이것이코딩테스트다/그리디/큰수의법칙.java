package 이것이코딩테스트다.그리디;
import java.util.*;

public class 큰수의법칙{
    // 첫번째 시도: 정렬 후 input[2]만큼 for문 반복
    public static void firstTrial(){
        int input[] = {5, 8, 3};
        int arr[] = {2,4,5,4,6};
        int sum = 0;

        // arr 오름차순 정렬
        // (java 기본 라이브러리에는 내림차순이 없으므로 오름차순 후 마지막 두 값을 사용)
        Arrays.sort(arr);

        // arr[0]를 input[1]만큼 반복하는데, input[2]배수 번째라면 arr[1]
        for(int i=0; i<input[1]; i++){
            if( (i+1) % input[2] == 0)
                sum+=arr[ arr.length-2 ];
            else
                sum+=arr[ arr.length-1 ];
        }
        System.out.println(sum);
    }

    public static void secondTrial(){
        //             N, M, K
        int input[] = {5, 8, 3};
        int N = input[0];
        int M = input[1];
        int K = input[2];
        int arr[] = {2,4,5,4,6};
        int sum = 0;
        
        // arr sort
        Arrays.sort(arr);

        // 반복되는 수열의 특징을 이용
        // 반복되는 수열 값
        sum += ( arr[N-1]*K + arr[N-2] );
        // 반복되는 횟수로 곱하기
        sum *= M/(K+1);
        // 반복 수열 그 외 더해야 하는 수
        sum += ( arr[N-1]*(M%(K+1)));

        System.out.println(sum);
    }

    public static void main(String[] args){
        
        firstTrial();
        secondTrial();
    }

}