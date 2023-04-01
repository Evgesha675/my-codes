package java_course.Ellipse2;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Polygon;
import java.awt.geom.Ellipse2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

interface Scalable {
    double MIN_SCALE_FACTOR = 0.1;
    double MAX_SCALE_FACTOR = 10.0;

    void scale(double scaleFactor);
}

interface Rotatable {
    double MIN_ROTATION_ANGLE = -Math.PI;
    double MAX_ROTATION_ANGLE = Math.PI;

    void rotate(double angle);
}

abstract class Shape {
    int x;
    int y;
    Color color;

    public Shape(int x, int y, Color color) {
        this.x = x;
        this.y = y;
        this.color = color;
    }

    abstract void draw(Graphics2D g);

}

class Triangle extends Shape implements Scalable, Rotatable {
    int base;
    int height;
    double angle;

    public Triangle(int x, int y, int base, int height, Color color) {
        super(x, y, color);
        this.base = base;
        this.height = height;
        this.angle = 0;
    }

    @Override
    void draw(Graphics2D g) {
        g.setColor(color);
        Graphics2D g2 = (Graphics2D) g.create();

        g2.rotate(angle, x + base / 2, y + height / 2);
        g2.draw(new Polygon(new int[]{x, x + base / 2, x + base}, new int[]{y + height, y, y + height}, 3));

        g2.dispose();
    }

    @Override
    public void scale(double scaleFactor) {
        if (scaleFactor < MIN_SCALE_FACTOR) {
            scaleFactor = MIN_SCALE_FACTOR;
        } else if (scaleFactor > MAX_SCALE_FACTOR) {
            scaleFactor = MAX_SCALE_FACTOR;
        }

        this.base *= scaleFactor;
        this.height *= scaleFactor;
    }

    @Override
    public void rotate(double angle) {
        if (angle < MIN_ROTATION_ANGLE) {
            angle = MIN_ROTATION_ANGLE;
        } else if (angle > MAX_ROTATION_ANGLE) {
            angle = MAX_ROTATION_ANGLE;
        }

        this.angle = angle;
    }
}

class Rectangle extends Shape implements Scalable, Rotatable {
    int width;
    int height;
    double angle;

    public Rectangle(int x, int y, int width, int height, Color color) {
        super(x, y, color);
        this.width = width;
        this.height = height;
        this.angle = 0;
    }

    @Override
    void draw(Graphics2D g) {
        g.setColor(color);
        Graphics2D g2 = (Graphics2D) g.create();
        g2.rotate(angle, x + width / 2, y + height / 2);
        g2.drawRect(x, y, width, height);
        g2.dispose();
    }

    @Override
    public void scale(double scaleFactor) {
        if (scaleFactor < MIN_SCALE_FACTOR) {
            scaleFactor = MIN_SCALE_FACTOR;
        } else if (scaleFactor > MAX_SCALE_FACTOR) {
            scaleFactor = MAX_SCALE_FACTOR;
        }

        this.width *= scaleFactor;
        this.height *= scaleFactor;
    }

    @Override
    public void rotate(double angle) {
        if (angle < MIN_ROTATION_ANGLE) {
            angle = MIN_ROTATION_ANGLE;
        } else if (angle > MAX_ROTATION_ANGLE) {
            angle = MAX_ROTATION_ANGLE;
        }

        this.angle = angle;
    }
    
    public static Ellipse2D.Double createInscribedEllipse(int x, int y, int width, int height) {
        double centerX = x + width / 2.0;
        double centerY = y + height / 2.0;
        double semiMajorAxis = width / 2.0;
        double semiMinorAxis = height / 2.0;
        return new Ellipse2D.Double(centerX - semiMajorAxis, centerY - semiMinorAxis, 2.0 * semiMajorAxis, 2.0 * semiMinorAxis);
    }
}

class Ellipse extends Shape implements Scalable, Rotatable {
    int width;
    int height;
    double angle;

    public Ellipse(int x, int y, int width, int height, Color color) {
        super(x, y, color);
        this.width = width;
        this.height = height;
        this.angle = 0;
    }

    @Override
    void draw(Graphics2D g) {
    g.setColor(color);
    Graphics2D g2 = (Graphics2D) g.create(); // Создаем новый графический контекст, чтобы сохранить оригинальный

    g2.rotate(angle, x + width / 2, y + height / 2); // Поворачиваем графический контекст
    g2.draw(new Ellipse2D.Double(x, y, width, height)); // Рисуем эллипс с измененным графическим контекстом

    g2.dispose(); // Освобождаем созданный графический контекст
}

    @Override
    public void scale(double scaleFactor) {
        if (scaleFactor < MIN_SCALE_FACTOR) {
            scaleFactor = MIN_SCALE_FACTOR;
        } else if (scaleFactor > MAX_SCALE_FACTOR) {
            scaleFactor = MAX_SCALE_FACTOR;
        }

        this.width *= scaleFactor;
        this.height *= scaleFactor;
    }

    @Override
    public void rotate(double angle) {
        if (angle < MIN_ROTATION_ANGLE) {
            angle = MIN_ROTATION_ANGLE;
        } else if (angle > MAX_ROTATION_ANGLE) {
            angle = MAX_ROTATION_ANGLE;
        }

        this.angle = angle;
    }
    public static Rectangle getBoundingBox(int x, int y, int width, int height) {
        return new Rectangle(x, y, width, height, Color.BLACK);
    }
}

public class Main {
    public static void main(String[] args) {
        
        BufferedImage image = new BufferedImage(800, 600, BufferedImage.TYPE_INT_RGB);
        Graphics2D g2d = image.createGraphics();
        g2d.setColor(Color.WHITE); // задаем белый цвет для фона
        g2d.fillRect(0, 0, 800, 600); // закрашиваем фон белым цветом
        g2d.setStroke(new BasicStroke(5));

        Rectangle rectangle = new Rectangle(400, 400, 100, 50, Color.BLUE);
        rectangle.scale(0.5);
        rectangle.rotate(Math.PI / 6);
        rectangle.draw(g2d);    

        Triangle triangle = new Triangle(400, 300, 100, 50, Color.BLUE);
        triangle.rotate(Math.PI / 3);
        triangle.scale(2);
        triangle.draw(g2d);
        

        Ellipse ellipse1 = new Ellipse(200, 200, 100, 50, Color.GREEN);
        ellipse1.rotate(Math.PI / 4);
        ellipse1.draw(g2d);

        Ellipse ellipse2 = new Ellipse(100, 100, 100, 50, Color. black);
        ellipse2.scale(0.5);
        ellipse2.rotate(-Math.PI / 4);
        ellipse2.draw(g2d);

        Ellipse ellipse3 = new Ellipse(300, 300, 100, 50, Color. black);
        ellipse3.scale(0.5);
        ellipse3.rotate(Math.PI / 2);
        ellipse3.draw(g2d);

        Ellipse ellipse = new Ellipse(50, 50, 100, 80, Color.RED);
        Ellipse.getBoundingBox(ellipse.x, ellipse.y, ellipse.width, ellipse.height);
        


        try {
            ImageIO.write(image, "png", new File("output.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
