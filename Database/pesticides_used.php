<?php
$servername = "localhost";
$username = "root";
$password = "bhanu183";
$conn = new mysqli($servername, $username, $password,"Annadata_Sukhibava");
if ($conn->connect_error)
{
    die("Connection failed: " . $conn->connect_error);
}

$q="create table PESTICIDES_USED(SNO int(5) AUTO_INCREMENT primary key,ID int(5),DATE_OF_QUERY varchar(10),PESTICIDE varchar(1000))";
$conn->query($q);
?>
