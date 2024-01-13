	<?php
		echo 'Hello from PHP';
		echo '<br>';
		print 'Hello from print';
	?>

	<!DOCTYPE html>
	<html lang="en">

	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
		<title><?php echo 'Learn PHP From Scratch'; ?></title>
	</head>

	<body class="bg-gray-100">
		<header class="bg-blue-500 text-white p-4">
			<div class="container mx-auto">
				<h1 class="text-3x1 font-semibold"><?php echo 'Learn PHP From Scratch'; ?></h1>
			</div>
		</header>
		<div class="container mx-auto p-4 mt-4">
			<div class="bg-white rounded-lg shadow-md p-6">
				<h2 class="text-2x1 font-semibold mb-4"><?php echo "Welcome To The Course" ?></h2>
				<?php echo '<p>In this course, I am learning the fundamentals of PHP!</p>' ?>
			</div>
		</div>
	</body>

	</html>
