package java_course;

import java.util.Scanner;

public class MatrixCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Ввод размеров первой матрицы
        System.out.println("Введите размеры первой матрицы (строки столбцы):");
        int m1 = scanner.nextInt();
        int n1 = scanner.nextInt();
        double[][] matrix1 = new double[m1][n1];

        // Ввод элементов первой матрицы
        System.out.println("Введите элементы первой матрицы:");
        for (int i = 0; i < m1; i++) {
            for (int j = 0; j < n1; j++) {
                matrix1[i][j] = scanner.nextDouble();
            }
        }

        // Ввод размеров второй матрицы
        System.out.println("Введите размеры второй матрицы (строки столбцы):");
        int m2 = scanner.nextInt();
        int n2 = scanner.nextInt();
        double[][] matrix2 = new double[m2][n2];

        // Ввод элементов второй матрицы
        System.out.println("Введите элементы второй матрицы:");
        for (int i = 0; i < m2; i++) {
            for (int j = 0; j < n2; j++) {
                matrix2[i][j] = scanner.nextDouble();
            }
        }

        // Проверка возможности сложения/вычитания матриц
        if (m1 != m2 || n1 != n2) {
            System.out.println("Сложение/вычитание матриц невозможно!");
        } else {
            // Выполнение сложения/вычитания матриц
            double[][] sum = addMatrices(matrix1, matrix2);
            double[][] difference = subtractMatrices(matrix1, matrix2);

            // Вывод результатов сложения/вычитания
            System.out.println("Сумма матриц:");
            printMatrix(sum);
            System.out.println("Разность матриц:");
            printMatrix(difference);
        }

        // Проверка возможности умножения матриц
        if (n1 != m2) {
            System.out.println("Умножение матриц невозможно!");
        } else {
            // Выполнение умножения матриц
            double[][] product = multiplyMatrices(matrix1, matrix2);

            // Вывод результата умножения
            System.out.println("Произведение матриц:");
            printMatrix(product);
        }

        scanner.close();
    }

    // Метод сложения матриц
    private static double[][] addMatrices(double[][] matrix1, double[][] matrix2) {
        int m = matrix1.length;
        int n = matrix1[0].length;
        double[][] sum = new double[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                sum[i][j] = matrix1[i][j] + matrix2[i][j];
            }
        }

        return sum;
    }

    // Метод вычитания матриц
    private static double[][] subtractMatrices(double[][] matrix1, double[][] matrix2){
        int m = matrix1.length;
        int n = matrix1[0].length;
        double[][] difference = new double[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                difference[i][j] = matrix1[i][j] - matrix2[i][j];
            }
        }
    
        return difference;
    }
    
    // Метод умножения матриц
    private static double[][] multiplyMatrices(double[][] matrix1, double[][] matrix2) {
        int m1 = matrix1.length;
        int n1 = matrix1[0].length;
        int m2 = matrix2.length;
        int n2 = matrix2[0].length;
        double[][] product = new double[m1][n2];
    
        for (int i = 0; i < m1; i++) {
            for (int j = 0; j < n2; j++) {
                for (int k = 0; k < n1; k++) {
                    product[i][j] += matrix1[i][k] * matrix2[k][j];
                }
            }
        }
    
        return product;
    }
    
    // Метод вывода матрицы на экран
    private static void printMatrix(double[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
    
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}    
