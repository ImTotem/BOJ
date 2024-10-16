import java.io.*;
import java.util.StringTokenizer;

public class Main {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public void solve() throws Exception {
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int max = 0;
        float sum = 0;

        for (int i = 0; i < n; i++) {
            int s = Integer.parseInt(st.nextToken());
            max = Math.max(max, s);
            sum += s;
        }

        System.out.println(sum / max * 100 / n);
    }

    public static void main(String[] args) throws Exception {
        new Main().solve();
    }
}
