<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="detailstyle.css">
    <link href="https://fonts.google.com/specimen/Alata:wght@300&display=swap" rel="stylesheet"> 
    <link href="https://fonts.googleapis.com/css2?family=Alata&family=Josefin+Sans:wght@300&display=swap" rel="stylesheet">
    <title>Your Details..</title>
</head>

<body>
    <div class="nav">
    <a href="/ANNADATA_SUKIBHAVA/fourcardfeature/main.php">HOME</a>
    <a href="/ANNADATA_SUKIBHAVA/index.php" >LOGOUT</a> 
    
    </div>
    <img src="person.png" height="200px" width="200px" alt="" srcset="" class="hero">
</body>
<?php 
   session_start(); // this NEEDS TO BE AT THE TOP of the page before any output etc
   $id=$_SESSION['id'];
   $servername="localhost";
   $username="root";
   $password="bhanu183";
   $conn=new mysqli($servername,$username,$password,"Annadata_Sukhibava");
   if ($conn->connect_error)
    {
      die("Connection failed: " . $conn->connect_error);
    }
   $q="SELECT * FROM Farmer_Details WHERE UID='".$id."'";
   $result=$conn->query($q);
   if($result->num_rows>0)
   {
       while($row=$result->fetch_assoc())
       {
           echo "<div class='left'><h1 class='side'> Name</h1>
           <h1> Unique ID</h1>
           <h1> Phno</h1>
           <h1> Sex</h1>
           <h1> Location</h1>
           <h1> Soil Type</h1>
           <h1> Crop</h1>
           <h1> Acers</h1>
           <h1> Start Date</h1>
           <h1> Expected Harvest Date</h1></div>";
        
            echo "<div class='right'>";
           echo "<h1>".$row['NAME']."</h1>";
           echo "<h1>".$row['UID']."</h1>";
           echo "<h1>".$row['PHNO']."</h1>";
           echo "<h1>".$row['GENDER']."</h1>";
           echo "<h1>".$row['LOCATION']."</h1>";
           echo "<h1>".$row['SOIL_TYPE']."</h1>";
           echo "<h1>".$row['CROP_NAME']."</h1>";
           echo "<h1>".$row['ACERS']."</h1>";
           echo "<h1>".$row['START_DATE']."</h1>";
           echo "<h1>".$row['EXPECTED_HARVEST_DATE']."</h1>";
           echo "</div>";


       }
   }
?>

</html>