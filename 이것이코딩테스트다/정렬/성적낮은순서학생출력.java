package 이것이코딩테스트다.정렬;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 성적낮은순서학생출력 {

    public static void bubbleSort(String[] name, Integer[] grade){
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

    public static void quickSort(Integer[] grade, String[] name, Integer start, Integer end){
        if(start>=end) return;

        int pivot = start;
        int left = start+1, right = end;

        while(left<=right){
            while(left<=end && grade[pivot]>=grade[left]){
                left++;
            }
            while(right>start && grade[pivot]<=grade[right])
                right--;
            
            if(left>right){
                // swap [pivot] <> [right]
                int tempG = grade[pivot];
                grade[pivot] = grade[right];
                grade[right] = tempG;

                String tempN = name[pivot];
                name[pivot]= name[right];
                name[right] = tempN;
            }else{
                // swap [left] <> [right]
                int tempG = grade[left];
                grade[left] = grade[right];
                grade[right] = tempG;

                String tempN = name[left];
                name[left]= name[right];
                name[right] = tempN;
            }
        }

        quickSort(grade, name, start, right-1);
        quickSort(grade, name, left+1, end);
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

        // bubbleSort(name, grade);
        quickSort(grade, name, 0, n-1);

        System.out.println("Sorting ...");

        for(int i=0; i<n; i++)
            System.out.println(name[i]+" "+grade[i]);
    }
}
