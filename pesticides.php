<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PESTICIDE SUGGESTIONS</title>
    <link href="https://fonts.google.com/specimen/Alata:wght@300&display=swap" rel="stylesheet"> 
    <link href="https://fonts.googleapis.com/css2?family=Alata&family=Josefin+Sans:wght@300&display=swap" rel="stylesheet"> 
    <link rel="stylesheet" href="pesticidestyle.css">
</head>
<body>

<div class="opt-mob">
    <i class="fas fa-bars"  style="font-size:30px;color:white;" id="opt"></i>
    <div id="myModal" class="modal">
        <h1 style="margin-top: 20px; text-align: center;"><u>PESTICIDE SUGGESTIONS</u></h1>
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
            $crop='';
            $sd;
            $q="SELECT * FROM Farmer_Details WHERE UID='".$id."'";
            $result=$conn->query($q);
            if($result->num_rows>0)
            {
                while($row=$result->fetch_assoc())
                {
                    $crop=$row['CROP_NAME'];
                    $sd=$row['START_DATE'];
                }
            }
            $crop=strtolower($crop);
            $day1=substr($sd,0,2);
            $month1=substr($sd,3,2);
            $year1=substr($sd,6,9);

            $date2=date("Y-m-d");
            $day2=substr($date2,0,2);
            $month2=substr($date2,3,2);
            $year2=substr($date2,6,9);

            $date1=$year1."-".$month1."-".$day1;
            $dd1=date_create($date1);
            $dd2=date_create($date2);
            $diff=date_diff($dd1,$dd2);
            $nd=$diff->format("%a");
            echo "<br><br>Number days from the start date to today=".$nd."<br><br><br><br>";

            if($crop=="cotton")
            {
                if($nd<=20)
                { 
                $query1="select * from COTTON_PESTICIDES where DAYS='000-020'";
                }
                elseif($nd>20 and $nd<=60)
                {
                $query1="select * from COTTON_PESTICIDES where DAYS='021-060'";
                }
                elseif($nd>60 and $nd<=90)
                {
                $query1="select * from COTTON_PESTICIDES where DAYS='061-090'";
                }
                elseif($nd>90 and $nd<=120)
                {
                $query1="select * from COTTON_PESTICIDES where DAYS='091-120'";
                }
                elseif($nd>120 and $nd<=150)
                {
                $query1="select * from COTTON_PESTICIDES where DAYS='121-150'";
                }
                elseif($nd>150 and $nd<=180)
                {
                $query1="select * from COTTON_PESTICIDES where DAYS='151-180'";
                }
            }
            elseif($crop=="pigeon pea")
            {
                if($nd<=20)
                {
                $query1="select * from PIGEON_PEA_PESTICIDE where DAYS='000-020'";
                }
                elseif($nd>20 and $nd<=50)
                {
                $query1="select * from PIGEON_PEA_PESTICIDE where DAYS='021-050'"; 
                }
                elseif($nd>50 and $nd<=90)
                {
                $query1="select * from PIGEON_PEA_PESTICIDE where DAYS='051-090'";
                }
                elseif($nd>90 and $nd<=125)
                {
                $query1="select * from PIGEON_PEA_PESTICIDE where DAYS='091-125'";
                }
                elseif($nd>125 and $nd<=160)
                {
                $query1="select * from PIGEON_PEA_PESTICIDE where DAYS='126-160'";
                }
                elseif($nd>160 and $nd<=210)
                {
                $query1="select * from PIGEON_PEA_PESTICIDE where DAYS='161-210'";
                }
            }
            elseif($crop=="rice")
            {
                if($nd<=25)
                {
                $query1="select * from PADDY_PESTICIDES where DAYS='000-025'";
                }
                elseif($nd>25 and $nd<=40)
                {
                $query1="select * from PADDY_PESTICIDES where DAYS='026-040;'";
                }
                elseif($nd>40 and $nd<=80)
                {
                $query1="select * from PADDY_PESTICIDES where DAYS='041-080'";
                }
                elseif($nd>80 and $nd<=110)
                {
                $query1="select * from PADDY_PESTICIDES where DAYS='081-110'";
                }
                elseif($nd>110 and $nd<=150)
                {
                $query1="select * from PADDY_PESTICIDES where DAYS='111-150'";
                }
            }

            elseif($crop=="mirchi")
            {
                if($nd <=30)
                {
                $query1="select * from MIRCHI_PESTICIDES where DAYS='000-030'"; 
                }
                elseif($nd>30 and $nd<=50)
                {
                $query1="select * from MIRCHI_PESTICIDES where DAYS='031-050'";
                }
                elseif($nd>50 and $nd<=70)
                {
                $query1="select * from MIRCHI_PESTICIDES where DAYS='051-070'";
                }
               elseif($nd>70 and $nd<=95)
                {
                $query1="select * from MIRCHI_PESTICIDES where DAYS='071-095'";
                }
                elseif($nd>95 and $nd<=135)
                {
                $query1="select * from MIRCHI_PESTICIDES where DAYS='096-135'";
                }
                elseif($nd>135 and $nd<=180)
                {
                $query1="select * from MIRCHI_PESTICIDES where DAYS='136-180'";
                }
            }
            elseif($crop=="sugarcane")
            {
                if($nd<=30)
                {
                $query1="select * from SUGARCANE_PESTICIDES where DAYS='000-030'";
                }
                elseif($nd>30 and $nd<=70)
                {
                $query1="select * from SUGARCANE_PESTICIDES where DAYS='030-070'";   
                }
                elseif($nd>70 and $nd<=110)
                {
                $query1="select * from SUGARCANE_PESTICIDES where DAYS='070-110'";
                }
                elseif($nd>110 and $nd<=150)
                {
                $query1="select * from SUGARCANE_PESTICIDES where DAYS='110-150'"; 
                }
                elseif ($nd>150 and $nd<=180)
                {
                $query1="select * from SUGARCANE_PESTICIDES where DAYS='151-180'";
                }
            }
            elseif($crop=="groundnut")
            {
                if($nd<=25)
                {
                $query1="select * from GROUNDNUT_PESTICIDES where DAYS='000-025'";
                }
                elseif($nd>25 and $nd<=40)
                {
                $query1="select * from GROUNDNUT_PESTICIDES where DAYS='026-040'";
                }
                elseif($nd>40 and $nd<=70)
                {
                $query1="select * from GROUNDNUT_PESTICIDES where DAYS='041-070'";
                }
                elseif($nd>70 and $nd<=100)
                {
                $query1="select * from GROUNDNUT_PESTICIDES where DAYS='071-100'"; 
                }
                elseif($nd>100 and $nd<=150)
                {
                $query1="select * from GROUNDNUT_PESTICIDES where DAYS='101-150'";
                }
            }
            $result=$conn->query($query1);
            $pesticide;
            if($result->num_rows>0)
            {
                while($row=$result->fetch_assoc())
                {
                    $str=$row['PESTICIDE'];
                    $pesticide=$str;
                    $pieces=explode('.',$str);
                    for($i=0;$i<count($pieces);$i+=1)
                    {
                        if($i+1%2==1)
                            echo "<u>PESTICIDE:</u>".$pieces[$i];
                        else
                            echo "<br><br><u>DOSAGE:</u>".$pieces[$i];
                    }
                    echo "<br><br><br><u>USES OF THE PESTICIDE:</u>".$row['USES'];
                }
                $pesticide=explode('.',$pesticide);
                $query="INSERT INTO PESTICIDES_USED (ID,DATE_OF_QUERY,PESTICIDE) VALUES ({$id},'".$date2."','".$pesticide[0]."')";
                $conn->query($query);
            }
            else 
            {
                echo "SORRYY!!THERE IS NO PESTICIDE TO SUGGEST";
            }

    
?>
</h1>    
        </div>
    </div>
</div>
</body>
</html>