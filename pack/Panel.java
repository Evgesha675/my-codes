package pack;

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

import javax.swing.Action;
import javax.swing.BoxLayout;
import javax.swing.ComboBoxModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;


public class Panel extends JPanel implements ActionListener {

    private static final String[] ITEMS = new String[] { "4","6","10","20"};
    
    private JPanel upperPanel1 = new JPanel();
    private JPanel upperPanel2 = new JPanel();
    private JPanel middlePanel = new JPanel();
    private JPanel lowerPanel1 = new JPanel();
    private JPanel lowerPanel2 = new JPanel();
    private JPanel lowerPanel3 = new JPanel();
    private JPanel lowerPanel4 = new JPanel();
    ArrayList list = new ArrayList<>();
    ArrayList lst = new ArrayList<>();
    private JButton rollBtn = new JButton("Добавить кубики");
    private JButton rollBtn2 = new JButton("Кинуть их");
    private JLabel displayResult = new JLabel(" ");
    private JLabel displayResult2 = new JLabel(" ");
    private JComboBox nbSide = new JComboBox<>();
    private JTextField ndSide = new JTextField(3);
    private  final  String  adin = "rollBtn"; 
    private  final  String  dvia = "rollBtn2";
    public Panel() {
        rollBtn.setName(adin);
        rollBtn2.setName(dvia);
        upperPanel1.setLayout(new FlowLayout(FlowLayout.LEFT));
        upperPanel2.setLayout(new FlowLayout(FlowLayout.LEFT));
        upperPanel1.add(new JLabel("Cколько кубиков? :"));
        upperPanel2.add(new JLabel("Cколько сторон у кубика? :"));
        // upperPanel2.add(nbSide);
        upperPanel1.add(ndSide);
        nbSide.setModel(new javax.swing.DefaultComboBoxModel<>(ITEMS));
        ndSide.setText("0");
        middlePanel.add(rollBtn);
        middlePanel.add(rollBtn2);
        rollBtn.addActionListener(this);
        rollBtn2.addActionListener(this);
        // rollBtn.addActionListener(new ActionListener() {
        // @Override
        // public void actionPerformed(ActionEvent actionEvent) {
        // int ndSideInt;
        // JButton btn = (JButton) actionEvent.getSource();
        // ndSideInt = Integer.parseInt(ndSide.getText());
        //         for(int i=0; i<ndSideInt;i++){
        //             nbSide = new JComboBox<>(ITEMS);
        //             list.add(nbSide);
        //             upperPanel2.add(nbSide);
      
        //         }

        //     }
        // });
       

       
        lowerPanel1.setLayout(new FlowLayout(FlowLayout.LEFT));
        lowerPanel1.add(new JLabel("Какое число выпало :"));

        lowerPanel2.add(displayResult);
        lowerPanel3.add(new JLabel("Сумма  :"));
        lowerPanel4.add(displayResult2);

        this.setLayout(new BoxLayout(this, BoxLayout.PAGE_AXIS));
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
        displayResult2.setText(" ");
        displayResult.setText(" ");
        int ndSideInt;
        
        ndSideInt = Integer.parseInt(ndSide.getText());
        JButton btn = (JButton) ev.getSource();

        if (btn.getName().equalsIgnoreCase(adin)){
        for(int i=0; i<ndSideInt;i++){
            nbSide = new JComboBox<>(ITEMS);
            upperPanel2.add(nbSide);
            list.add(nbSide);
            this.revalidate();
            }
        }
    
        // else {if (ndSideInt==0){JOptionPane.showMessageDialog(null, "Error\nЯ не буду их кидать!");}
      else {
            Random r = new Random();
            int result2 = 0;
           for(int i = 0; i<list.size();i++){
        
            String text = (String)  ((JComboBox) list.get(i)).getSelectedItem();
            int number = Integer.parseInt(text);
            int rnd_nmb = r.nextInt(number)+1;
             result2 += rnd_nmb;
           displayResult.setText(displayResult.getText() + "  " + String.valueOf(rnd_nmb));
           }
           displayResult2.setText(displayResult2.getText() + "  " + String.valueOf(result2));
       }
    }}
        
        
        //         Random r = new Random();
        //         for(int j=0; j<ndSideInt;j++){
        //         nbSideInt = Integer.parseInt(nbSide.getSelectedItem().toString());
                
        //         int low = 1;
        //         int high = nbSideInt+ 1;
        //         int result2 = 0;
        //         for(int i=0; i<ndSideInt+1;i++) {
        //             int result = r.nextInt(high-low) + low;
        //             result2 += result;
        //             displayResult.setText(displayResult.getText() + "  " + String.valueOf(result));

        //         displayResult2.setText(displayResult2.getText() + "  " + String.valueOf(result2));
        //     }
        // }

    








         //try {
        //     if(nbSideInt !=4 & nbSideInt !=6 & nbSideInt !=10 & nbSideInt !=20){
        //         JOptionPane.showMessageDialog(null, "Error\n Столько сторон не может быть");}
        //     else
        //     {
        //         Random r = new Random();
        //         int low = 1;
        //         int high = nbSideInt + 1;
        //         int result2 = 0;
        //         for(int i=0; i<ndSideInt;i++) {

        //             int result = r.nextInt(high-low) + low;
        //             result2 += result;
        //             displayResult.setText(displayResult.getText() + "  " + String.valueOf(result));
        //         }


        //         displayResult2.setText(displayResult2.getText() + "  " + String.valueOf(result2));
        //     }
        // } catch(NumberFormatException e) {
        //     JOptionPane.showMessageDialog(null, "Error\n Чо ты вввёл?");
        // };

   


