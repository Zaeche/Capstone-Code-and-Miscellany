<?php
session_start();
$_SESSION["logged"]='';
echo "You are logged out";
header("Location: login.php");

?>
