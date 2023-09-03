package java_course.another;

public class SortString{
    public static void main(String[] args) {
        String[] words = {"wjdnjwdn", "balaboba", "apple", "bba"};

        bubbleSort(words);

        for (String word : words) {
            System.out.println(word);
        }
    }
//простая реализация пузырьком
    public static void bubbleSort(String[] arr) {
        int n = arr.length;
        String temp;
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < (n - i); j++) {
                if (arr[j - 1].compareTo(arr[j]) > 0) {
                    // меняем элементы местами
                    temp = arr[j - 1];
                    arr[j - 1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }
}
//с использованием Arrays
/*
import java.util.Arrays;
import java.util.Collections;

public class SortArray {
    public static void main(String[] args) {
        String[] words = {"apple", "banana", "orange", "pear"};
        
        Arrays.sort(words, Collections.reverseOrder());
        
        for (String word : words) {
            System.out.println(word);
        }
    }
}
 */