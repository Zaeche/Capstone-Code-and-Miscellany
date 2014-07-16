<?php
session_start(); /// initialize session
include("redChickens.php");
check_logged();
?>

<?php header( "refresh:2; url=statusSwitch.php" ); ?>


<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="status.css">
</head>
<body>
<div id = "header">
<a href = "homepage.php"><img src = "Home_Button.png" /></a>
<a href = "feedback.php"><img src = "Results.png" /></a>
<a href = "about.php"><img src = "about-us.png" /></a>
<a href = "logout.php"><img src = "Logout.png" /></a>

</div>

<div id = "content">
<div id = "main-top"><!-- Leave this empty --></div>
<div id = "main-center">

<h1> Current System Status </h1>

<?php
// Connect to the database
$conn = mysql_connect("localhost", "testUser", "tester");

//execute an SQL statement and return a recordset
mysql_select_db("testDatabase");

$rs = mysql_query("SELECT Switch, State, Description, Temperature FROM statusTable");

echo "<table border='1'>";
echo "<tr><th>Switch</th><th>State</th><th>Description</th><th>Temperature</th></tr>";

while ($row = mysql_fetch_array($rs)) //looping through the recordset (until End Of File)
{
	echo "<tr><td>" .$row['Switch']. "</td><td>" .$row['State']. "</td><td>" .$row['Description']. "</td><td>" .$row['Temperature']. "</td></tr>";
}

echo "</table>";


//close the recordset and the database connection
mysql_close($conn);
?>

<?php
if (isset($_POST['ON']))
{
        $output = exec("python /var/www/sendMessage.py ON");
        echo $output;
}
?>

<?php
if (isset($_POST['OFF']))
{
        $output = exec("python /var/www/sendMessage.py OFF");
        echo $output;
}
?>

<link rel="stylesheet" href="status.css">
	<form id="form_1" method="post">
                <button name="ON"> Switch ON </button><br>
                <button name="OFF"> Switch OFF </button><br>
        </form>

	<div id = "footer">
	<div class="copyright">
	</div>
	</div>

</div>
</body>
</html>
