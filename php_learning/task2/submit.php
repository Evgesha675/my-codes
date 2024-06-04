<?php
include 'db.php'; // Подключаемся к базе данных

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Добавляем отладочную информацию
    echo "<pre>";
    print_r($_POST);
    echo "</pre>";

    $name = $_POST['name'] ?? null;
    $lastname = $_POST['lastname'] ?? null;
    $email = $_POST['email'] ?? null;
    $tel = $_POST['tel'] ?? null;
    $subject_id = $_POST['subject'] ?? null;
    $payment_id = $_POST['payment'] ?? null;
    $mailing = isset($_POST['mailing']) ? 1 : 0;
    $current_time = date('Y-m-d H:i:s');

    if ($name && $lastname && $email && $tel && $subject_id && $payment_id) {
        $sql = "INSERT INTO participants (name, lastname, email, tel, subject_id, payment_id, mailing, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";
        $stmt = $pdo->prepare($sql);

        try {
            $stmt->execute([$name, $lastname, $email, $tel, $subject_id, $payment_id, $mailing, $current_time, $current_time]);
            echo "Заявка успешно отправлена!";
        } catch (PDOException $e) {
            echo "Ошибка при отправке заявки: " . $e->getMessage();
        }
    } else {
        echo "Пожалуйста, заполните все обязательные поля.";
    }
}
