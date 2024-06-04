<?php
$host = '127.0.0.1'; // Адрес сервера
$port = 3306; // Порт
$dbname = 'evgeshatest28'; // Имя базы данных
$username = 'evgeshatest28'; // Имя пользователя
$password = '3wrmcpUJ'; // Пароль

try {
    $dsn = "mysql:host=$host;port=$port;dbname=$dbname";
    $pdo = new PDO($dsn, $username, $password);
    // Установка режима ошибок PDO на исключение
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Подключение к базе данных успешно!";
} catch (PDOException $e) {
    die("Не удалось подключиться к базе данных: " . $e->getMessage());
}
?>