<?php
// вывод
echo "hello world \n";
// типы данных (дефолт)
$a = 2;
$b = true;
$c = 'hi';
$d = null;
echo "{$a}\n";
echo 2 . 5;//конктаенация
$new_a = strval($a);//тоже что и (string)$a
// ещё для преобразования можно использовать settype($a , 'type')
echo "\n{$a},{$new_a} ";
// получение типа данных
echo gettype($a);
echo ' ';
echo gettype($new_a);
echo "\n";
echo gettype($b);
// сущ дефолт проверки на тмипы данных (is_'type')
// ещё можно вот так объявлять константы
define ('CONST_NAME', 'hu');
echo "\n";
echo const_name;
// лучше делать проверочку 
echo "\n";
if (!defined('CONST_NAME')){
    define ('CONST_NAME', 'hu');
};
// удобный и простой вид для переноса перемкенных/строк
define("CONSTANT", "значение константы");
echo "Константа: " . CONSTANT . "\n";