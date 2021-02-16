
<?php
$servername = "localhost";
$username = "root";
$password = "bhanu183";
$conn = new mysqli($servername, $username, $password,"Annadata_Sukhibava");
if ($conn->connect_error)
{
    die("Connection failed: " . $conn->connect_error);
}
$query="create table COTTON_PESTICIDES(DAYS varchar(10) primary key,PESTICIDE varchar(1000),USES varchar(500));";
$conn->query($query);

$data="insert into COTTON_PESTICIDES values
('000-020','Mint and camphor.Dosage:10 g/liter','To save the seed from ants'),
('021-060','BotaniGardES.Dosage:5ml/liter.Spinosad.Dosage:5ml/liter.Neem Oil.Dosage:10ml/liter','Aganist the stink bugs and Thrips'),
('061-090','Pyrethrum formulation:Prepared from powdered flower heads or liquid extracts of chrysanthemum.Dosage:3ml/liter.Custard apple leaf extract.Dosage:20g/liter','Aganist the cotton stainers and spider mites'),
('091-120','Neem spray:prepared from neem kernels.Dosage:20ml/liter','Aganist the pink boll worms'),
('121-150','Alfalfa hay.Dosage:20gm/liter.Gibrax phytozyme.Dosage:2mL/litre','Aganist the Lygus Bugs'),
('151-180','Pyrethrum:prepared from powdered flower heads or liquid extracts of chrysanthemum.Dosage:2ml/liter.Econeem plus.Dosage:10ml/liter','Aganist theAPHIDS and whitefly');";

$conn->query($data);

?>