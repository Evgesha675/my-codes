<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Регистрация на конференцию</title>
</head>
<body>
    <h1>Регистрация на конференцию</h1>
    <form action="submit.php" method="post">
        <div>
            <label for="name">Имя:</label>
            <input type="text" id="name" name="name" required>
        </div>
        <div>
            <label for="lastname">Фамилия:</label>
            <input type="text" id="lastname" name="lastname" required>
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div>
            <label for="tel">Телефон:</label>
            <input type="tel" id="tel" name="tel" required>
        </div>
        <div>
            <label for="subject">Тема конференции:</label>
            <select id="subject" name="subject" required>
                <option value="1">Бизнес и коммуникации</option>
                <option value="2">Технологии</option>
                <option value="3">Реклама</option>
                <option value="4">Маркетинг</option>
                <option value="5">Проектирование</option>
            </select>
        </div>
        <div>
            <label for="payment">Метод оплаты:</label>
            <select id="payment" name="payment" required>
                <option value="1">WebMoney</option>
                <option value="2">Яндекс.Деньги</option>
                <option value="3">PayPal</option>
                <option value="4">Кредитная карта</option>
                <option value="5">Робокасса</option>
            </select>
        </div>
        <div>
            <label for="mailing">Подписаться на рассылку:</label>
            <input type="checkbox" id="mailing" name="mailing" checked>
        </div>
        <button type="submit">Отправить заявку</button>
    </form>
</body>
</html>
