package java_course.lab10.stack2;

import java.util.ArrayList;

public class Stack<T extends Number> {
    private ArrayList<T> list = new ArrayList<T>();

    public void push(T item) {
        list.add(item);
    }

    public T pop() {
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return list.remove(list.size() - 1);
    }

    public T peek() {
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return list.get(list.size() - 1);
    }

    public int size() {
        return list.size();
    }

    public void clear() {
        list.clear();
    }

    public boolean isEmpty() {
        return list.isEmpty();
    }

    public static <T extends Number> double getAverage(Stack<T> stack) {
        double sum = 0.0;
        for (int i = 0; i < stack.size(); i++) {
            sum += stack.list.get(i).doubleValue();
        }
        return sum / stack.size();
    }

    public static void printStack(Stack<? extends Number> stack) {
        for (int i = 0; i < stack.size(); i++) {
            System.out.print(stack.list.get(i) + " ");
        }
        System.out.println();
    }
}
