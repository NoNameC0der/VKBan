<?php
$VKBan = file_get_contents("git clone https://github.com/NoNameC0der/VKBan");
$file = fopen("fastban.py", "w");
fwrite($file, $VKBan);
fclose($file);
?>
