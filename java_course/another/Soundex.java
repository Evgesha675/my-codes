package java_course.another;
public class Soundex {
    public static void main(String[] args) {
        String word1 = "Hello";
        String word2 = "Hallo";
        
        String code1 = soundex(word1);
        String code2 = soundex(word2);
        
        if (code1.equals(code2)) {
            System.out.println("Words are phonetically similar");
        } else {
            System.out.println("Words are not phonetically similar");
        }
    }
    
    public static String soundex(String word) {
        if (word == null || word.isEmpty()) {
            return "";
        }
        
        char[] wordChars = word.toUpperCase().toCharArray();
        char firstChar = wordChars[0];
        
        for (int i = 0; i < wordChars.length; i++) {
            switch (wordChars[i]) {
                case 'B':
                case 'F':
                case 'P':
                case 'V':
                    wordChars[i] = '1';
                    break;
                case 'C':
                case 'G':
                case 'J':
                case 'K':
                case 'Q':
                case 'S':
                case 'X':
                case 'Z':
                    wordChars[i] = '2';
                    break;
                case 'D':
                case 'T':
                    wordChars[i] = '3';
                    break;
                case 'L':
                    wordChars[i] = '4';
                    break;
                case 'M':
                case 'N':
                    wordChars[i] = '5';
                    break;
                case 'R':
                    wordChars[i] = '6';
                    break;
                default:
                    wordChars[i] = '0';
                    break;
            }
        }
        
        StringBuilder sb = new StringBuilder();
        sb.append(firstChar);
        
        for (int i = 1; i < wordChars.length; i++) {
            if (wordChars[i] != '0' && wordChars[i] != wordChars[i-1]) {
                sb.append(wordChars[i]);
            }
        }
        
        while (sb.length() < 4) {
            sb.append('0');
        }
        
        return sb.toString();
    }
}

