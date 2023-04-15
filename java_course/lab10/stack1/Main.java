package java_course.lab10.stack1;

import java.util.NoSuchElementException;

public class Main {
    public static void main(String[] args) {
        Stack<Number> stack = new Stack<>(5);
        stack.push(1);
        stack.push(2.5);
        stack.push((short) 3);
        System.out.println(stack.size());  // 3
        System.out.println(stack.pop());  // 3
        System.out.println(stack.pop());  // 2.5
        System.out.println(stack.size());  // 1
        stack.push(4L);
        stack.push(5f);
        System.out.println(stack.pop());  // 5.0
        System.out.println(stack.pop());  // 4
        System.out.println(stack.pop());  // 1
        
        try {
            System.out.println(stack.pop());
        } catch (NoSuchElementException e) {
            System.out.println(e.getMessage());  
        }
    }
}

