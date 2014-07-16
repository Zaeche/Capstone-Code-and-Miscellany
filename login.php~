<?php
session_start();
include("redChickens.php");
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<link rel = "stylesheet" type ="text/css" href = "login.css" />
	<title> userAuth </title>
</head>
<div id = "content">
<div id = "main-top"><!-- Leave this empty --></div>
<div id = "main-center">
<body>

<div id="formSec">
<?php
if ($_POST["ac"]=="log") {
     if ($USERS[$_POST["username"]]==$_POST["password"]) {
          $_SESSION["logged"]=$_POST["username"];
     } else {
          echo 'Incorrect username/password. Please, try again.';
     };
};
if (array_key_exists($_SESSION["logged"],$USERS)) {
     echo "You are logged in.";
     header("Location: homepage.php");
} 

else {
    echo '<form action="login.php" method="post"><input type="hidden" name="ac" value="log"> ';
    echo 'Username: <input type="text" name="username" />';
    echo 'Password: <input type="password" name="password" />';
    echo '<input type="submit" value="Login" />';
    echo '</form>';	
};
?>
 
</div>

</div>
</div>
</div>
</body>
</html>

