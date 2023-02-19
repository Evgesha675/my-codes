package my_codes;
//dsdsds

import java.util.*;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите выражение: ");
        String input = scanner.nextLine();
        scanner.close();

        List<String> postfix = infixToPostfix(input);
        double result = evaluatePostfix(postfix);

        System.out.println("Результат: " + result);
    }

    private static List<String> infixToPostfix(String input) {
        List<String> postfix = new ArrayList<>();
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);

            if (Character.isDigit(c)) {
                String number = "" + c;
                while (i < input.length() - 1 && Character.isDigit(input.charAt(i + 1))) {
                    number += input.charAt(i + 1);
                    i++;
                }
                postfix.add(number);
            } else if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                while (!stack.isEmpty() && stack.peek() != '(') {
                    postfix.add(stack.pop().toString());
                }
                stack.pop();
            } else if (isOperator(c)) {
                while (!stack.isEmpty() && getPrecedence(stack.peek()) >= getPrecedence(c)) {
                    postfix.add(stack.pop().toString());
                }
                stack.push(c);
            }
        }

        while (!stack.isEmpty()) {
            postfix.add(stack.pop().toString());
        }

        return postfix;
    }

    private static double evaluatePostfix(List<String> postfix) {
        Stack<Double> stack = new Stack<>();

        for (String token : postfix) {
            if (isOperator(token.charAt(0))) {
                double b = stack.pop();
                double a = stack.pop();
                double result = performOperation(token.charAt(0), a, b);
                stack.push(result);
            } else {
                double number = Double.parseDouble(token);
                stack.push(number);
            }
        }

        return stack.pop();
    }

    private static boolean isOperator(char c) {
        return c == '+' || c == '-' || c == '*' || c == '/';
    }

    private static int getPrecedence(char operator) {
        switch (operator) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            default:
                return 0;
        }
    }

    private static double performOperation(char operator, double a, double b) {
        switch (operator) {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '*':
                return a * b;
            case '/':
                return a / b;
            default:
                return 0;
        }
    } 
   
}
