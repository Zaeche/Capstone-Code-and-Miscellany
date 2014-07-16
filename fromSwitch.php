<?php
session_start(); /// initialize session
include("redChickens.php");
check_logged();
?>

<?php
	 header( "refresh:2; url=fromSwitch.php" );
?>


<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="site.css">
</head>
<body>

<div id="main">
	<h1>Results/Feedback</h1>

<?php
// Connect to the database
$conn = mysql_connect("localhost", "testUser", "tester");

//execute an SQL statement and return a recordset
mysql_select_db("testDatabase");

$rs = mysql_query("SELECT Switch, Instruction, Data FROM fromSwitch");

echo "<table border='1'>";
echo"<tr><th>Switch</th><th>Instruction</th><th>Data</th></tr>";

while ($row = mysql_fetch_array($rs)) //looping through the recordset (until End Of File)
{
	echo "<tr><td>" .$row['Switch']. "</td><td>" .$row['Instruction']. "</td><td>" .$row['Data']. "</td></tr>";
}

echo "</table>";

//close the recordset and the database connection
mysql_close($conn);
?>


</div>
</body>
</html>

<footer> <?php include("Footer.php"); ?> </footer>
