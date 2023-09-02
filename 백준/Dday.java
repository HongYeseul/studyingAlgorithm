package 백준;
// #1308 D-Day(https://www.acmicpc.net/problem/1308)

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Calendar;
import java.util.StringTokenizer;

public class Dday {
    
    public static void main(String[] args) throws Exception{
        // 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
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

        

        Calendar todayTz = Calendar.getInstance();
        Calendar DdayTz =Calendar.getInstance();

        todayTz.set(today[0], today[1], today[2]);
        DdayTz.set(Dday[0], Dday[1], Dday[2]);

        long cnt_dday = DdayTz.getTimeInMillis();
        long cnt_today = todayTz.getTimeInMillis();
        long result = cnt_dday - cnt_today;
        result = result / 1000 / 60 / 60 / 24;

        if(Dday[0] > (today[0]+1000)){ // 1000년 보다 많이 남았을 경우
            System.out.println("gg");
            return;
        }else if(Dday[0]==(today[0]+1000) && Dday[1]>=today[1] && Dday[2] >= today[2]){ // 1000년 차이 날 경우
            System.out.println("gg");
            return;
        }else System.out.println("D-"+(int)result);
        // if(result >= 365243) System.out.println("gg");
        // else System.out.println("D-"+(int)result);
        
    }
}
