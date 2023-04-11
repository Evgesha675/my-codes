package database;

import java.sql.*;

public class Main {
  public static void main(String[] args) {
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
      
      // Закрытие соединения с базой данных
      conn.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}