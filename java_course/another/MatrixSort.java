package java_course.another;

import java.util.Scanner;

public class MatrixSort {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите количество строк матрицы: ");
        int rows = scanner.nextInt();

        System.out.print("Введите количество столбцов матрицы: ");
        int cols = scanner.nextInt();

        int[][] matrix = new int[rows][cols];

        // Заполнение матрицы с клавиатуры
        System.out.println("Введите элементы матрицы:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }

        // Сортировка строк матрицы по возрастанию суммы элементов
        for (int i = 0; i < rows - 1; i++) {
            int minSumRowIndex = i;
            int minSumRowSum = getRowSum(matrix[minSumRowIndex]);

            for (int j = i + 1; j < rows; j++) {
                int currentRowSum = getRowSum(matrix[j]);
                if (currentRowSum < minSumRowSum) {
                    minSumRowIndex = j;
                    minSumRowSum = currentRowSum;
                }
            }

            if (minSumRowIndex != i) {
                swapRows(matrix, i, minSumRowIndex);
            }
        }

        // Вывод отсортированной матрицы
        System.out.println("Отсортированная матрица:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }

        scanner.close();
    }

    // Метод для нахождения суммы элементов строки матрицы
    private static int getRowSum(int[] row) {
        int sum = 0;
        for (int i = 0; i < row.length; i++) {
            sum += row[i];
        }
        return sum;
    }

    // Метод для обмена местами двух строк матрицы
    private static void swapRows(int[][] matrix, int i, int j) {
        int[] temp = matrix[i];
        matrix[i] = matrix[j];
        matrix[j] = temp;
    }
}
