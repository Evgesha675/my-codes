package java_course.entity;

// Подкласс "Техника", наследующий от суперкласса "Сущность"
public class Machine extends Entity {
    protected String purpose; // назначение техники
    
    // Конструктор с параметрами
    public Machine(String name, String purpose) {
        super(name);
        this.purpose = purpose;
    }
    
    // Перегрузка конструктора с одним параметром
    public Machine(String name) {
        super(name);
        this.purpose = "неизвестно";
    }
    
    // Переопределение метода "описание"
    @Override
    public void describe() {
        System.out.println("Это техника с названием " + name + ", предназначенная для " + purpose);
    }
    
    // Новый метод, специфичный для подкласса "Техника"
    public void work() {
        System.out.println(name + " выполняет работу");
    }
}