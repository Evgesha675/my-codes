<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Мой календарь</title>
    <link rel="stylesheet" href="style.css"> <!-- Подключаем CSS для стилизации -->
</head>
<body>
    <div class="container">
        <h1>Мой календарь</h1>
        <div class="new-task">
            <h2>Новая задача</h2>
            <form action="submit.php" method="post">
                <label for="title">Тема:</label>
                <input type="text" id="title" name="title" required>

                <label for="type">Тип:</label>
                <select id="type" name="type">
                    <option value="встреча">Встреча</option>
                    <option value="осведомитель">Осведомитель</option>
                    <option value="совещание">Совещание</option>
                    <option value="дело">Дело</option>
                </select>

                <label for="location">Место:</label>
                <input type="text" id="location" name="location">

                <label for="start_time">Дата и время:</label>
                <input type="datetime-local" id="start_time" name="start_time" required>

                <label for="duration">Длительность:</label>
                <input type="time" id="duration" name="duration">

                <label for="comments">Комментарии:</label>
                <textarea id="comments" name="comments"></textarea>

                <button type="submit" class="submit-button">Добавить</button>

            </form>
        </div>
        
        <div class="task-list">
            <h2>Список задач</h2>
            <div class="filter">
                <form action="index.php" method="get">
                    <button type="submit" name="filter" value="current">Текущие задачи</button>
                    <input type="date" id="filter-date" name="filter-date">
                    <button type="submit" name="filter" value="today">сегодня</button>
                    <button type="submit" name="filter" value="tomorrow">завтра</button>
                    <button type="submit" name="filter" value="this_week">на эту неделю</button>
                    <button type="submit" name="filter" value="next_week">на след. неделю</button>
                </form>
                <form action="" method="get">
                    <label for="task_date">Выберите дату:</label>
                    <input type="date" id="task_date" name="task_date">
                    <button type="submit">Текущие задачи</button>
                </form>

            </div>
            <table>
                <thead>
                    <tr>
                        <th>Тип</th>
                        <th>Задача</th>
                        <th>Место</th>
                        <th>Дата и время</th>
                    </tr>
                </thead>
                <tbody>
                    <?php
                    include 'db.php'; // Подключаемся к базе данных

                    // Получаем текущие задачи
                    $filter = isset($_GET['filter']) ? $_GET['filter'] : 'current';

                    switch ($filter) {
                        case 'today':
                            $sql = "SELECT * FROM Events WHERE DATE(start_time) = CURDATE()";
                            break;
                        case 'tomorrow':
                            $sql = "SELECT * FROM Events WHERE DATE(start_time) = CURDATE() + INTERVAL 1 DAY";
                            break;
                        case 'this_week':
                            $sql = "SELECT * FROM Events WHERE WEEK(start_time) = WEEK(CURDATE())";
                            break;
                        case 'next_week':
                            $sql = "SELECT * FROM Events WHERE WEEK(start_time) = WEEK(CURDATE()) + INTERVAL 1 WEEK";
                            break;
                        case 'current':
                        default:
                            $sql = "SELECT * FROM Events WHERE status = 'текущее'";
                            break;
                    }

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
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
