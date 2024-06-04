<?php
$host = '127.0.0.1'; // Адрес сервера
$port = 3306; // Порт
$dbname = 'task187'; // Имя базы данных
$username = 'task187'; // Имя пользователя
$password = 'kZ4ubDYd'; // Пароль

try {
    $dsn = "mysql:host=$host;port=$port;dbname=$dbname";
    $pdo = new PDO($dsn, $username, $password);
    // Установка режима ошибок PDO на исключение
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Не удалось подключиться к базе данных: " . $e->getMessage());
}
?>
