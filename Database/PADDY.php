<?php
$servername = "localhost";
$username = "root";
$password = "bhanu183";
$conn = new mysqli($servername, $username, $password,"Annadata_Sukhibava");
if ($conn->connect_error)
{
    die("Connection failed: " . $conn->connect_error);
}
$q="create table PADDY_PESTICIDES(DAYS varchar(10) primary key,PESTICIDE varchar(1000),USES varchar(500));";
$conn->query($q);

$data='insert into PADDY_PESTICIDES values
("000-025","Pyrazosulfuron-Ethyl.Dosage:2 g/litre","Controls major broadleaf weeds, Sedges and Grassy Weeds."),
("026-040","Cartap Hydrochloride.Dosage:1 mL/litre.Mortar.Dosage:2 mL /litre.Chlorantraniliprole.Dosage:2 g/litre","Against Stem Borer"),
("041-080","Bifenthrin.Dosage:2 mL /litre.Caldan 50SP.Dosage:3 g/litre.","Against leaf folders"),
("081-110","Buprofezin 25% Sc.Dosage:3 mL/L.Thiamethoxam 25% Wg.Dosage:2mL/litre.Pymetrozine 50% WG.Dosage:3 mL/L","For integrated pest management"),
("111-150","Godiwa Super.Dosage:3 mL/L.Conika.Dosage:3 gm/L.Kasugamycin 3% SL.Dosage:2 gm/L.Spectrum.Dosage:1 mL/litre","For Blast and Sheath Blight diseases");
';
$conn->query($data);

?>
