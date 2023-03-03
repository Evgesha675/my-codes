package java_course;

import java.util.Arrays;

public class Palindromes {
    public static void main(String[] args) {
        String str = "кабак упал и лапупал нан бок ";
        int[] palindromes = findPalindromes(str);

        System.out.print("Palindromes: ");
        for (int i = 0; i < palindromes.length; i++) {
            System.out.print(palindromes[i]+1 + " ");
        }
    }

    public static int[] findPalindromes(String str) {
        String[] words = str.split(" ");
        int[] palindromes = new int[words.length];
        int count = 0;

        for (int i = 0; i < words.length; i++) {
            if (isPalindrome(words[i])) {
                palindromes[count++] = i;
            }
        }

        return Arrays.copyOf(palindromes, count);
    }

    public static boolean isPalindrome(String str) {
        int left = 0;
        int right = str.length() - 1;

        while (left < right) {
            if (str.charAt(left++) != str.charAt(right--)) {
                return false;
            }
        }

        return true;
    }
}
