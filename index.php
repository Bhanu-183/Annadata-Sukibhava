<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://fonts.google.com/specimen/Alata:wght@300&display=swap" rel="stylesheet"> 
  <link href="https://fonts.googleapis.com/css2?family=Alata&family=Josefin+Sans:wght@300&display=swap" rel="stylesheet"> 
  <link rel="stylesheet" href="style.css">
  <title>Annadata Sukibhava</title>
</head>
<body>
<p>ANNADATA SUKIBHAVA</p>
  <p class="heading">MAY THE PROVIDER BE HAPPY!!</p>
  
</body>
</html>
<?php
  $id=$pno="";
  $msg="";
  if($_SERVER[REQUEST_METHOD]=="POST")
  {
    $id=$_POST['id'];
    $pno=$_POST['num'];
    $id=trim($id);
    $id=htmlspecialchars($id);
    $pno=trim($pno);
    $pno=htmlspecialchars($pno);
    $servername = "localhost";
    $username = "root";
    $password = "bhanu183";
    $conn = new mysqli($servername, $username, $password,"Annadata_Sukhibava");
    if ($conn->connect_error)
    {
      die("Connection failed: " . $conn->connect_error);
    }
    $q="SELECT * FROM Farmer_Details WHERE UID='".$id."' AND PHNO='".$pno."'";
    $result = $conn->query($q);
    if ($result->num_rows > 0)
    {
      while($row=$result->fetch_assoc())
      {
        session_start();
        $_SESSION['id'] = $id;
        header("Location:/ANNADATA_SUKIBHAVA/fourcardfeature/main.php");
      }
    }
    else
    {
      $msg="TryAgain";
    }
    $conn->close();
  }
?>
<img src="./farmer.jpg" alt="" srcset="" class="hero">
<div>
<form action="<?php echo htmlspecialchars($_SERVER[PHP_SELF]);?>" method="post">
    <span>UID</span><input style="margin-left:28px;margin-top:60px" placeholder="Enter UID" type="text" class="in" name=id value=<?php echo $id?>> <br> <br>
    <span>PHNO</span><input type="text" name="num" class="in" placeholder="Enter Phone Number" value=<?php echo $pno?>> <br> <br>
    <input type="submit" value="LOGIN" class="btn">
</form>
</div>
<p class="new">NEW USER?? <a href="http://localhost/ANNADATA_SUKIBHAVA/signup.php" style="color:white; font-size:large;font-family:'Alata';padding:5px;">SIGN UP</a></p>
  <?php
    if($msg=="TryAgain")
      echo '<script>alert("NO ENTRY PRESENT!!TRY AGAIN")</script>';
  ?>
