<?php
include 'db.php'; // Подключаемся к базе данных

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $title = $_POST['title'];
    $type = $_POST['type'];
    $location = $_POST['location'];
    $start_time = $_POST['start_time'];
    $duration = $_POST['duration'];
    $comments = $_POST['comments'];
    $status = 'текущее'; // По умолчанию статус "текущее"

    // Подготовка SQL запроса
    $sql = "INSERT INTO Events (title, type, location, start_time, duration, comments, status) VALUES (?, ?, ?, ?, ?, ?, ?)";
    $stmt = $pdo->prepare($sql);

    // Выполнение запроса
    try {
        $stmt->execute([$title, $type, $location, $start_time, $duration, $comments, $status]);
        header("Location: index.php"); // Перенаправляем обратно на главную страницу
        exit;
    } catch (PDOException $e) {
        echo "Ошибка добавления события: " . $e->getMessage();
    }
}
?>