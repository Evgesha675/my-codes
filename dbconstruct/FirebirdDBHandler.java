package dbconstruct;

import java.sql.*;
import java.util.ArrayList;

public class FirebirdDBHandler {

    private static final String DB_URL = "jdbc:firebirdsql:localhost/3050:C:/PIPES.FDB";
    private static final String DB_USER = "sysdba";
    private static final String DB_PASSWORD = "masterkey";
    
    public static void main(String[] args) {
        ArrayList<String> lines = readDatabase();
        writeDatabase(lines);
    }

    private static ArrayList<String> readDatabase() {
        ArrayList<String> lines = new ArrayList<>();
        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT * FROM table_name")) {
            while (rs.next()) {
                String line = rs.getString("column_name");
                lines.add(line);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return lines;
    }

    private static void writeDatabase(ArrayList<String> lines) {
        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
             PreparedStatement pstmt = conn.prepareStatement("UPDATE table_name SET column_name = ? WHERE id = ?")) {
            for (int i = 0; i < lines.size(); i++) {
                String line = lines.get(i);
                pstmt.setString(1, line);
                pstmt.setInt(2, i+1);
                pstmt.executeUpdate();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
