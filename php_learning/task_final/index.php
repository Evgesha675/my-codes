<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Мой календарь</title>
    <link rel="stylesheet" href="style.css"> <!-- Подключаем CSS для стилизации -->
</head>
<body>
    <h1>Мой календарь</h1>
    <form action="submit.php" method="post">
        <fieldset>
            <legend>Новая задача</legend>
            <div>
                <label for="title">Тема:</label>
                <input type="text" id="title" name="title" required>
            </div>
            <div>
                <label for="type">Тип:</label>
                <select id="type" name="type">
                    <option value="встреча">Встреча</option>
                    <option value="осведомитель">Осведомитель</option>
                    <option value="совещание">Совещание</option>
                    <option value="дело">Дело</option>
                </select>
            </div>
            <div>
                <label for="location">Место:</label>
                <input type="text" id="location" name="location">
            </div>
            <div>
                <label for="start_time">Дата и время:</label>
                <input type="datetime-local" id="start_time" name="start_time" required>
            </div>
            <div>
                <label for="duration">Длительность:</label>
                <input type="time" id="duration" name="duration">
            </div>
            <div>
                <label for="comments">Комментарии:</label>
                <textarea id="comments" name="comments"></textarea>
            </div>
            <button type="submit">Добавить</button>
        </fieldset>
    </form>
    
    <h2>Список задач</h2>
    <table>
        <tr>
            <th>Тип</th>
            <th>Задача</th>
            <th>Место</th>
            <th>Дата и время</th>
            <th>Длительность</th>
            <th>Комментарии</th>
            <th>Действие</th>
        </tr>
        <?php
        include 'db.php'; // Подключаемся к базе данных

        // Получаем текущие задачи
        $sql = "SELECT * FROM Events WHERE status = 'текущее'";
        $stmt = $pdo->query($sql);
        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            echo "<tr>";
            echo "<td>" . htmlspecialchars($row['type']) . "</td>";
            echo "<td>" . htmlspecialchars($row['title']) . "</td>";
            echo "<td>" . htmlspecialchars($row['location']) . "</td>";
            echo "<td>" . htmlspecialchars($row['start_time']) . "</td>";
            echo "<td>" . htmlspecialchars($row['duration']) . "</td>";
            echo "<td>" . htmlspecialchars($row['comments']) . "</td>";
            echo "<td>
                  <form action='delete.php' method='post' style='display:inline;'>
                      <input type='hidden' name='id' value='" . $row['id'] . "'>
                      <button type='submit'>Удалить</button>
                  </form>
                  </td>";
            echo "</tr>";
        }
        ?>
    </table>
</body>
</html>