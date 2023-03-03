package java_course;

public class ArithmeticValidation {
    public static void main(String[] args) {
        String expression = "6";
        
        boolean isValid = isValidExpression(expression);
        if (isValid) {
            System.out.println("expression is valid");
        } else {
            System.out.println("expression is invalid");
        }
    }
    
    private static boolean isValidExpression(String expression) {
        if (expression == null || expression.isEmpty()) {
            return false;
        }
        
        String regex = "^\\s*(\\-?\\d+(\\.\\d+)?\\s*([-+*/]\\s*\\d+(\\.\\d+)?\\s*)*)$";
        return expression.matches(regex);
    }

}
