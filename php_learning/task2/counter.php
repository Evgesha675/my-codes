<?php
session_start();

$hits_file = 'hits.txt';
$sessions_file = 'sessions.txt';
$unique_visitors_file = 'unique_visitors.txt';
$visitors_log = 'visitors.log';

// Функция для увеличения счетчика
function increment_counter($file) {
    if (!file_exists($file)) {
        file_put_contents($file, '0');
    }
    $count = file_get_contents($file);
    $count++;
    file_put_contents($file, $count);
    return $count;
}

// Обновляем счетчик загрузок страницы (хитов)
$hits = increment_counter($hits_file);

// Обновляем счетчик пользователей по сессиям
if (!isset($_SESSION['session_start'])) {
    $_SESSION['session_start'] = time();
    $sessions = increment_counter($sessions_file);
}

// Получаем IP-адрес пользователя
$user_ip = $_SERVER['REMOTE_ADDR'];
$current_time = time();
$current_date = date('Y-m-d H:i:s', $current_time);

// Проверяем, был ли пользователь уже зарегистрирован
$visitor_log_content = file_exists($visitors_log) ? file_get_contents($visitors_log) : '';
$is_unique = strpos($visitor_log_content, $user_ip) === false;

if ($is_unique) {
    file_put_contents($visitors_log, "$user_ip $current_date\n", FILE_APPEND);
    increment_counter($unique_visitors_file);
}
?>