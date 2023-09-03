package java_course;

public class EmailValidation {
    public static void main(String[] args) {
        String email = "example.email@domain.com";
        
        boolean isValid = isValidEmail(email);
        if (isValid) {
            System.out.println("Email is valid");
        } else {
            System.out.println("Email is invalid");
        }
    }
    
    private static boolean isValidEmail(String email) {
        if (email == null || email.isEmpty()) {
            return false;
        }
        
        String regex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$";
        return email.matches(regex);
    }
    
}
/*Регулярное выражение ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$ означает:

    ^ - начало строки
    [a-zA-Z0-9._%+-]+ - любая комбинация букв, цифр, знаков подчеркивания, точек, знаков процента, знаков плюс и минус, длиной от одного символа и более
    @ - символ собаки
    [a-zA-Z0-9.-]+ - любая комбинация букв, цифр, точек и дефисов, длиной от одного символа и более
    \\. - символ точки (требует экранирования т.к. входит в комбинацию всех символов и 
    должен быть выделен отдельно)
    [a-zA-Z]{2,} - любая комбинация букв, длиной от двух символов и более
    $ - конец строки
    метод matches() для проверки строки на соответствие регулярному выражению (возврващает true false)
     */