package pack;

import javax.swing.JFrame;

public class Window extends JFrame {
    Panel panel = new Panel();
    
    public Window() {
        this.setLocationRelativeTo(null);
        this.setVisible(true);
        this.setTitle("DiceRoll");
        this.setSize(500,300);
        this.setResizable(true);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setContentPane(panel);
    }

}
