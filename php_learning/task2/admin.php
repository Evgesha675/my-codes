<?php
session_start();

$admin_username = 'admin';
$admin_password = 'cc15ff7133beb3b9edf8d5aa5bbf8d29'; // md5('sEcREt_PasSwoRD')

if (isset($_SESSION['LAST_ACTIVITY']) && (time() - $_SESSION['LAST_ACTIVITY'] > 300)) {
    session_unset();
    session_destroy();
}
$_SESSION['LAST_ACTIVITY'] = time();

if (isset($_POST['logout'])) {
    session_unset();
    session_destroy();
    header("Location: admin.php");
    exit;
}

if (isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = md5($_POST['password']);

    if ($username == $admin_username && $password == $admin_password) {
        $_SESSION['loggedin'] = true;
    } else {
        echo "Неверное имя пользователя или пароль.";
    }
}

if (!isset($_SESSION['loggedin'])) {
    ?>
    <form action="admin.php" method="post">
        <label for="username">Имя пользователя:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Пароль:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit" name="login">Войти</button>
    </form>
    <?php
    exit;
}

include 'db.php';

if (isset($_POST['delete'])) {
    $id = $_POST['id'];
    $sql = "DELETE FROM participants WHERE id = ?";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$id]);
    echo "Заявка удалена.";
}

$sql = "SELECT * FROM participants";
$stmt = $pdo->query($sql);
$participants = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<h1>Административная панель</h1>
<form action="admin.php" method="post">
    <button type="submit" name="logout">Выйти</button>
</form>
<table>
    <tr>
        <th>ID</th>
        <th>Имя</th>
        <th>Фамилия</th>
        <th>Email</th>
        <th>Телефон</th>
        <th>Тема конференции</th>
        <th>Метод оплаты</th>
        <th>Дата создания</th>
        <th>Действия</th>
    </tr>
    <?php foreach ($participants as $participant): ?>
    <tr>
        <td><?= htmlspecialchars($participant['id']) ?></td>
        <td><?= htmlspecialchars($participant['name']) ?></td>
        <td><?= htmlspecialchars($participant['lastname']) ?></td>
        <td><?= htmlspecialchars($participant['email']) ?></td>
        <td><?= htmlspecialchars($participant['tel']) ?></td>
        <td><?= htmlspecialchars($participant['subject_id']) ?></td>
        <td><?= htmlspecialchars($participant['payment_id']) ?></td>
        <td><?= htmlspecialchars($participant['created_at']) ?></td>
        <td>
            <form action="admin.php" method="post" style="display:inline;">
                <input type="hidden" name="id" value="<?= $participant['id'] ?>">
                <button type="submit" name="delete">Удалить</button>
            </form>
        </td>
    </tr>
    <?php endforeach; ?>
</table>
