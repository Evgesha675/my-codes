<?php
 
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $fname = $_POST['fname'];
    $lname = $_POST['lname'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $topic = $_POST['topic'];
    $payment = $_POST['payment'];
    $newsletter = isset($_POST['newsletter']) ? "Да" : "Нет";

    // Генерация уникального имени файла на основе времени
    $filename = "application_" . date("Y-m-d_H-i-s") . ".txt";

    // Сохранение данных в файл
    $data = "Имя: $fname\nФамилия: $lname\nEmail: $email\nТелефон: $phone\nТематика конференции: $topic\nМетод оплаты: $payment\nЖелание получать рассылку: $newsletter\n\n";
    file_put_contents($filename, $data);

    echo "Ваша заявка успешно принята!";
}
