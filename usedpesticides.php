<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pesticides Suggested</title>
    <link rel="stylesheet" href="pesticidestyle.css">
</head>
<body>
<div class="opt-mob">
    <i class="fas fa-bars"  style="font-size:30px;color:white;" id="opt"></i>
    <div id="myModal" class="modal">
        <h1 style="margin-top: 20px; text-align: center;"><u>PESTICIDES SUGGESTED SO FAR</u></h1>
        <a href="/ANNADATA_SUKIBHAVA/fourcardfeature/main.php"><span class="close">&times;</span></a>
        <div class="modal-content">  
            <h1>
                <?php
                    session_start();
                    $id=$_SESSION['id'];
                    $servername="localhost";
                    $username="root";
                    $password="bhanu183";
                    $conn=new mysqli($servername,$username,$password,"Annadata_Sukhibava");
                    if ($conn->connect_error)
                    {
                        die("Connection failed: " . $conn->connect_error);
                    }
                    $query="SELECT * FROM PESTICIDES_USED WHERE ID='".$id."'";
                    $result=$conn->query($query);
                    if($result->num_rows>0)
                    {
                        while($row=$result->fetch_assoc())
                        {
                            echo "<br><br>PESTICIDE SUGGESTED:".$row["PESTICIDE"]."<br>DATE OF SUGGESTION:".$row["DATE_OF_QUERY"];
                        }
                    }
                    else
                    {
                        echo "NO PESTICIDE SUGGESTED SO FAR";
                    }
                ?>
            </h1>    
        </div>
    </div>  
</div>
</body>
</html>