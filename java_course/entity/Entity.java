package java_course.entity;

// Суперкласс "Сущность"
public class Entity {
    protected String name; // название сущности
    
    // Конструктор с параметром
    public Entity(String name) {
        this.name = name;
    }
    
    // Геттер для поля "name"
    public String getName() {
        return name;
    }
    
    // Метод "описание", который будет переопределен в подклассах
    public void describe() {
        System.out.println("Это некая сущность с названием " + name);
    }
}
