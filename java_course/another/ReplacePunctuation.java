package java_course;

public class ReplacePunctuation {
    public static void main(String[] args) {
        String str = "Just a sentences for code! ! !";
        String result = str.replaceAll("[\\p{Punct}]", " ");

        System.out.println("Original string: " + str);
        System.out.println("Result string: " + result);
    }
    
}
