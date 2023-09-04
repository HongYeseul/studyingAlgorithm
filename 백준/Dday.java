package 백준;
// #1308 D-Day(https://www.acmicpc.net/problem/1308)

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Dday {
    
    public static boolean isLeap(int year){
        if(year%4 ==0){
            if(year%100 == 0)
                return year%400 == 0? true:false;
            else return true;
        }else return false;
    }


    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int [] commonYear = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int [] leapYear = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};        

        int [] today = new int [3];
        int [] Dday = new int [3];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<3; i++){
            today[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<3; i++){
            Dday[i] = Integer.parseInt(st.nextToken());
        }

        int sum = 0;
        // 오늘, D-day의 년도는 제외하고 해당 년도의 날짜 수 세기
        for(int year=today[0]; year<=Dday[0]; year++){
            for(int month=1; month<=12; month++){
                if(year == today[0] && month<=today[1]){ continue; } // 오늘의 년도 pass
                else if(year == Dday[0] && month == Dday[1]){ break; } // d-day년도 pass

                if(isLeap(year)){ // 윤년이었을 때 해당 달의 일 수 더하기
                    sum+=(leapYear[month]);
                }else{ // 평년이었을 때 해당 달의 일 수 더하기
                    sum+=(commonYear[month]);
                }
            }
        }

        // 윤년인지 파악 후 해당 달의 시작 날(오늘 날짜의 day)~마지막 날
        int startDate = 0;
        if(isLeap(today[0])){ // 오늘 날짜의 년도가 윤년인지 확인
            startDate = leapYear[today[1]]; // 
        }else{ startDate = commonYear[today[1]]; }
        sum+=(startDate-today[2]);
        
        sum+=Dday[2]; // D-day의 일 수 더하기

        if(sum >= 365243) System.out.println("gg");
        else System.out.println("D-"+sum);
    }
}
