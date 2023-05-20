package java_course.lab11;

import java.util.Arrays;
import java.util.Collection;
import java.util.List;

@FunctionalInterface
interface CollectionOperation<T extends Number, R> {
    R perform(Collection<T> collection);
}

public class Main1 {
    public static void main(String[] args) {
        CollectionOperation<Integer, Integer> minOperation = collection -> {
            if (collection == null || collection.isEmpty()) {
                throw new IllegalArgumentException("Collection is null or empty");
            }
            int min = Integer.MAX_VALUE;
            for (Integer element : collection) {
                int value = element.intValue();
                if (value < min) {
                    min = value;
                }
            }
            return min;
        };

        CollectionOperation<Integer, Integer> maxOperation = collection -> {
            if (collection == null || collection.isEmpty()) {
                throw new IllegalArgumentException("Collection is null or empty");
            }
            int max = Integer.MIN_VALUE;
            for (Integer element : collection) {
                int value = element.intValue();
                if (value > max) {
                    max = value;
                }
            }
            return max;
        };

        List<Integer> numbers = Arrays.asList(5, 3, 7, 1, 9, 2, 8);

        int min = minOperation.perform(numbers);
        int max = maxOperation.perform(numbers);

        System.out.println("Min: " + min);
        System.out.println("Max: " + max);
    }
}
