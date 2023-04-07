package java_course.lab9.Seria;

import java.io.*;

public class SerializationExample {
    public static void main(String[] args) {
        Address address1 = new Address("Lenin", 123);
        Person person1 = new Person("Karl", 30, address1);

        Address address2 = new Address("Baikalskaya", 456);
        Person person2 = new Person("Anatolij", 25, address2);

        String fileName = "people.bin";

        // сериализация объектов в файл
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName))) {
            oos.writeObject(person1);
            oos.writeObject(person2);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // десериализация объектов из файла
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName))) {
            Person deserializedPerson1 = (Person) ois.readObject();
            System.out.println(deserializedPerson1);

            Person deserializedPerson2 = (Person) ois.readObject();
            System.out.println(deserializedPerson2);
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
