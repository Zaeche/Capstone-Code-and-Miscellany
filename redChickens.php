<?php
$USERS["testUser"] = "theTester";
$USERS["Zigby"] = "zebra";
$USERS["username3"] = "password3";

function check_logged(){
     global $_SESSION, $USERS;
     if (!array_key_exists($_SESSION["logged"],$USERS)) {
          header("Location: login.php");
     };
};
?>
