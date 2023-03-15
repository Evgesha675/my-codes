package database;

import java.sql.*;

public class FirebirdExample {
    public static void main(String[] args) {
        try {
            // Load the driver
            Class.forName("org.firebirdsql.jdbc.FBDriver");

            // Connect to the database
            String url = "jdbc:firebirdsql://localhost/3050:/path/to/your/database.fdb";
            String user = "yourUser";
            String password = "yourPassword";
            Connection conn = DriverManager.getConnection(url, user, password);

            // Execute some SQL statements
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM myTable");
            while (rs.next()) {
                System.out.println(rs.getInt("id") + " " + rs.getString("name"));
            }

            // Close the connection
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
/*В этом примере мы сначала загружаем драйвер Firebird, 
используя Class.forName(). Затем мы создаем соединение
 с базой данных с помощью DriverManager.getConnection(), 
 передавая URL-адрес, имя пользователя и пароль.
  Затем мы выполняем некоторые операторы SQL, используя
   Statement.executeQuery(), и обрабатываем результаты с помощью
    ResultSet. Наконец, мы закрываем соединение, используя
     Connection.close(). Обратите внимание, что в строке
      URL замените /path/to/your/database.fdb фактическим
       путем к файлу базы данных Firebird. */