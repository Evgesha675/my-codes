<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Конференция</title>
</head>
<body>
    <h2>Заявка на участие в конференции</h2>
    <form action="submit.php" method="post">
        <label for="fname">Имя:</label><br>
        <input type="text" id="fname" name="fname" required><br>
        <label for="lname">Фамилия:</label><br>
        <input type="text" id="lname" name="lname" required><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br>
        <label for="phone">Телефон:</label><br>
        <input type="tel" id="phone" name="phone" required><br>
        <label for="topic">Тематика конференции:</label><br>
        <select id="topic" name="topic" required>
            <option value="Бизнес">Бизнес</option>
            <option value="Технологии">Технологии</option>
            <option value="Реклама и Маркетинг">Реклама и Маркетинг</option>
        </select><br>
        <label for="payment">Метод оплаты:</label><br>
        <input type="radio" id="webmoney" name="payment" value="WebMoney" required>
        <label for="webmoney">WebMoney</label><br>
        <input type="radio" id="yandex" name="payment" value="Яндекс.Деньги">
        <label for="yandex">Яндекс.Деньги</label><br>
        <input type="radio" id="paypal" name="payment" value="PayPal">
        <label for="paypal">PayPal</label><br>
        <input type="radio" id="creditcard" name="payment" value="Кредитная карта">
        <label for="creditcard">Кредитная карта</label><br>
        <input type="checkbox" id="newsletter" name="newsletter" value="1">
        <label for="newsletter">Получать рассылку о конференции</label><br>
        <input type="submit" value="Отправить заявку">
    </form>
</body>
</html>
