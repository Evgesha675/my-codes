package java_course.Shape;

public interface Scalable {
    double MIN_SCALE = 0.1;
    double MAX_SCALE = 10.0;

    void scale(double factor);
}
