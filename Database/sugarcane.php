<?php
$servername = "localhost";
$username = "root";
$password = "bhanu183";
$conn = new mysqli($servername, $username, $password,"Annadata_Sukhibava");
if ($conn->connect_error)
{
    die("Connection failed: " . $conn->connect_error);
}

$q="create table SUGARCANE_PESTICIDES(DAYS varchar(10) primary key,PESTICIDE varchar(1000),USES varchar(500));";
$conn->query($q);

$data='insert into SUGARCANE_PESTICIDES values
("000-030","Use beauvaria bassiana 1% bio pesticides mixed with 61% farm yard manure and water sprinkled on it,kept for 8-0 days in shade.Dosage:3-5 kg per hectare","To save from termite insect"),
("031-070","malathion dissolved in 1250 litre water.Dosage: 1 litre","it saves from white flies"),
("071-110","Fenvalrate.Dosage:25 kg 10% EC","To kill white guidar"),
("111-150","tricograma.Dosage: 10 cards per hectare","to kill early shoot borer"),
("151-180","Burn the dry leaves after harvesting of sugarecane","To kill shalk insect");';
$conn->query($data);

?>