package java_course.Matrix;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[][] matrix1 = {{1, 2, 3}, {4, 5, 6}};
        int[][] matrix2 = {{7, 8, 9}, {10, 11, 12}};
    
        // транспонирование
        int[][] transposed = MatrixOperations.transpose(matrix1);
        System.out.println(Arrays.deepToString(transposed));
    
        // сложение матриц
        int[][] sum = MatrixOperations.add(matrix1, matrix2);
        System.out.println(Arrays.deepToString(sum));
    
        // умножение на скаляр
        int[][] multiplied = MatrixOperations.multiplyByScalar(matrix1, 2);
        System.out.println(Arrays.deepToString(multiplied));
    }
    
    
}
