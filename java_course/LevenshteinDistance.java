package java_course;

public class LevenshteinDistance {
    public static void main(String[] args) {
        String input = "машина Машина ипщтгп трзбщо1f";
        String[] words = input.split(" ");

        // Рассчитываем расстояние Левенштейна между каждой парой слов
        for (int i = 0; i < words.length; i++) {
            for (int j = i + 1; j < words.length; j++) {
                int distance = calculateLevenshteinDistance(words[i], words[j]);
                System.out.printf("Расстояние Левенштейна между словами '%s' и '%s' равно %d%n", words[i], words[j], distance);
            }
        }
    }

    public static int calculateLevenshteinDistance(String s1, String s2) {
        int[][] dp = new int[s1.length() + 1][s2.length() + 1];

        for (int i = 0; i <= s1.length(); i++) {
            for (int j = 0; j <= s2.length(); j++) {
                if (i == 0) {
                    dp[i][j] = j;
                } else if (j == 0) {
                    dp[i][j] = i;
                } else {
                    int substitutionCost = s1.charAt(i - 1) == s2.charAt(j - 1) ? 0 : 1;
                    dp[i][j] = Math.min(dp[i - 1][j] + 1, Math.min(dp[i][j - 1] + 1, dp[i - 1][j - 1] + substitutionCost));
                }
            }
        }
    
        return dp[s1.length()][s2.length()];
    }
}
