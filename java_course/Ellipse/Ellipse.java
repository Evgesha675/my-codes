package java_course.Ellipse;

public class Ellipse {
    private double a;  // большая полуось
    private double b;  // малая полуось
    // конструктор по умолчанию
    public Ellipse() {
        this.a = 0.0;
        this.b = 0.0;
    }
    // конструктор с параметрами
    public Ellipse(double a, double b) {
        this.a = a;
        this.b = b;
    }
    // метод для получения большой полуоси
    public double getMajorAxis() {
        return this.a;
    }
    // метод для получения малой полуоси
    public double getMinorAxis() {
        return this.b;
    }
    // метод для установки большой полуоси
    public void setMajorAxis(double a) {
        this.a = a;
    }
    // метод для установки малой полуоси
    public void setMinorAxis(double b) {
        this.b = b;
    }   
    // метод для вычисления площади эллипса
    public double getArea() {
        return Math.PI * this.a * this.b;
    }
}

