package java_course.entity;

// Подкласс "Животное", наследующий от суперкласса "Сущность"
public class Animal extends Entity {
    protected String habitat; // место обитания животного
    
    // Конструктор с параметрами
    public Animal(String name, String habitat) {
        super(name);
        this.habitat = habitat;
    }
    
    // Перегрузка конструктора с одним параметром
    public Animal(String name) {
        super(name);
        this.habitat = "неизвестно";
    }
    
    // Переопределение метода "описание"
    @Override
    public void describe() {
        System.out.println("Это животное с названием " + name + ", обитающее в " + habitat);
    }
    
    // Новый метод, специфичный для подкласса "Животное"
    public void sound() {
        System.out.println(name + " издает звуки");
    }
}