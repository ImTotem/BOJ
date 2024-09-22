import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        char[][] words = new char[5][15];

        for (int i = 0; i < 5; i++) {
            words[i] = scanner.next().toCharArray();
        }

        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < 15; i++) {
            for (int j = 0; j < 5; j++) {
                if (words[j].length - 1 < i)
                    continue;
                answer.append(words[j][i]);
            }
        }

        System.out.println(answer);
    }
}
