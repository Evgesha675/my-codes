<?php


// print_r(glob('data/*'));
foreach (glob('data/.') as $pathname){

    echo '<b>' . $pathname . '</b><br>';
    echo 'size' . filesize($pathname) . '<br>';
    
}


$dir = 'data/'; 

if (! file_exists($dir)){
    mkdir ($dir,0777,true);
}        
$filename = 'example.txt';
$content = 'Hello world' . date('Y-m-d H:i:s') ."\n";
file_put_contents($filename,$content , FILE_APPEND);


?>