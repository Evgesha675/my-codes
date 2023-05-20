package java_course.lab11;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main2 {
    public static void main(String[] args) {
        List<Person> people = new ArrayList<>();
        people.add(new Person("black", "blonde"));
        people.add(new Person("white", "red"));
        people.add(new Person("brown", "black"));
        people.add(new Person("white", null));

        // Компаратор по цвету кожи
        Comparator<Person> bySkinColor = (p1, p2) -> p1.getSkinColor().compareTo(p2.getSkinColor());

        // Компаратор по наличию волос
        Comparator<Person> byHairColor = Comparator.comparing((Person p) -> p.getHairColor(), Comparator.nullsLast(String::compareTo));

        // Сортировка списка людей сначала по цвету кожи, а затем по наличию волос
        Collections.sort(people, bySkinColor.thenComparing(byHairColor));

        // Вывод отсортированного списка на консоль
        for (Person person : people) {
            System.out.println("Skin color: " + person.getSkinColor() + ", hair color: " + person.getHairColor());
        }
    }

    public static class Person {
        private String skinColor;
        private String hairColor;

        public Person(String skinColor, String hairColor) {
            this.skinColor = skinColor;
            this.hairColor = hairColor;
        }

        public String getSkinColor() {
            return skinColor;
        }

        public String getHairColor() {
            return hairColor;
        }
    }
}
