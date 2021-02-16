<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <link rel="stylesheet" href="signupstyle.css">
    <link href="https://fonts.google.com/specimen/Alata:wght@300&display=swap" rel="stylesheet"> 
    <link href="https://fonts.googleapis.com/css2?family=Alata&family=Josefin+Sans:wght@300&display=swap" rel="stylesheet">
    <script>
        $(document).ready(function () 
        {
              $("#type").change(function ()
              {
                  var val = $(this).val();
                  if (val == "Clay Loam" || val=="Red Clayey Soils" || val=="Red Loam" || val=="Alluvial Loam")
                  {
                      $("#size").html("<option value='Rice'>Rice</option>");
                  }
                  else if (val=="Peaty soil" || val=="Sandy soil" || val=="Clayey soil" || val=="chalky Soil")
                  {
                      $("#size").html("<option value='Groundnut'>Groundnut</option>");
                  }
                  else if (val == "Slit Loam")
                  {
                      $("#size").html("<option value='Cotton'>Cotton</option><option value='Groundnut'>Groundnut</option>");
                  }
                  else if (val=="Sandy Loam" || val=="Red clay loam")
                  {
                      $("#size").html("<option value='Pigeon Pea'>Pigeon Pea</option>");
                  }
                  else if (val=="Red Sandy Loam")
                  {
                      $("#size").html("<option value='Cotton'>Cotton</option>");
                  }
                  else if (val == "Black Soil")
                  {
                      $("#size").html("<option value='Cotton'>Cotton</option><option value='Mirchi'>Mirchi</option><option value='Sugarcane'>Sugarcane</option>");
                  }
                  else if (val=="Red Sandy Soil")
                  {
                      $("#size").html("<option value='Sugarcane'>Sugarcane</option>");
                  }
                  else if (val=="Red Soil")
                  {
                      $("#size").html("<option value='Mirch'>Mirchi</option>");
                  }
                  else if (val=="item0")
                  {
                      $("#size").html("<option value=''>--select Soil--</option>");
                  }
              });
          });
    </script>


    <title>SignUp-Annadata Sukibhava</title>
</head>
<body>

