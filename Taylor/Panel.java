package Taylor;

import java.awt.FlowLayout;
import java.awt.LayoutManager;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;


public class Panel extends JPanel implements ActionListener {
    
    private JPanel upperPanel1 = new JPanel();
    private JPanel upperPanel2 = new JPanel();
    private JPanel middlePanel = new JPanel();
    private JPanel lowerPanel1 = new JPanel();
    private JPanel lowerPanel2 = new JPanel();
    private JPanel lowerPanel3 = new JPanel();
    private JPanel lowerPanel4 = new JPanel();
    private JButton rollBtn = new JButton("sinx");
    private JButton rollBtn2 = new JButton("cosx");
    private JLabel displayResult = new JLabel(" ");
    private JTextField ndSide = new JTextField(15);
    private  final  String  adin = "rollBtn"; 
    private  final  String  dvia = "rollBtn2";
    public static long factorial(int number) {
        long result = 1;

        for (int factor = 2; factor <= number; factor++) {
            result *= factor;
        }

        return result;
    }
    public Panel() {
        rollBtn.setName(adin);
        rollBtn2.setName(dvia);
        upperPanel1.setLayout(new FlowLayout(FlowLayout.LEFT));
        upperPanel2.setLayout(new FlowLayout(FlowLayout.LEFT));
        upperPanel1.add(new JLabel("Введите число(в радианах):"));
        upperPanel1.add(ndSide);
        ndSide.setText("0");
        middlePanel.add(rollBtn);
        middlePanel.add(rollBtn2);
        rollBtn.addActionListener(this);
        rollBtn2.addActionListener(this);
        lowerPanel1.setLayout(new FlowLayout(FlowLayout.LEFT));
        lowerPanel1.add(new JLabel("ответ: "));

        lowerPanel2.add(displayResult);
      

        this.setLayout((LayoutManager) new BoxLayout(this, BoxLayout.PAGE_AXIS));
        this.add(upperPanel1);
        this.add(upperPanel2);
        
        
        this.add(middlePanel);
        this.add(lowerPanel1);
        this.add(lowerPanel2);
        this.add(lowerPanel3);
        this.add(lowerPanel4);
    }

    @Override
    public void actionPerformed(ActionEvent ev) {
        displayResult.setText(" ");
        double but = Double.parseDouble(ndSide.getText());
        JButton btn = (JButton) ev.getSource();
        if (btn.getName().equalsIgnoreCase(adin)){
           double sinuxa = 0;
            for( int i = 0; i<20;i++){
                sinuxa += (Math.pow(-1,i)*Math.pow(but,2*i+1))/factorial(2*i+1);
            }
            displayResult.setText(String.valueOf (sinuxa));
        }
        else{
            double cosinuxa = 0;
            for( int i = 0; i<20;i++){
                cosinuxa += (Math.pow(-1,i)*Math.pow(but,2*i+1))/factorial(2*i+1);
                displayResult.setText(String.valueOf (Math.sqrt(1-Math.pow(cosinuxa,2))));
            }
        }
        
   
    }

}


   


