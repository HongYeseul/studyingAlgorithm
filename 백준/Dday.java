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

        // System.out.println("입력값: "+ today[0]+today[1]+today[2]+ " D-day "+ Dday[0]+Dday[1]+Dday[2]);

        int sum = 0;
        for(int year=today[0]; year<=Dday[0]; year++){
            for(int month=1; month<=12; month++){
                if(year == today[0] && month<=today[1]){ continue; }
                else if(year == Dday[0] && month == Dday[1]){ break; }

                // System.out.println(month);
                if(isLeap(year)){
                    sum+=(leapYear[month]);
                }else{
                    sum+=(commonYear[month]);
                }
            }
        }

        // System.out.println("중간점검값: "+ sum);
        int startDate = 0;
        if((today[0]/4)==0 && ((today[0]/100)!=0 || (today[0]/400)==0)){
            startDate = leapYear[today[1]];
        }else{ startDate = commonYear[today[1]]; }

        for(int i=today[2]; i<startDate; i++){
            sum++;
        }
        for(int i=1; i<=Dday[2]; i++){
            sum++;
        }
        
        if(sum >= 365000) System.out.println("gg");
        else System.out.println("D-"+sum);
    }
}
