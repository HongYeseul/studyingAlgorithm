import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int num = Integer.parseInt(st.nextToken());
        int pow = Integer.parseInt(st.nextToken());
        int mod = Integer.parseInt(st.nextToken());

        System.out.println(pow(num, pow, mod));
    }

    private static long pow(long num, long pow, long mod) {
        if (pow == 0) return 1;

        long x = pow(num, pow/2, mod);
        if (pow % 2 == 0) {
            return x * x % mod;
        }
        return (x * x % mod) * num % mod;
    }
}
