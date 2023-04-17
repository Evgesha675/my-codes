package databasenew;

import java.sql.*;
import java.util.ArrayList;
import java.util.Scanner;

public class PipeManager implements AutoCloseable {
    private Connection connection;
    private PreparedStatement addPipeStatement;
    private PreparedStatement deletePipeStatement;
    private PreparedStatement selectAllPipesStatement;
    private PreparedStatement updatePipeStatement;

    public PipeManager(Connection connection) throws SQLException {
        this.connection = connection;
        addPipeStatement = connection.prepareStatement("INSERT INTO PIPES (ID, LENGTH, WIDTH, WALLS) VALUES (?, ?, ?, ?)", Statement.RETURN_GENERATED_KEYS);
        addPipeStatement.setNull(1, java.sql.Types.INTEGER); // Это чтобы указать, что ID должен быть автоматически сгенерирован.

        deletePipeStatement = connection.prepareStatement("DELETE FROM PIPES WHERE ID = ?");
        selectAllPipesStatement = connection.prepareStatement("SELECT * FROM PIPES");
        updatePipeStatement = connection.prepareStatement("UPDATE PIPES SET LENGTH = ?, WIDTH = ?, WALLS = ? WHERE ID = ?");
    }
    
    public void addPipe(double length, double width, int walls) {
        try {
            int id = getNextId();
            PreparedStatement statement = addPipeStatement;
            statement.setInt(1, id);
            statement.setDouble(2, length);
            statement.setDouble(3, width);
            statement.setInt(4, walls);
            statement.executeUpdate();
            statement.close();
        } catch (SQLException e) {
            System.out.println("Error while adding pipe: " + e.getMessage());
        }
    }
    
    private int getNextId() throws SQLException {
        int nextId = 1;
        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery("SELECT MAX(ID) FROM PIPES");
        if (resultSet.next()) {
            nextId = resultSet.getInt(1) + 1;
        }
        statement.close();
        return nextId;
    }
    

    public void deletePipe(int id) throws SQLException {
        deletePipeStatement.setInt(1, id);
        deletePipeStatement.executeUpdate();
    }

    public ArrayList<Pipe> selectAllPipes() throws SQLException {
        ResultSet resultSet = selectAllPipesStatement.executeQuery();
        ArrayList<Pipe> pipes = new ArrayList<>();
        while (resultSet.next()) {
            int id = resultSet.getInt("ID");
            double length = resultSet.getDouble("LENGTH");
            double width = resultSet.getDouble("WIDTH");
            int walls = resultSet.getInt("WALLS");
            pipes.add(new Pipe(id, length, width, walls));
        }
        resultSet.close();
        return pipes;
    }

    public void updatePipe(int id, double length, double width, int walls) throws SQLException {
        updatePipeStatement.setDouble(1, length);
        updatePipeStatement.setDouble(2, width);
        updatePipeStatement.setInt(3, walls);
        updatePipeStatement.setInt(4, id);
        updatePipeStatement.executeUpdate();
    }

    public void close() throws SQLException {
        addPipeStatement.close();
        deletePipeStatement.close();
        selectAllPipesStatement.close();
        updatePipeStatement.close();
        connection.close();
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in);
             Connection connection = DriverManager.getConnection("jdbc:firebirdsql://localhost/C:/PIPES.fdb", "sysdba", "masterkey");
             PipeManager pipeManager = new PipeManager(connection)) {

            boolean exit = false;

            while (!exit) {
                System.out.println("Выберите действие:");
                System.out.println("1. Посмотреть таблицу");
                System.out.println("2. Удалить строку");
                System.out.println("3. Добавить строку");
                System.out.println("4. Выйти");

                String input = scanner.nextLine();

                switch (input) {
                    case "1":
                        ArrayList<Pipe> pipes = pipeManager.selectAllPipes();
                        System.out.println("Таблица:");
                        for (Pipe pipe : pipes) {
                            System.out.println(pipe);
                        }
                        break;
                    case "2":
                        System.out.println("Введите ID строки, которую нужно удалить:");
                        int idToDelete = Integer.parseInt(scanner.nextLine());
                        pipeManager.deletePipe(idToDelete);
                        System.out.println("Строка успешно удалена");
                        break;
                    case "3":
                    System.out.println("Введите параметры новой трубы:");
                    System.out.print("Length: ");
                    double length = scanner.nextDouble();
                    scanner.nextLine(); // consume the newline character
                    System.out.print("with: ");
                    double width = scanner.nextDouble();
                    scanner.nextLine(); // consume the newline character
                    System.out.print("Walls: ");
                    int walls = scanner.nextInt();
                    scanner.nextLine(); // consume the newline character
                    pipeManager.addPipe(length, width, walls);
                    System.out.println("Труба успешно добавлена");
                    break;
                    case "4":
                        exit = true;
                        break;
                    default:
                        System.out.println("Неверный ввод. Пожалуйста, попробуйте еще раз.");
                }
            }

        } catch (SQLException e) {
            System.out.println("Ошибка работы с базой данных: " + e.getMessage());
        }
    }
}

