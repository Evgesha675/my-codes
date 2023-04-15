package java_course.lab10.stack3;

import java.util.LinkedList;
import java.util.NoSuchElementException;

public class LinkedStack<E> {

    private Node<E> top;
    private int size;

    public void push(E data) {
        Node<E> node = new Node<>(data, top);
        top = node;
        size++;
    }

    public E pop() {
        if (isEmpty()) {
            throw new NoSuchElementException("Stack is empty");
        }
        Node<E> node = top;
        top = top.next;
        size--;
        return node.data;
    }

    public E peek() {
        if (isEmpty()) {
            throw new NoSuchElementException("Stack is empty");
        }
        return top.data;
    }

    public int size() {
        return size;
    }

    public void clear() {
        top = null;
        size = 0;
    }

    public boolean isEmpty() {
        return top == null;
    }

    public static <E> LinkedList<E> createLinkedList(LinkedStack<E> stack) {
        LinkedList<E> list = new LinkedList<>();
        Node<E> node = stack.top;
        while (node != null) {
            list.addFirst(node.data);
            node = node.next;
        }
        return list;
    }

    private static class Node<E> {
        E data;
        Node<E> next;

        Node(E data, Node<E> next) {
            this.data = data;
            this.next = next;
        }
    }
}
