package java_course.lab11;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

public class Main3 {
    public static void main(String[] args) {
        List<Person> people = new ArrayList<>();
        people.add(new Person("Evgenii", 25));
        people.add(new Person("Dasha", 30));
        people.add(new Person("MiroSLAVE", 20));

        // Фильтр по возрасту
        Predicate<Person> ageFilter = person -> person.getAge() >= 25;

        // Фильтрация списка людей по возрасту
        List<Person> filteredPeople = filter(people, ageFilter);

        // Вывод отфильтрованного списка на консоль
        for (Person person : filteredPeople) {
            System.out.println(person.getName() + ", " + person.getAge());
        }
    }

    public static <T> List<T> filter(List<T> list, Predicate<T> predicate) {
        List<T> result = new ArrayList<>();
        for (T element : list) {
            if (predicate.test(element)) {
                result.add(element);
            }
        }
        return result;
    }

    public static class Person {
        private String name;
        private int age;

        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public String getName() {
            return name;
        }

        public int getAge() {
            return age;
        }
    }
}
