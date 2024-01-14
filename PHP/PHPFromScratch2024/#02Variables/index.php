<?php

// String
$name = "Sigmund Freud";
$name2 = "Nicola Tesla";

var_dump($name);
echo getType($name2);
echo '<br>';

// Integer
$age = 35;
var_dump($age);
echo '<br>';

// Float
$rating = 9.5;
var_dump($rating);
echo '<br>';

// Boolean
$isLoaded = true;
var_dump($isLoaded);
echo '<br>';

/*
*This is a common practice in modern PHP development. 
* If your file contains only PHP code, leaving out the closing tag helps prevent 
* any accidental whitespace or newline characters from being sent to the output, 
* which can avoid issues, especially when working with HTTP headers.
*/
