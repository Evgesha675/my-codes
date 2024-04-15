<?php
//explode implode str_replace str_ireplace 
//trim rtrim ltrim удаление пробелов
$str = " fdf ff  ";
print_r(trim($str));
print_r("\n");
//strlen($str) длина строки в байтах mb_strlen($str) длина в символах
print_r(strlen("drxtcfvgbhjsd\n"));
//strtolwer($str) strtoupper($str) верхний нижний регистр, есть так же с mb 
// mb для ютф символов

print_r(strtoupper("jkn\n"));
// Хеширование /*md5($str) sha1($str) */ (не рекомендуется) crc32($str)
//лучше добавлять к паролям *соль* для безопасности (строка добавляющаяся к пароль пользователю)
// Хеширование паролей password_hash($password), password_verify($password, $hash) (проверка правильности хэша для пароля)

//регулярки
//POSIX-совместимые базовые(BRE) расширенные(ERE) устаревшие регулярки (да и нет их в PHP)
//Perl-совместимые (PCRE)
//спецсимволы [] \/ ^ $ . | & * + () {} (экранируются символом \)
$reg = '213 abc def';
$pattern = '/ ... /'; // Регулярное выражение должно быть заключено в косые черты
preg_match($pattern, $reg, $matches);
print_r($matches); // Выведет найденное совпадение
