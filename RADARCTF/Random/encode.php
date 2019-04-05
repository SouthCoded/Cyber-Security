<?php
    function encode($input){ 
        $inputlen = strlen($input);
		$randkey = rand(1, 9); 
		$i = 0;
		while ($i < $inputlen) {
			$inputchr[$i] = (ord($input[$i]) - $randkey);
			$i++; 
		}
		$encrypted = implode('.', $inputchr) . '.' . (ord($randkey)+49);
		return $encrypted;
    }
	echo(encode("radar{}"));
	?>

  
	114 97 100 97 114 123 114 97 110 100 95 105 115 95 110 111 116 95 103 111 111 100 95 105 100 101 97 95 108 111 108 125 102

	ord(53) = 5

	$randkey = 5

	$inputlen = 31

	109 = ord(key) - 5;

	114,

