package java_course.lab10.stack2;
public class Main{
public static void main(String[] args) {
    Stack<Number> stack = new Stack<Number>();
    stack.push(1);
    stack.push(2.5);
    stack.push(3);
    stack.push(4.2);

    System.out.print("Stack elements: ");
    Stack.printStack(stack);

    System.out.println("Stack size: " + stack.size());
    System.out.println("Stack is empty: " + stack.isEmpty());
    System.out.println("Stack peek: " + stack.peek());

    double avg = Stack.getAverage(stack);
    System.out.println("Average value of stack elements: " + avg);

    stack.clear();
    System.out.print("Stack elements after clearing: ");
    Stack.printStack(stack);
}
}