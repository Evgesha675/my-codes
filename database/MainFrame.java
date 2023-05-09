package database;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.table.DefaultTableModel;

public class MainFrame {
  private Connection conn;
  private Statement stmt;
  private JTable table;
  private DefaultTableModel tableModel;

  public static void main(String[] args) {
    MainFrame mainFrame = new MainFrame();
    mainFrame.run();
  }

  public void run() {
    try {
      // Установка параметров подключения к базе данных
      Class.forName("org.firebirdsql.jdbc.FBDriver");
      String url = "jdbc:firebirdsql:localhost/3050:C:/PIPES.FDB";
      String user = "sysdba";
      String password = "masterkey";

      // Подключение к базе данных
      conn = DriverManager.getConnection(url, user, password);
      stmt = conn.createStatement();

      // Создание графического интерфейса
      JFrame frame = new JFrame("Pipes");
      JPanel panel = new JPanel(new BorderLayout());
      JLabel label = new JLabel("Pipes");
      panel.add(label, BorderLayout.NORTH);

      // Создание таблицы и ее модели
      tableModel = new DefaultTableModel();
      table = new JTable(tableModel);
      tableModel.addColumn("ID");
      tableModel.addColumn("Length");
      tableModel.addColumn("Width");
      tableModel.addColumn("Walls");
      JScrollPane scrollPane = new JScrollPane(table);
      panel.add(scrollPane, BorderLayout.CENTER);

      // Создание кнопок для добавления и удаления записей
      JButton addButton = new JButton("Add");
      addButton.addActionListener(new ActionListener() {
        public void actionPerformed(ActionEvent e) {
          addRecord();
        }
      });
      JButton deleteButton = new JButton("Delete");
      deleteButton.addActionListener(new ActionListener() {
        public void actionPerformed(ActionEvent e) {
          deleteRecord();
        }
      });
      JPanel buttonPanel = new JPanel();
      buttonPanel.add(addButton);
      buttonPanel.add(deleteButton);
      panel.add(buttonPanel, BorderLayout.SOUTH);

      // Заполнение таблицы данными из базы данных
      updateTable();

      // Отображение графического интерфейса
      frame.getContentPane().add(panel);
      frame.pack();
      frame.setLocationRelativeTo(null);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setVisible(true);
    } catch (ClassNotFoundException | SQLException e) {
      e.printStackTrace();
    }
  }

  private void updateTable() throws SQLException {
    tableModel.setRowCount(0);
    ResultSet rs = stmt.executeQuery("SELECT * FROM PIPES");
    while (rs.next()) {
      int id = rs.getInt("ID");
      int length = rs.getInt("LENGTH");
      int width = rs.getInt("WIDTH");
      int walls = rs.getInt("WALLS");
      tableModel.addRow(new Object[] {id, length, width, walls});
    }
  }

  private void addRecord() {
    JTextField lengthField = new JTextField();
    JTextField widthField = new JTextField();
    JTextField wallsField = new JTextField();
    Object[] message = {"Length:", lengthField, "Width:", widthField, "Walls:", wallsField};
    int option = JOptionPane.showConfirmDialog(null, message, "Add Record", JOptionPane.OK_CANCEL_OPTION);
    if (option == JOptionPane.OK_OPTION) {
      try {
        int length = Integer.parseInt(lengthField.getText());
        int width = Integer.parseInt(widthField.getText());
        int walls = Integer.parseInt(wallsField.getText());
        stmt.executeUpdate("INSERT INTO PIPES (LENGTH, WIDTH, WALLS) VALUES (" + length + ", " + width + ", " + walls + ")");
        updateTable();
      } catch (NumberFormatException | SQLException ex) {
        ex.printStackTrace();
      }
    }
  }

  private void deleteRecord() {
    int row = table.getSelectedRow();
    if (row != -1) {
      int id = (int) tableModel.getValueAt(row, 0);
      try {
        stmt.executeUpdate("DELETE FROM PIPES WHERE ID = " + id);
        updateTable();
      } catch (SQLException e) {
        e.printStackTrace();
      }
    }
  }
}
    
