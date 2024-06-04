<?php
include 'db.php'; // Подключаемся к базе данных

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $id = $_POST['id'];

    // Подготовка SQL запроса
    $sql = "DELETE FROM Events WHERE id = ?";
    $stmt = $pdo->prepare($sql);

    // Выполнение запроса
    try {
        $stmt->execute([$id]);
        header("Location: index.php"); // Перенаправляем обратно на главную страницу
        exit;
    } catch (PDOException $e) {
        echo "Ошибка удаления события: " . $e->getMessage();
    }
} else {
    echo "Неверный метод запроса.";
}
?>