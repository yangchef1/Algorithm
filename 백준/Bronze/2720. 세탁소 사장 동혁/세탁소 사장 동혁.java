import java.sql.SQLOutput;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[][] result = new int[N][4];

        for (int i = 0; i < N; i++) {
            int Money = sc.nextInt();
            result[i][0] = Money / 25;
            Money = Money % 25;
            result[i][1] = Money / 10;
            Money = Money % 10;
            result[i][2] = Money / 5;
            result[i][3] = Money % 5;

        }

        for (int i = 0; i < N; i++) {
            for (Integer e: result[i]){
                System.out.printf("%d ",e);
            }
            System.out.println();
        }

    }
}
