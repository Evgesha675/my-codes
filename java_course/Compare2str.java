package java_course;

public class Compare2str {
    public static void main(String... args) {
    String str1 = "Hello";
String str2 = "World";
int result = str1.compareTo(str2);
if (result < 0) {
    System.out.println("Строка " + str1 + " меньше, чем " + str2);
} else if (result > 0) {
    System.out.println("Строка " + str1 + " больше, чем " + str2);
} else {
    System.out.println("Строки " + str1 + " и " + str2 + " равны");
}
    
}
}
