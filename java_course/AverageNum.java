package java_course;

import java.util.Scanner;

public class AverageNum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите размер массива: ");
        int size = scanner.nextInt();

        double[] array = new double[size];

        System.out.println("Введите элементы массива:");

        // заполняем массив
        for (int i = 0; i < size; i++) {
            array[i] = scanner.nextDouble();
        }

        // вычисляем среднее значение
        double sum = 0;
        for (int i = 0; i < size; i++) {
            sum += array[i];
        }
        double average = sum / size;

        System.out.println("Среднее значение: " + average);
        scanner.close();

    }
}

