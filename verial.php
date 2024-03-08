<?php
$key_name = $_POST['key_name'];

$file = fopen("veri.txt", "a");
fwrite($file, $key_name . "\n"); 
fclose($file);
?>