<?php
    $name=$phno=$gender=$location=$soil=$crop=$acers=$sd="";
    
    function uid()
    {
        $unid=rand(1,10000);
        $servername="localhost";
        $username="root";
        $password="bhanu183";
        $conn=new mysqli($servername,$username,$password,"Annadata_Sukhibava");
        if ($conn->connect_error)
        {
            die("Connection failed: " . $conn->connect_error);
        }
        $q="select * from Farmer_Details where UID='".$unid."'";
        $result=$conn->query($q);
        if($result->num_rows==0)
        {
            return $unid;
        }
        else
        {
            uid();
        }
    }
    function expected_date($crop,$sd)
    {   
        $d1=substr($sd,0,2);
        $m1=substr($sd,3,2);
        $y1=substr($sd,6,9);
        $crop=strtolower($crop);
        if($crop=="cotton" or $crop=="mirchi" or $crop=="sugarcane")
        {
            
            $nd=180;
            $d1+=$nd%30;
            $m1=$m1+$nd/30;
            if($m1>12 or ($m1==12 and $d1>31))
            {
                if($m1>12)
                    $m1=$m1-12;
                $y1+=1;
            }
            strval($d1);
            strval($m1);
            strval($y1);
            
            if(strlen($d1)==1)
                $d1="0".$d1;
            
            if(strlen($m1)==1)
                $m1="0".$m1;
            $date2 =$d1."/".$m1."/".$y1;
            
            return $date2;
        }

        elseif($crop =="rice" or $crop=="groundnut")
        {
            $nd = 150;
            $d1+=$nd%30;
            $m1=$m1+$nd/30;
            if($m1>12 or ($m1==12 and $d1>31))
            {
                if($m1>12)
                    $m1=$m1-12;
                $y1+=1;
            }
            strval($d1);
            strval($m1);
            strval($y1);
            if(strlen($d1)==1)
            {
            	$d1="0".$d1;
            }
            if(strlen($m1)==1)
            {
            	$m1="0".$m1;
            }
            $date2 =$d1.'/'.$m1.'/'.$y1;
            return $date2;

        }
        elseif($crop=="pigeon pea")
        {
            $nd = 210;
            $d1+=$nd%30;
            $m1=$m1+$nd/30;
            if($m1>12 or ($m1==12 and $d1>31))
            {
                if($m1>12)
                    $m1=$m1-12;
                $y1+=1;
            }
            strval($d1);
            strval($m1);
            strval($y1);
            if(strlen($d1)==1)
            {
            	$d1="0".$d1;
            }
            if(strlen($m1)==1)
            {
            	$m1="0".$m1;
            }
            $date2 =$d1.'/'.$m1.'/'.$y1;
            return $date2;
        }
    }
    if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        $servername="localhost";
        $username="root";
        $password="bhanu183";
        $conn=new mysqli($servername,$username,$password,"Annadata_Sukhibava");
        if ($conn->connect_error)
        {
            die("Connection failed: " . $conn->connect_error);
        }
        $id=uid();
        $name = test_input($_POST["name"]);
        $phno = test_input($_POST["phno"]);
        $quer1="SELECT * FROM Farmer_Details WHERE PHNO='".$phno."'";
        $res=$conn->query($quer1);
        if($res->num_rows!=0)
        {
            echo '<script>alert("THE ENTERED PHONE NUMBER IS ALREADY PRESENT")</script>';
        }
        $gender = test_input($_POST["gender"]);
        $location=test_input($_POST["location"]);
        $soil=test_input($_POST["soil"]);
        $crop=test_input($_POST["crop"]);
        
        $acers=test_input($_POST["acers"]);
        $sd=test_input($_POST["sd"]);
        $yr=substr($sd,0,4);
        $month=substr($sd,5,2);
        
        $date=substr($sd,8,9);
        
        $sd=$date."/".$month."/".$yr;
        $ed=expected_date($crop,$sd);
        
        $query="INSERT INTO Farmer_Details (NAME,UID,PHNO,GENDER,LOCATION,SOIL_TYPE,CROP_NAME,ACERS,START_DATE,EXPECTED_HARVEST_DATE) VALUES('".$name."','".$id."','".$phno."','".$gender."','".$location."','".$soil."','".$crop."','".$acers."','".$sd."','".$ed."')";
        if ($conn->query($query)===TRUE) 
        {
            session_start();
            $_SESSION['id'] = $id;
            header("Location:/ANNADATA_SUKIBHAVA/details.php");
        }
        else
        {
            echo $conn->error;
        }
    }
    
    function test_input($data)
    {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
?>


    <div class="container">
    <div class="caption">
          <p style="margin-left:180px">WELCOME</p> <br><br><br><br> <p style="margin-left:280px">TO</p> <br><br><br><br><p style="margin-left:30px">ANNADATA SUKIBHAVA</p> <br>
          <p class="main">MAY <br> THE <br> PROVIDER <br> BE <br> HAPPY</p>
    </div>
    <div class="mob-caption">
        <p style="margin-left:50px">WELCOME ANNADATA SUKIBHAVA</p> <br>
        <p style="margin-left:65px">MAY THE PROVIDER BE HAPPY</p>
    </div>
    <div class="vl"></div>
    <h1 class="heading"> <u> Fill in the Details</u></h1>
        <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>" method="post">
          <div class='left'>
            <span>Name</span><input type="text" name="name" class="name" placeholder="Name" value="<?php echo $name;?>" required> <br> <br>
            <span>Phone Number</span><input type="text" name="phno" class="phno" placeholder="Phone Number" value="<?php echo $phno;?>" required> <br> <br>
            <span>Gender:
            <input type="radio" name="gender" <?php if (isset($gender) && $gender=="male") echo "checked";?> value="M" class="gen" required>Male
            <input type="radio" name="gender" <?php if (isset($gender) && $gender=="female") echo "checked";?> value="F" required class="gen fem">Female
            <br><br>
            <span>Location</span><input type="text" name="location" class='location' required value="<?php echo $location;?>" placeholder="Location"> <br> <br>

            
          </div>
          <button type="submit" class="submit">SUBMIT</button>
          <button type="reset" class="reset">RESET</button>
          <div class="right">
          
                
            <br><br>
        
              <span>Soil</span>

            <select id="type" class="soil" name="soil" id="soil" required>
                  <option value="">--Select Soil--</option>
                  <option value="Clay Loam">Clay Loam</option>
                  <option value="Peaty soil">Peaty soil</option>
                  <option value="Slit Loam">Slit Loam</option>
                  <option value="Sandy soil">Sandy soil</option>
                  <option value="Sandy Loam">Sandy Loam</option>
                  <option value="Clayey soil">Clayey soil</option>
                  <option value="Red Clayey Soils">Red Clayey Soils</option>
                  <option value="Red Sandy Loam">Red Sandy Loam</option>
                  <option value="Black Soil">Black Soil</option>
                  <option value="Red Loam">Red Loam</option>
                  <option value="Alluvial Loam">Alluvial Loam</option>
                  <option value="chalky Soil">chalky Soil</option>
                  <option value="Red Sandy Soil">Red Sandy Soil</option>
                  <option value="Red Soil">Red Soil</option>
                  <option value="Red clay loam">Red clay loam</option>
            </select> <br>
            <span>Crop</span>
            <select id="size" name="crop" class="crop" value="<?php echo $crop;?>" required>
                  <option value="">--Select Crop--</option>
              </select><br>
            <span>Number of Acers</span><input type="number" name="acers" class="acers" value="<?php echo $acers;?>" required placeholder="Number of Acers"> <br>
            <span>Start Date</span><input type="date" date_format='dd-mm-yyyy' name="sd" class="sd" required> <br> <br>
        </div>
        
      </form>
    </div>
</body>
</html>


