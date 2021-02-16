<?php
$servername = "localhost";
$username = "root";
$password = "bhanu183";
$conn = new mysqli($servername, $username, $password);
if ($conn->connect_error)
{
    die("Connection failed: " . $conn->connect_error);
}


$q="CREATE DATABASE Annadata_Sukhibava";
$conn->query($q);

?>
