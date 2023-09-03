package java_course.another;

public class Regular1 {
    public static void main(String[] args) {
        String str = "ab12c3d e456fg78h90";
        String result = str.replaceAll("[^0-9\\s]", "");

        System.out.println("Original string: " + str);
        System.out.println("Result string: " + result);
    }
    
}
