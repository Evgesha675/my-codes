<!-- <form method = " GET | POST" action = "URL"> -->
    
<!-- Обращаться к массивам можно с помощью $_GET $_POST $_REQUEST (неважно как получать)
Всегда стоит проверять наличие ключа и ошибки для таких обращений

Метод GET встречался нам в HTTP запросах 
GET - получить (всё происходит в URL) POST - запостить xD
Этот метод оправдан в случаях поиска, пагинации(поиск по страницам) и параметрам фильтрации
Для остального лучше использовать метод POST (+ можно отправить любой объем данных(обычно ограничивают со стороны сервера))

Обработка Файла на сервере
( в презентации (имяЮ тип данныз, размер в байтах, путь к временному файлу, код ошибки)) всё это можно получить
нужна проверка на файл, т.к. в .jpeg можно записать php скрипт, который проникнет к нам на сервер спокойно 
* Защита от атаки. Директория где хранятся файлы должна быть обособленной (не исполнять PHP файлы, 
    пусть это будут просто неисполняемые файлики) Если файл нужно запускать, то нужно его запускать на отдельном сервере в docker'е
    

 -->
