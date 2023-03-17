package java_course.Ellipse_peregruz;
public class Ellipse {
    private double a;  // большая полуось
    private double b;  // малая полуось
    
    // конструктор по умолчанию
    public Ellipse() {
        this.a = 0.0;
        this.b = 0.0;
    }
    
    // конструктор с параметрами (double, double)
    public Ellipse(double a, double b) {
        this.a = a;
        this.b = b;
    }
    
    // конструктор с параметром (double)
    public Ellipse(double r) {
        this.a = r;
        this.b = r;
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
    
    // метод для вычисления периметра эллипса (аппроксимация)
    public double getPerimeter() {
        return Math.PI * (3 * (this.a + this.b) - Math.sqrt((3 * this.a + this.b) * (this.a + 3 * this.b)));
    }
    
    // перегруженный метод setAxes с двумя параметрами
    public void setAxes(double a, double b) {
        this.a = a;
        this.b = b;
    }
    
    // перегруженный метод setAxes с одним параметром
    public void setAxes(double r) {
        this.a = r;
        this.b = r;
    }
}
