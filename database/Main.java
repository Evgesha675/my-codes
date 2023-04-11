package database;

import java.sql.*;

public class Main {
  public static void main(String[] args) {
    try {
      // Установка соединения с базой данных
      Class.forName("org.firebirdsql.jdbc.FBDriver");
      Connection conn = DriverManager.getConnection("jdbc:firebirdsql://localhost/C:/MYDB.FDB", "ISU", "111");

      // Выполнение SQL-запроса и вывод результатов
      Statement stmt = conn.createStatement();
      ResultSet rs = stmt.executeQuery("SELECT * FROM pipes");
      while (rs.next()) {
        int id = rs.getInt("id");
        int length = rs.getInt("length");
        int width = rs.getInt("width");
        int walls = rs.getInt("walls");
        System.out.println("Pipe " + id + ": Length=" + length + ", Width=" + width + ", Walls=" + walls);
      }

      // Закрытие соединения
      rs.close();
      stmt.close();
      conn.close();
    } catch (Exception e) {
      System.err.println("Error: " + e.getMessage());
    }
  }
}
