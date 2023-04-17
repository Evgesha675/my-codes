package java_course.lab10.stack1;

import java.util.NoSuchElementException;

public class Stack<E> {
    private E[] array;
    private int top;

    public Stack(int capacity) {
        array = (E[]) new Object[capacity];
        top = -1;
    }

    public void push(E element) {
        if (top == array.length - 1) {
            throw new IllegalStateException("Stack overflow");
        }
        top++;
        array[top] = element;
    }

    public E pop() {
        if (isEmpty()) {
            throw new NoSuchElementException("Stack underflow");
        }
        E element = array[top];
        array[top] = null;
        top--;
        return element;
    }

    public int size() {
        return top + 1;
    }

    public boolean isEmpty() {
        return top == -1;
    }
}