package java_course.entity;

public class Main {
    public static void main(String[] args) {
        Animal dog = new Animal("Dog", "Mammal");
        dog.sound();
        
        Machine car = new Machine("Car", "Transportation");
        car.work();
    }
}
