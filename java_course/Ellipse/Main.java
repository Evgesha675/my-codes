package java_course.Ellipse;

public class Main {
    public static void main(String[] args) {
        Ellipse ellipse1 = new Ellipse(3.0, 2.0);
        System.out.println("Major axis of ellipse1: " + ellipse1.getMajorAxis());
        System.out.println("Minor axis of ellipse1: " + ellipse1.getMinorAxis());
        System.out.println("Area of ellipse1: " + ellipse1.getArea());

        Ellipse ellipse2 = new Ellipse();
        ellipse2.setMajorAxis(5.0);
        ellipse2.setMinorAxis(4.0);
        System.out.println("Major axis of ellipse2: " + ellipse2.getMajorAxis());
        System.out.println("Minor axis of ellipse2: " + ellipse2.getMinorAxis());
        System.out.println("Area of ellipse2: " + ellipse2.getArea());
    }
}
