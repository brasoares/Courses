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

// Array
$friends = ['Harry', 'Ron', 'Hermione', 'Hagrid'];
var_dump($friends);
echo '<br>';

// Object
$person = new stdClass();
var_dump($person);
echo '<br>';

// Null
$nonono = null;
var_dump($nonono);
echo '<br>';

// Resource
$file = fopen('quasar.txt', 'r'); // Opens the file and the 'r' is for reading.
var_dump($file);

// Work on the image!
$imgPath = (/quasar.jpg);
$imgSize = getimagesize($imagePath);
echo $imgSize;

/*
*This is a common practice in modern PHP development. 
* If your file contains only PHP code, leaving out the closing tag helps prevent 
* any accidental whitespace or newline characters from being sent to the output, 
* which can avoid issues, especially when working with HTTP headers.
*/
