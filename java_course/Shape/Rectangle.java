package java_course.Shape;

import java.awt.Color;
import java.awt.Graphics;

public class Rectangle extends Shape implements Scalable {
    private int x;
    private int y;
    private int width;
    private int height;

    public Rectangle(int x, int y, int width, int height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    @Override
    public void draw(Graphics graphics) {
        graphics.setColor(Color.YELLOW);
        graphics.drawRect(x, y, width, height);
        graphics.setColor(Color.CYAN);
    }

    @Override
    public void scale(double factor) {
        if (factor < MIN_SCALE || factor > MAX_SCALE) {
            throw new IllegalArgumentException("Invalid scale factor");
        }

        width *= factor;
        height *= factor;
    }
}
