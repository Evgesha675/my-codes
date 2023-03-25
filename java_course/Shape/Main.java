package java_course.Shape;

import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("My Drawing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // создаем прямоугольник
        Rectangle rectangle = new Rectangle(10, 10, 100, 50);

        // создаем панель, на которой будем рисовать
        JPanel panel = new JPanel() {
            @Override
            public void paintComponent(Graphics g) {
                super.paintComponent(g);

                // рисуем прямоугольник
                rectangle.draw((Graphics2D) g);

                // масштабируем прямоугольник
                rectangle.scale(2.0);

                // рисуем масштабированный прямоугольник
                rectangle.draw((Graphics2D) g);
            }
        };

        frame.add(panel);
        frame.setSize(500, 500);
        frame.setVisible(true);
    }
}
