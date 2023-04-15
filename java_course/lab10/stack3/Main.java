package java_course.lab10.stack3;

import java.util.LinkedList;

public class Main{
    public static void main(String[] args) {
    LinkedStack<Number> stack = new LinkedStack<>();
    stack.push(1);
    stack.push(2.5);
    stack.push(3);
    stack.push(4.2);

    System.out.println("Stack elements: " + stack);
    System.out.println("Stack size: " + stack.size());
    System.out.println("Stack is empty: " + stack.isEmpty());
    System.out.println("Stack peek: " + stack.peek());

    LinkedList<Number> list = LinkedStack.createLinkedList(stack);
    System.out.println("Linked list: " + list);
    }
}