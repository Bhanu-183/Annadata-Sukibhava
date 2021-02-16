<?php 
   session_start(); // this NEEDS TO BE AT THE TOP of the page before any output etc
   $id=$_SESSION['id'];
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- displays site properly based on user's device -->
 
  <link rel="stylesheet" href="styles.css">
  <title>Welcome!!Annadata Sukibhava</title>

  <!-- Feel free to remove these styles or customise in your own stylesheet 👍 -->
  <style>
    .attribution { font-size: 11px; text-align: center; }
    .attribution a { color: hsl(228, 45%, 44%); }
  </style>
</head>
<body>
<script src="./script.js"></script>
  <div class="header">
  <p>DEVELOPED BY:Bhanu Krishna Prasad.V</p> 
    <h1><span class="unbold">Reliable and Efficient</span><br>
        Powered by Technology</h1>
        <a href="/ANNADATA_SUKIBHAVA/index.php" class="log">LOG OUT</a> 
  </div>
 
  <div class="cards">
    <div class="left">
      <a href="http://localhost/ANNADATA_SUKIBHAVA/details.php">
      <div class="first card">
        <h2>Details</h2>
        <p>Get all your details like UID,start date,crop,Acers etc.</p>
        <img src="./images/icon-team-builder.svg" alt="">
      </div>
      </a>
    </div>

    <a href="http://localhost/ANNADATA_SUKIBHAVA/pesticides.php">
    <div class="second card">
      <h2>Pesticide Suggestions</h2>
      <p>We will suggest you the best pesticide based on your crop and the time of start</p>
      <img src="./images/icon-karma.svg" alt="nothng">
    </div>
    </a>
    
    <div class="right">
      <a href="http://localhost/ANNADATA_SUKIBHAVA/usedpesticides.php">
      <div class="fourth card">
        <h2>Pesticides used so far..</h2>
        <p>Details of all the pesticides suggested so far...Along with the date of suggestion</p>
        <img src="./images/icon-supervisor.svg" alt="">
      </div>
    </a>
    </div>
  </div>


  
</body>
</html>
