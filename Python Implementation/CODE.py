import mysql.connector
import random
from datetime import date 
import datetime



'''ESTABLISHING THE CONNECTION WITH THE MySQL SERVER'''
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="pa$$word",
    database="Annadata_Sukhibava"
    )
mycursor = mydb.cursor()



'''ENTERING THE DETAILS OF THE NEW USER INTO THE DATABASE'''
def new_entry():
    print("PLEASE ENTER THE REQUIRED DETAILS\n")
    mycursor.execute("select * from Farmer_Details")
    res=mycursor.fetchall()
    sn=len(res)+1
    name=input("\nENTER YOUR NAME:")
    unid=uid()
    pno=input("ENTER YOUR PHONE NO:")
    gen=input("ENTER YOUR SEX:")
    loc=input("ENTER YOUR VILLAGE NAME:")
    print('''DIFFERENT SOILS AVAILABLE IN YOUR LOCATION ARE:
+------------------+
| Clay Loam        |
| peaty soil       |
| Slit Loam        |
| Sandy soil       |
| Sandy Loam       |
| clayey soil      |
| Red Clayey Soils |
| Red Sandy Loam   |
| Black Soil       |
| Red Loam         |
| Alluvial Loam    |
| chalky Soil      |
| Red Sandy Soil   |
| Red Soil         |
| Red clay loam    |
+------------------+
''')
          
    soil=input("ENTER YOUR SOIL TYPE FROM THE ABOVE SOILS:")
    crop=crop_suggestion(soil)
    acers=input("ENTER NO.OF ACERS:")
    sd=input("ENTER THE START DATE IN DD/MM/YYYY FORMAT:")
    ed=expected_date(crop,sd)
    q="""INSERT INTO Farmer_Details(SNO,NAME,UID,PHNO,GENDER,LOCATION,SOIL_TYPE,CROP_NAME,ACERS,START_DATE,EXPECTED_HARVEST_DATE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    ar=(sn,name,unid,pno,gen,loc,soil,crop,acers,sd,ed)
    mycursor.execute(q,ar)
    mydb.commit()
    print("\nENTER '1' to check your details\nEnter '0' to exit")
    ch=int(input('Enter your choice:'))
    if ch==1:
        mycursor.execute(f"select * from Farmer_Details where UID={unid}")
        myresult = mycursor.fetchall()
        details(myresult)
    else:
        exit()


'''ASSIGNING AN UNIQUE UID TO THE NEW USER'''
def uid():
    unid=random.randrange(1,10000)
    mycursor.execute(f"select * from Farmer_Details where UID={unid}")
    res=mycursor.fetchall()
    if len(res)==0:
        return unid
    else:
        unid()



'''SUGGESTING THE CROP TO THE NEW USER ACCORDING TO THE NATURE OF THE SOIL'''
def crop_suggestion(soil):
    soil=soil.lower()
    if soil=="black soil":
        print("THE CROPS SUITABLE IN BLACK SOIL ARE")
        print("1.COTTON\n2.MIRCHI\n3.SUGARCANE")
        select=int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if select==1:
            return "Cotton"
        elif select==2:
            return "Mirchi"
        elif select==3:
            return "Sugarcane"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTIONS!!!PLEASE TRY AGAIN:)")
            crop_suggestion(soil)
    elif soil=="slit loam":
        print("THE CROPS SUITABLE IN SLIT SOIL ARE")
        print("1.COTTON\n2.GROUNDNUT")
        select=int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if select==1:
            return "Cotton"
        elif select==2:
            return "Groundnut"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTIONS!!!PLEASE TRY AGAIN:)")
            crop_suggestion(soil)
    elif soil=="red soil":
        print("THE CROPS SUITABLE IN RED SOIL ARE")
        print("1.MIRCHI")
        select=int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if select==1:
            return "Mirchi"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTIONS!!!PLEASE TRY AGAIN:)")
            crop_suggestion(soil)

    elif soil == "clay loam":
        print("THE CROPS SUITABLE IN CLAY SOILS IS")
        print("1.RICE")
        select = int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if(select == 1):
            return "Rice"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTION!!!PLEASE TRY AGAIN:)")
            crop_suggestion(soil)
    elif soil == "chalky soil":
        print("THE CROPS SUITABLE IN CHALKY SOILS IS")
        print("1.GROUNDNUT")
        select = int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if(select == 1):
            return "Groundnut"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTION!!!PLEASE TRY AGAIN:)")
        crop_suggestion(soil)
    elif soil == "red clay loam":
        print("THE CROPS SUITABLE IN RED CLAY LOAM IS")
        print("1.PIGEON PEA")
        select = int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if(select == 1):
            return "PIGEON PEA"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTION!!!PLEASE TRY AGAIN:)")
            crop_suggestion(soil)
    elif soil == "peaty soil":
        print("THE CROPS SUITABLE IN PEATY SOIL IS")
        print("1.GROUNDNUT")
        select = int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if(select == 1):
            return "Groundnut"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTION!!!PLEASE TRY AGAIN:)")
            crop_suggestion(soil)
    elif soil == "red clayey soils":
        print("THE CROPS SUITABLE IN RED CLAYEY SOILS IS")
        print("1.RICE")
        select = int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if(select == 1):
            return "Rice"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTION!!!PLEASE TRY AGAIN:)")
            crop_suggestion(soil)
    elif soil == "red sandy loam":
        print("THE CROPS SUITABLE IN RED SANDY LOAM IS")
        print("1.COTTON")
        select = int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if(select == 1):
            return "Cotton"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTION!!!PLEASE TRY AGAIN:)")
            crop_suggestion(soil)
    elif soil == "alluvial loam":
        print("THE CROPS SUITABLE IN ALLUVIAL SOILS IS")
        print("1.RICE")
        select = int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if(select == 1):
            return "Rice"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTION!!!PLEASE TRY AGAIN:)")
            crop_suggestion(soil)
    elif soil == "red loam":
        print("THE CROPS SUITABLE IN RED LOAM IS")
        print("1.RICE")
        select = int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if(select == 1):
            return "RICE"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTION!!!PLEASE TRY AGAIN:)")
            crop_suggestion(soil)
    elif soil == "sandy loam":
        print("THE CROPS SUITABLE IN SANDY LOAM IS")
        print("1.PIGEON PEA")
        select = int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if(select == 1):
            return "PIGEON PEA"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTION!!!PLEASE TRY AGAIN:)")
            crop_suggestion(soil)
    elif soil == "sandy soil":
        print("THE CROPS SUITABLE IN SANDY SOILS IS")
        print("1.GROUNDNUT")
        select = int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if(select == 1):
            return "GROUNDNUT"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTION!!!PLEASE TRY AGAIN:)")
        crop_suggestion(soil)
    elif soil == "red sandy soil":
        print("THE CROPS SUITABLE IN RED SANDY SOIL IS")
        print("1.SUGARCANE")
        select = int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if(select == 1):
            return "SUGARCANE"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTION!!!PLEASE TRY AGAIN:)")
            crop_suggestion(soil)
    elif soil == "clayey soil":
        print("THE CROPS SUITABLE IN CLAYEY SOIL IS")
        print("1.GROUNTNUT")
        select = int(input("PLEASE ENTER THE CORRESPONDING NUMBER FOR THE CROP YOU WANT TO SELECT:"))
        if(select == 1):
            return"GROUNDNUT"
        else:
            print("YOUR CHOICE DID NOT MATCHED WITH THE GIVEN OPTION!!!PLEASE TRY AGAIN:)")
            crop_suggestion(soil)




'''PREDECTING THE EXPECTED HARVEST DATE OF THE CROP SUGGESTED'''
def expected_date(crop,sd):
    d1=int(sd[0:2])
    m1=int(sd[3:5])     
    y1=int(sd[6:10])
    crop=crop.lower()
    if crop=="cotton":
        nd=180
        d1+=nd%30
        m1=m1+int(nd/30)
        if m1>12 or (m1==12 and d1>31):
            if m1>12:
                m1=m1-12
            y1+=1
        d2=str(d1)
        m2=str(m1)
        y2=str(y1)
        if len(d2)==1:
            d2='0'+d2
        if len(m2)==1:
            m2='0'+m2
        if len(y2)==1:
            y2='0'+y2
        date2 =d2+"/"+m2+"/"+y2
        return date2
    elif crop == "mirchi":
        nd = 180
        d1+= nd%30
        m1 = m1+int((nd/30))
        if m1>12 or m1==12 and d1>31:
            if m1>12:
                m1=m1-12
            y1+=1
        d2 = str(d1)
        m2 = str(m1)
        y2 = str(y1)
        if len(d2)==1:
            d2='0'+d2
        if len(m2)==1:
            m2='0'+m2
        if len(y2)==1:
            y2='0'+y2
        date2 =d2+"/"+m2+"/"+y2
        return date2
    elif crop == "rice":
        nd = 150
        d1+= nd%30
        m1 = m1+int((nd/30))
        if m1>12 or m1==12 and d1>31:
            if m1>12:
                m1=m1-12
            y1+=1
        d2 = str(d1)
        m2 = str(m1)
        y2 = str(y1)
        if len(d2)==1:
            d2='0'+d2
        if len(m2)==1:
            m2='0'+m2
        if len(y2)==1:
            y2='0'+y2
        date2 = d2+"/"+m2+"/"+y2
        return date2
    elif crop == "pigeon pea":
        nd = 210
        d1+= nd%30
        m1 = m1+int((nd/30))
        if m1>12 or m1==12 and d1>31:
            if m1>12:
                m1=m1-12
            y1+=1
        d2 = str(d1)
        m2 = str(m1)
        y2 = str(y1)
        if len(d2)==1:
            d2='0'+d2
        if len(m2)==1:
            m2='0'+m2
        if len(y2)==1:
            y2='0'+y2
        date2 =d2+"/"+m2+"/"+y2
        return date2
    elif crop == "sugarcane":
        nd = 180
        d1+= nd%30
        m1 = m1+int((nd//30))
        if m1>12 or m1==12 and d1>31:
            if m1>12:
                m1=m1-12
            y1+=1
        d2 = str(d1)
        m2 = str(m1)
        y2 = str(y1)
        if len(d2)==1:
            d2='0'+d2
        if len(m2)==1:
            m2='0'+m2
        if len(y2)==1:
            y2='0'+y2
        date2 = d2+"/"+m2+"/"+y2
        return date2
    elif crop=="groundnut":
        nd=150
        d1+= nd%30
        m1 = m1+int((nd/30))
        if m1>12 or m1==12 and d1>31:
            if m1>12:
                m1=m1-12
            y1+=1
        d2 = str(d1)
        m2 = str(m1)
        y2 = str(y1)
        if len(d2)==1:
            d2='0'+d2
        if len(m2)==1:
            m2='0'+m2
        if len(y2)==1:
            y2='0'+y2
        date2 =d2+"/"+m2+"/"+y2
        return date2

    

'''PRINTING THE ENTERED USER's DETAILS'''
def details(det):
    print("\n------------------YOUR DETAILS-------------------")
    print("UID:",det[0][2])
    print("NAME:",det[0][1])
    print("CROP NAME:",det[0][7])
    print("START DATE:",det[0][9])
    print("EXPECTED HARVEST DATE:",det[0][10])




'''FINDING THE NUMBER OF DAYS OF CROP BEING STARTED'''
def number_of_days(myresult):
    current_time = datetime.datetime.now()
    d1=current_time.day
    m1=current_time.month            #TODAY'S DATE
    y1=current_time.year
    sd=myresult[0][9]
    d2=int(sd[0:2])
    m2=int(sd[3:5])                 #GETTING THE START DATE
    y2=int(sd[6:10])
    date1=date(y1,m1,d1)
    date2=date(y2,m2,d2)
    no_days=(date1-date2).days      #NO.OF.DAYS
    return no_days




'''SUGGESTING THE PESTICIDES TO BE USED'''
def pesticides(nd,myresult):
    crop=myresult[0][7]
    crop=crop.lower()
    pesticide=""
    use=""
    if crop=="cotton":
        if nd<=20:
            mycursor.execute("select PESTICIDE from COTTON_PESTICIDES where DAYS='000-020'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from COTTON_PESTICIDES where DAYS='000-020'")
            use=mycursor.fetchall()
        elif nd>20 and nd<=60:
            mycursor.execute("select PESTICIDE from COTTON_PESTICIDES where DAYS='021-060'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from COTTON_PESTICIDES where DAYS='021-060'")
            use=mycursor.fetchall()
        elif nd>60 and nd<=90:
            mycursor.execute("select PESTICIDE from COTTON_PESTICIDES where DAYS='061-090'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from COTTON_PESTICIDES where DAYS='061-090'")
            use=mycursor.fetchall()
        elif nd>90 and nd<=120:
            mycursor.execute("select PESTICIDE from COTTON_PESTICIDES where DAYS='091-120'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from COTTON_PESTICIDES where DAYS='091-120'")
            use=mycursor.fetchall()
        elif nd>120 and nd<=150:
            mycursor.execute("select PESTICIDE from COTTON_PESTICIDES where DAYS='121-150'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from COTTON_PESTICIDES where DAYS='121-150'")
            use=mycursor.fetchall()
        elif nd>150 and nd<=180:
            mycursor.execute("select PESTICIDE from COTTON_PESTICIDES where DAYS='151-180'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from COTTON_PESTICIDES where DAYS='151-180'")
            use=mycursor.fetchall()
    elif crop=="pigeon pea":
        if nd<=20:
            mycursor.execute("select PESTICIDE from PIGEON_PEA_PESTICIDE where DAYS='000-020'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from PIGEON_PEA_PESTICIDE where DAYS='000-020'")
            use=mycursor.fetchall()
        elif nd>20 and nd<=50:
            mycursor.execute("select PESTICIDE from PIGEON_PEA_PESTICIDE where DAYS='021-050'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from PIGEON_PEA_PESTICIDE where DAYS='021-050'")
            use=mycursor.fetchall()
        elif nd>50 and nd<=90:
            mycursor.execute("select PESTICIDE from PIGEON_PEA_PESTICIDE where DAYS='051-090'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from PIGEON_PEA_PESTICIDE where DAYS='051-090'")
            use=mycursor.fetchall()
        elif nd>90 and nd<=125:
            mycursor.execute("select PESTICIDE from PIGEON_PEA_PESTICIDE where DAYS='091-125'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from PIGEON_PEA_PESTICIDE where DAYS='091-125'")
            use=mycursor.fetchall()
        elif nd>125 and nd<=160:
            mycursor.execute("select PESTICIDE from PIGEON_PEA_PESTICIDE where DAYS='126-160'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from PIGEON_PEA_PESTICIDE where DAYS='126-160'")
            use=mycursor.fetchall()
        elif nd>160 and nd<=210:
            mycursor.execute("select PESTICIDE from PIGEON_PEA_PESTICIDE where DAYS='161-210'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from PIGEON_PEA_PESTICIDE where DAYS='161-210'")
            use=mycursor.fetchall()
    elif crop=="rice":
        if nd<=25:
            mycursor.execute("select PESTICIDE from PADDY_PESTICIDES where DAYS='000-025'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from PADDY_PESTICIDES where DAYS='000-025'")
            use=mycursor.fetchall()
        elif nd>25 and nd<=40:
            mycursor.execute("select PESTICIDE from PADDY_PESTICIDES where DAYS='026-040'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from PADDY_PESTICIDES where DAYS='026-040'")
            use=mycursor.fetchall()
        elif nd>40 and nd<=80:
            mycursor.execute("select PESTICIDE from PADDY_PESTICIDES where DAYS='041-080'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from PADDY_PESTICIDES where DAYS='041-080'")
            use=mycursor.fetchall()
        elif nd>80 and nd<=110:
            mycursor.execute("select PESTICIDE from PADDY_PESTICIDES where DAYS='081-110'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from PADDY_PESTICIDES where DAYS='081-110'")
            use=mycursor.fetchall()
        elif nd>110 and nd<=150:
            mycursor.execute("select PESTICIDE from PADDY_PESTICIDES where DAYS='111-150'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from PADDY_PESTICIDES where DAYS='111-150'")
            use=mycursor.fetchall()
    elif crop=="mirchi":
        if nd <=30:
            mycursor.execute("select PESTICIDE from MIRCHI_PESTICIDES where DAYS='000-030'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from MIRCHI_PESTICIDES where DAYS='000-030'")
            use=mycursor.fetchall()
        elif nd>30 and nd<=50:
            mycursor.execute("select PESTICIDE from MIRCHI_PESTICIDES where DAYS='031-050'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from MIRCHI_PESTICIDES where DAYS='031-050'")
            use=mycursor.fetchall()
        elif nd>50 and nd<=70:
            mycursor.execute("select PESTICIDE from MIRCHI_PESTICIDES where DAYS='051-070'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from MIRCHI_PESTICIDES where DAYS='051-070'")
            use=mycursor.fetchall()
        elif nd>70 and nd<=95:
            mycursor.execute("select PESTICIDE from MIRCHI_PESTICIDES where DAYS='071-095'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from MIRCHI_PESTICIDES where DAYS='071-095'")
            use=mycursor.fetchall()
        elif nd>95 and nd<=135:
            mycursor.execute("select PESTICIDE from MIRCHI_PESTICIDES where DAYS='096-135'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from MIRCHI_PESTICIDES where DAYS='096-135'")
            use=mycursor.fetchall()
        elif nd>135 and nd<=180:
            mycursor.execute("select PESTICIDE from MIRCHI_PESTICIDES where DAYS='136-180'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from MIRCHI_PESTICIDES where DAYS='136-180'")
            use=mycursor.fetchall()
    elif crop=="sugarcane":
        if nd<=30:
            mycursor.execute("select PESTICIDE from SUGARCANE_PESTICIDES where DAYS='000-030'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from SUGARCANE_PESTICIDES where DAYS='000-030'")
            use=mycursor.fetchall()
        elif nd>30 and nd<=70:
            mycursor.execute("select PESTICIDE from SUGARCANE_PESTICIDES where DAYS='031-070'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from SUGARCANE_PESTICIDES where DAYS='031-070'")
            use=mycursor.fetchall()
        elif nd>70 and nd<=110:
            mycursor.execute("select PESTICIDE from SUGARCANE_PESTICIDES where DAYS='071-110'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from SUGARCANE_PESTICIDES where DAYS='071-110'")
            use=mycursor.fetchall()
        elif nd>110 and nd<=150:
            mycursor.execute("select PESTICIDE from SUGARCANE_PESTICIDES where DAYS='111-150'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from SUGARCANE_PESTICIDES where DAYS='111-150'")
            use=mycursor.fetchall()
            print(use)
        elif nd>150 and nd<=180:
            mycursor.execute("select PESTICIDE from sugarcane_PESTICIDES where DAYS='151-180'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from sugarcane_PESTICIDES where DAYS='151-180'")
            use=mycursor.fetchall()
    elif crop=="groundnut":
        if nd<=25:
            mycursor.execute("select PESTICIDE from GROUNDNUT_PESTICIDES where DAYS='000-025'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from GROUNDNUT_PESTICIDES where DAYS='000-025'")
            use=mycursor.fetchall()
        elif nd>25 and nd<=40:
            mycursor.execute("select PESTICIDE from GROUNDNUT_PESTICIDES where DAYS='026-040'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from GROUNDNUT_PESTICIDES where DAYS='026-040'")
            use=mycursor.fetchall()
        elif nd>40 and nd<=70:
            mycursor.execute("select PESTICIDE from GROUNDNUT_PESTICIDES where DAYS='041-070'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from GROUNDNUT_PESTICIDES where DAYS='041-070'")
            use=mycursor.fetchall()
        elif nd>70 and nd<=100:
            mycursor.execute("select PESTICIDE from GROUNDNUT_PESTICIDES where DAYS='071-100'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from GROUNDNUT_PESTICIDES where DAYS='071-100'")
            use=mycursor.fetchall()
        elif nd>100 and nd<=150:
            mycursor.execute("select PESTICIDE from GROUNDNUT_PESTICIDES where DAYS='101-150'")
            pesticide=mycursor.fetchall()
            mycursor.execute("select USES from GROUNDNUT_PESTICIDES where DAYS='101-150'")
            use=mycursor.fetchall()

    
    
    print("\nIT'S BEEN {0} DAYS,SO THE PESTCIDES AND THEIR DOSAGES THAT CAN BE USED ARE AS  FOLLOWS:\n".format(nd))
    for i in pesticide[0]:
        s=i.split(".")
        for j in range(len(s)):
            if j==0 or j%2==0:
                print("PESTICIDE:"+s[j])
            else:
                print("DOSAGE:"+s[j]+'\n')
    print("USES OF THE PESTICIDES ARE:")
    print(use[0][0])
    insert(myresult,pesticide)


'''TO INSERT THE PESTICIDE SUGGESTED INTO THE DATABASE'''
def insert(myresult,pesticide):
    mycursor.execute("select * from PESTICIDES_USED")
    res=mycursor.fetchall()
    sn=str(len(res)+1)
    uid=str(myresult[0][2])
    pest=''
    for i in pesticide[0]:
        s=i.split(".")
        for j in range(len(s)):
            if j==0 or j%2==0:
                pest=pest+s[j]+'    '
    current_time = datetime.datetime.now()
    d1=str(current_time.day)
    m1=str(current_time.month)           #TODAY'S DATE
    y1=str(current_time.year)
    date=d1+'/'+m1+'/'+y1
    
    q='''insert into PESTICIDES_USED(SNO,ID,DATE_OF_QUERY,PESTICIDE)values(%s,%s,%s,%s)'''
    val=(sn,uid,date,pest)
    mycursor.execute(q,val)
    mydb.commit()
    



'''GIVING THE BEST PRICE AVAILABLE'''
def dealers(deal):
    pass



'''IF THE ENTERED UID IS NOT MATCHED IN THE DATABASE'''
def missing():
    print("\nSORRY!!THE ENTERED ID IS NOT PRESENT IN THE DATABASE\n")
    print("IF YOU WANT TO TRY AGAIN,THEN ENTER 1\nIF YOU ARE NEW TO 'ANNADATA SUKHIBAVA',THEN ENTER 2\nENTER 0 TO EXIT\n")
    choice=int(input("Enter your choice:"))
    if choice==1:
       search(int(input("Enter your UID:")))
    elif choice==2:
        new_entry()
    elif choice==0:
        exit()


''' TO DISPLAY ALL THE PESTICIDES USED SO FAR'''
def display_pesticides(myresult):
    uid=str(myresult[0][2])
    mycursor.execute(f"select ID,DATE_OF_QUERY,PESTICIDE from PESTICIDES_USED where ID={uid}")
    res = mycursor.fetchall()
    if len(res)==0:
        print("\nWE DID'NT SUGGESTE ANY PESTICIDES SO FAR")
    else:
        print("\nTHE PESTICIDES RECOMMENED SO FAR ARE AS FOLLOWS:")
        for i in res:
            print("UID            :",i[0])
            print("DATE OF QUERY  :",i[1])
            print("PESTICIDE      :",i[2])
            print()
            
                
    


'''TO CHECK WHETHER THE CROP HAS REACHED THE HARVEST DATE OR NOT'''
def check_for_harvest(myresult):
    current_time = datetime.datetime.now()
    d1=current_time.day
    m1=current_time.month            #TODAY'S DATE
    y1=current_time.year
    hd=myresult[0][10]
    d2=int(hd[0:2])
    m2=int(hd[3:5])                 #GETTING THE HARVEST DATE
    y2=int(hd[6:10])
    date1=date(y1,m1,d1)
    date2=date(y2,m2,d2)
    no_days=(date2-date1).days
    #print(no_days)
    if no_days<=0:
        return True



'''IF THE ID IS FOUND'''
def found(myresult):
    if check_for_harvest(myresult):
            print("YOUR CROP IS READY FOR THE HARVEST...")
            exit()                  #UNTILL THE DEALERS FUNCTION IS READY
            dealers(myresult)
    nd=number_of_days(myresult)
    print("\nENTER '1' TO GET YOUR DETAILS\nENTER '2' TO GET SUGGESTIONS FOR THE PESTICIDES TO USE\nENTER '3' TO KNOW WHAT ARE ALL THE PESTICIDES USED SO FOR\nENTER '4' TO EXIT\n")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        details(myresult)
        found(myresult)
    elif choice==2:
        pesticides(nd,myresult)
        found(myresult)
    elif choice==3:
        display_pesticides(myresult)
        found(myresult)
    elif choice==4:
        print("THANK YOU!!")
        exit() 



'''SEARCHING THE ENTERED UID IN THE DATABASE'''        
def search(s):
    mycursor.execute(f"select * from Farmer_Details where UID={s}")
    myresult = mycursor.fetchall()
    if len(myresult)==0:
        missing()
    else:
        found(myresult)     



print("""--------WELCOME TO ANNADATA SUKHIBHAVA---------
IF YOUR ARE NEW TO ANNADATA SUKHIBHAVA ENTER "0"
ELSE
ENTER YOUR ID""")
s=int(input("INPUT:"))
if s==0:
    new_entry()
else:
    search(s)
