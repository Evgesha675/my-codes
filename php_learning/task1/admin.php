<?php
// Получение списка заявок
$files = glob("application_*.txt");

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['delete'])) {
    if (isset($_POST['applications'])) {
        foreach ($_POST['applications'] as $file) {
            unlink($file);
        }
        echo "Выбранные заявки успешно удалены.";
    } else {
        echo "Выберите заявки для удаления.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Администратор</title>
</head>
<body>
    <h2>Список заявок</h2>
    <form action="" method="post">
        <?php foreach ($files as $file): ?>
            <input type="checkbox" name="applications[]" value="<?= $file ?>">
            <?= $file ?><br>
        <?php endforeach; ?>
        <input type="submit" name="delete" value="Удалить">
    </form>
</body>
</html>
