package java_course.lab13;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class TextEditor extends JFrame implements ActionListener, KeyListener {
    private JTextArea textArea;

    public TextEditor() {
        setTitle("Text Editor");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(500, 500);

        textArea = new JTextArea();
        textArea.setFont(new Font("Arial", Font.PLAIN, 12));
        textArea.addKeyListener(this);

        JScrollPane scrollPane = new JScrollPane(textArea);
        scrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);

        JButton formatButton = new JButton("Format");
        formatButton.addActionListener(this);

        JPanel buttonPanel = new JPanel();
        buttonPanel.add(formatButton);

        Container container = getContentPane();
        container.setLayout(new BorderLayout());
        container.add(scrollPane, BorderLayout.CENTER);
        container.add(buttonPanel, BorderLayout.SOUTH);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                TextEditor textEditor = new TextEditor();
                textEditor.setVisible(true);
            }
        });
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getActionCommand().equals("Format")) {
            String text = textArea.getText();
            text = formatText(text);
            textArea.setText(text);
        }
    }

    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_TAB) {
            int position = textArea.getCaretPosition();
            String text = textArea.getText();
            text = text.substring(0, position) + "\t" + text.substring(position);
            textArea.setText(text);
            textArea.setCaretPosition(position + 1);
            e.consume();
        }
    }

    public void keyTyped(KeyEvent e) {
    }

    public void keyReleased(KeyEvent e) {
    }

    private String formatText(String text) {
        // Здесь вы можете реализовать логику форматирования текста по своему усмотрению
        // Ниже приведен простой пример форматирования - добавление отступов в начале каждой строки

        StringBuilder formattedText = new StringBuilder();
        String[] lines = text.split("\n");

        for (String line : lines) {
            formattedText.append("\t").append(line).append("\n");
        }

        return formattedText.toString();
    }
}
