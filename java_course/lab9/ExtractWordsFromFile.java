package java_course.lab9;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class ExtractWordsFromFile {
    public static void main(String[] args) {
        String inputFileName = "input.txt";
        String outputFileName = "output.txt";

        try (BufferedReader br = new BufferedReader(new FileReader(inputFileName));
             FileWriter fw = new FileWriter(outputFileName)) {
            String line;
            ArrayList<String> words = new ArrayList<>();
            while ((line = br.readLine()) != null) {
                // Извлекаем слова из строки с помощью регулярного выражения
                String[] lineWords = line.split("\\W+");
                for (String word : lineWords) {
                    // Добавляем слово в список, если оно не пустое
                    if (!word.isEmpty()) {
                        words.add(word);
                    }
                }
            }
            // Сортируем список слов
            Collections.sort(words);
            // Записываем отсортированный список слов в выходной файл
            for (String word : words) {
                fw.write(word + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
