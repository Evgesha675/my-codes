package dbconstruct;

import java.sql.*;
import java.io.*;
import java.util.ArrayList;

public class FirebirdDatabase {
    private static final String DB_URL = "jdbc:firebirdsql://localhost/C:/PIPES.FDB";
    private static final String DB_USER = "sysdba";
    private static final String DB_PASSWORD = "masterkey";

    public static void main(String[] args) {
        ArrayList<String> data = readDataFromFile();
        if (data != null) {
            System.out.println("Data read from file:");
            for (String line : data) {
                System.out.println(line);
            }
            boolean success = writeDataToFile(data);
            if (success) {
                System.out.println("Data written to file PIPES1.FDB successfully.");
            } else {
                System.out.println("Failed to write data to file PIPES1.FDB.");
            }
        } else {
            System.out.println("Failed to read data from file.");
        }
    }

    private static ArrayList<String> readDataFromFile() {
        ArrayList<String> data = new ArrayList<>();
        try (Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD)) {
            String query = "SELECT * FROM YOUR_TABLE_NAME"; // Замените YOUR_TABLE_NAME на имя вашей таблицы

            try (PreparedStatement statement = connection.prepareStatement(query);
                 ResultSet resultSet = statement.executeQuery()) {
                while (resultSet.next()) {
                    String line = resultSet.getString("YOUR_COLUMN_NAME"); // Замените YOUR_COLUMN_NAME на имя столбца, содержащего данные
                    data.add(line);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return data;
    }

    private static boolean writeDataToFile(ArrayList<String> data) {
        try (Connection connection = DriverManager.getConnection(DB_URL.replace("PIPES.FDB", "PIPES1.FDB"), DB_USER, DB_PASSWORD)) {
            String query = "INSERT INTO YOUR_TABLE_NAME (YOUR_COLUMN_NAME) VALUES (?)"; // Замените YOUR_TABLE_NAME и YOUR_COLUMN_NAME на соответствующие значения

            try (PreparedStatement statement = connection.prepareStatement(query)) {
                for (String line : data) {
                    statement.setString(1, line);
                    statement.executeUpdate();
                }
            }
            return true;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }
}
