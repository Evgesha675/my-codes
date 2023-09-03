package java_course;

import java.util.Scanner;

public class StringArraySearch {
    public static void main(String[] args) {
        String[] array = {"apple", "banana", "orange", "peach", "pear"};
        Scanner sc = new Scanner(System.in);
        int targetIndex = sc.nextInt();
        sc.close();
        String target = array[targetIndex];

        int foundIndex = -1;
        for (int i = 0; i < array.length; i++) {
            if (array[i].equals(target)) {
                foundIndex = i;
                break;
            }
        }

        if (foundIndex == -1) {
            System.out.println(target + " not found in the array");
        } else {
            System.out.println(target + " found at index " + foundIndex);
        }
    }
}
//or
// public class Main {
//     public static void main(String[] args) {
//         String[] strings = {"one", "two", "three", "four", "five"};
//         String target = "four";
//         boolean found = false;
        
//         for (String s : strings) {
//             if (s.equals(target)) {
//                 found = true;
//                 break;
//             }
//         }
        
//         if (found) {
//             System.out.println("Строка " + target + " найдена в массиве.");
//         } else {
//             System.out.println("Строка " + target + " не найдена в массиве.");
//         }
//     }
// }
