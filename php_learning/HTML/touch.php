<?php

echo 0777;
exitl; 
$dir = 'data/'; //несуществующая директория

if (! file_exists($dir)){
    mkdir ($dir,0777,true);
}
$filename = $dir .'example.txt';
$content = 'Hello world' . date('Y-m-d H:i:s') ."\n";
file_put_contents($filename,$content , FILE_APPEND);


