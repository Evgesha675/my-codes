import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {

    public static boolean isValid(String s) {
        String regex = "\\(\\)|\\{\\}|\\[\\]";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(s);

        while (matcher.find()) {
            s = s.replaceAll(regex, "");
            matcher = pattern.matcher(s);
        }

        return s.isEmpty();
    }

    public static void main(String[] args) {
        String expression1 = "([]{})";
        String expression2 = "([)]";

        System.out.println("Expression 1 is valid: " + isValid(expression1)); // Output: true
        System.out.println("Expression 2 is valid: " + isValid(expression2)); // Output: false
    }
}
