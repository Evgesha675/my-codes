package java_course.Ellipse_peregruz;
public class Main{
public static void main(String[] args) {
    // создаем объекты с различными параметрами
    Ellipse ellipse1 = new Ellipse();
    Ellipse ellipse2 = new Ellipse(3.0, 2.0);
    
    // выводим значения полуосей и площади для каждого объекта
    System.out.println("Ellipse 1 - Major Axis: " + ellipse1.getMajorAxis() + ", Minor Axis: " + ellipse1.getMinorAxis() + ", Area: " + ellipse1.getArea());
    System.out.println("Ellipse 2 - Major Axis: " + ellipse2.getMajorAxis() + ", Minor Axis: " + ellipse2.getMinorAxis() + ", Area: " + ellipse2.getArea());
    
    // изменяем значения полуосей для каждого объекта
    ellipse1.setMajorAxis(5.0);
    ellipse1.setMinorAxis(4.0);
    ellipse2.setMajorAxis(8.0);
    ellipse2.setMinorAxis(6.0);
    
    // выводим значения полуосей и площади для каждого объекта после изменения
    System.out.println("Ellipse 1 - Major Axis: " + ellipse1.getMajorAxis() + ", Minor Axis: " + ellipse1.getMinorAxis() + ", Area: " + ellipse1.getArea());
    System.out.println("Ellipse 2 - Major Axis: " + ellipse2.getMajorAxis() + ", Minor Axis: " + ellipse2.getMinorAxis() + ", Area: " + ellipse2.getArea());
    
    // создаем новый объект с помощью копирующего конструктора
    Ellipse ellipse3 = new Ellipse();
    
    // выводим значения полуосей и площади для нового объекта
    System.out.println("Ellipse 3 - Major Axis: " + ellipse3.getMajorAxis() + ", Minor Axis: " + ellipse3.getMinorAxis() + ", Area: " + ellipse3.getArea());
    
    // выводим периметр для каждого объекта
    System.out.println("Ellipse 1 - Perimeter: " + ellipse1.getPerimeter());
    System.out.println("Ellipse 2 - Perimeter: " + ellipse2.getPerimeter());
    System.out.println("Ellipse 3 - Perimeter: " + ellipse3.getPerimeter());
}
}