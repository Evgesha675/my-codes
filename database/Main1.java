package database;

import java.sql.*;
import java.util.Scanner;

public class Main1 {
  /**
   * @param args
   * @throws ClassNotFoundException
   */
  public static void main(String[] args) throws ClassNotFoundException {
    try {
      // Загрузка JDBC-драйвера
      Class.forName("org.firebirdsql.jdbc.FBDriver");

      // Установка параметров подключения к базе данных
      //ISU - админ 
      // файлик закину отдельно!
      String url = "jdbc:firebirdsql:localhost/3050:C:/PIPES.FDB";
      String user = "sysdba";
      String password = "masterkey";

      // Подключение к базе данных
      Connection conn = DriverManager.getConnection(url, user, password);

      // Выполнение запросов
      Statement stmt = conn.createStatement();
      ResultSet rs = stmt.executeQuery("SELECT * FROM PIPES");
      while (rs.next()) {
        int id = rs.getInt("ID");
        int length = rs.getInt("LENGTH");
        int width = rs.getInt("WIDTH");
        int walls = rs.getInt("WALLS");
        System.out.println("Pipe " + id + ": Length=" + length + ", Width=" + width + ", Walls=" + walls);
      }

      Scanner scanner = new Scanner(System.in);
      String input;
      while (true) {
        // Предлагаем пользователю заполнить или удалить запись
        System.out.println("Do you want to add or delete a record? (Y/N)");
        input = scanner.nextLine();
        if (input.equalsIgnoreCase("Y")) {
          System.out.println("Enter 'A' to add a record or 'D' to delete a record: ");
          String action = scanner.nextLine();
          if (action.equalsIgnoreCase("A")) {
            System.out.println("Enter length: ");
            int length = scanner.nextInt();
            System.out.println("Enter width: ");
            int width = scanner.nextInt();
            System.out.println("Enter walls: ");
            int walls = scanner.nextInt();
            String insertQuery = String.format("INSERT INTO PIPES (ID, LENGTH, WIDTH, WALLS) VALUES ((SELECT MAX(ID) FROM PIPES) + 1, %d, %d, %d)", length, width, walls);
            int rowCount = stmt.executeUpdate(insertQuery);
            if (rowCount > 0) {
              System.out.println("Record added successfully!");
            } else {
              System.out.println("Record not added!");
            }
          } else if (action.equalsIgnoreCase("D")) {
            System.out.println("Enter ID of record to delete: ");
            int id = scanner.nextInt();
            String deleteQuery = String.format("DELETE FROM PIPES WHERE ID = %d", id);
            int rowCount = stmt.executeUpdate(deleteQuery);
            if (rowCount > 0) {
              System.out.println("Record deleted successfully!");
            } else {
              System.out.println("Record not deleted!");
            }
          }
          scanner.nextLine(); // Очистка буфера сканера
        } else {
          break;
        }
      }
    
      while (true) {
        System.out.println("Do you want to close the connection? (Y/N)");
        input = scanner.nextLine();
        if (input.equalsIgnoreCase("Y")) {
            conn.close();
            System.out.println("Connection closed successfully!");
            break;
        } else if (input.equalsIgnoreCase("N")) {
            break;
        } else {
            System.out.println("Invalid input. Please enter Y or N.");
        }
    }
} catch (SQLException e) {
    System.out.println("Error connecting to database: " + e.getMessage());
}}}