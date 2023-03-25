package java_course.Ellipse_peregruz;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;

public class Main1 {
    public static void main(String[] args) {
        // создаем объекты с различными параметрами
        Ellipse ellipse1 = new Ellipse();
        Ellipse ellipse2 = new Ellipse(3.0, 2.0);
        ellipse1.setMajorAxis(5.0);
        ellipse1.setMinorAxis(4.0);
        // создаем изображение
        BufferedImage image = new BufferedImage(400, 400, BufferedImage.TYPE_INT_RGB);
        Graphics2D graphics = image.createGraphics();

        // устанавливаем цвет фона
        graphics.setBackground(Color.WHITE);
        graphics.clearRect(0, 0, image.getWidth(), image.getHeight());

        // рисуем эллипсы
        graphics.setColor(Color.RED);
        graphics.drawOval(50, 50, (int) ellipse1.getMajorAxis() * 10, (int) ellipse1.getMinorAxis() * 10);
        graphics.setColor(Color.BLUE);
        graphics.drawOval(150, 150, (int) ellipse2.getMajorAxis() * 10, (int) ellipse2.getMinorAxis() * 10);

        // сохраняем изображение в файл
        try {
            ImageIO.write(image, "PNG", new File("ellipses.png"));
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
