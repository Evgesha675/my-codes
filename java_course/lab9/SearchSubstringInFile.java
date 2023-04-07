package java_course.lab9;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class SearchSubstringInFile {
    public static void main(String[] args) {
        String fileName = "file.txt"; // имя файла, в котором нужно искать
        String substring = "text"; // подстрока, которую нужно найти
        

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            
            while ((line = br.readLine()) != null) {
                String[] words = line.split("\\s+");
                int index = -1;
                for (int i = 0; i < words.length; i++) {
                    if (words[i].equals(substring)) {
                        index = i + 1; // учитываем, что порядковый номер слова начинается с 1
                        break;
                    }
                }
                if (index != -1) {
                    System.out.println("The word \"" + substring + "\" is the " + index + " word in the string: " + line);
                }
                if (line.contains(substring)) {
                    System.out.println(line.substring(line.indexOf(substring)));
                    System.out.println((line.indexOf(substring)));
                    System.out.println(line);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}    