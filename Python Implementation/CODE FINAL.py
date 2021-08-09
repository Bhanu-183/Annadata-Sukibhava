import tkinter as tk 
import mysql.connector 
from tkinter import *
import PIL 
import random
from datetime import date 
import datetime
from tkinter import messagebox 


'''GETTING THE UID ENTERED'''
def submitact(): 
    user=id.get()
    if len(user)==0:
        messagebox.showerror("ERROR", "ENTER AN UID!!")
    else:
        s=int(user)
        result=logintodb(s)



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


    
'''SEARCHING THE UID IN DATABASE'''
def logintodb(s):
    mycursor.execute(f"select * from Farmer_Details where UID={s}")
    global myresult
    myresult=mycursor.fetchall()
    if len(myresult)==0:
        notfound=tk.Label(root, text ="SORRY!!! THE ID ENTERED IS NOT REGISTERED") 
        notfound.place(x=70,y=240)
    else:
        if check_for_harvest(myresult):
            '''dealers=tk.Tk()
            dealers.geometry("5000x5000") 
            dealers.title("DEALERS")           #UNTILL THE DEALERS FUNCTION IS READY'''
            messagebox.showerror("MESSAGE","TIME FOR HARVEST!!")
            #dealers(myresult)
        else:
            sucess=tk.Tk()
            sucess.geometry("5000x5000") 
            sucess.title("WELCOME TO ANNADATA SUKHIBAVA")
        
            '''DETAILS BUTTON'''
            detailsbtn = tk.Button(sucess, text ="DETAILS",bg ='GREEN',height=5,width=100,command = details) 
            detailsbtn.place(x = 400, y = 170)

            ''''PESTICIDES BUTTON'''
            pesticidesbtn = tk.Button(sucess, text ="PESTICIDE SUGGESTIONS",bg ='GREEN',height=5,width=100,command = pesticides) 
            pesticidesbtn.place(x = 400, y = 300)

            '''PESTICIDES USE SO FAR BTN'''
            usedbtn = tk.Button(sucess, text ="PESTICIDES USED SO FAR",bg ='GREEN',height=5,width=100,command = display_pesticides) 
            usedbtn.place(x = 400, y = 430)

            '''EXIT BUTTON'''
            exitbtn = tk.Button(sucess, text ="EXIT",bg ='RED',height=5,width=100,command=sucess.destroy) 
            exitbtn.place(x = 400, y = 560)
        


'''DISPLAYING THE DETAILS OF THE USER'''
def details():
    details=tk.Tk()
    details.geometry("5000x5000") 
    details.title("DETAILS OF THE USER")
    one='\n\n\n\n\nUID='+str(myresult[0][2])
    UID = tk.Label(details, text=one,)
    UID.config(font=('times', 20, 'italic'),width=35)
    UID.pack()
    name='\n\n\nNAME='+str(myresult[0][1])
    NAME = tk.Label(details, text=name)
    NAME.config(font=('times', 20, 'italic'),width=35)
    NAME.pack()
    cname='\n\n\nCROP NAME='+str(myresult[0][7])
    CNAME = tk.Label(details, text=cname)
    CNAME.config(font=('times', 20, 'italic'),width=35)
    CNAME.pack()
    sdate='\n\n\nSTART DATE='+str(myresult[0][9])
    SDATE = tk.Label(details, text=sdate)
    SDATE.config(font=('times', 20, 'italic'),width=35)
    SDATE.pack()
    edate='\n\n\nEXPECTED HARVEST DATE='+str(myresult[0][10])
    EDATE = tk.Label(details, text=edate)
    EDATE.config(font=('times', 20, 'italic'),width=35)
    EDATE.pack()
    backbtn = tk.Button(details, text ="BACK",bg ='red',height=3,width=5,command=details.destroy) 
    backbtn.place(x=950,y=900)




'''FINDING THE NUMBER OF DAYS OF CROP BEING STARTED'''
def number_of_days():
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



'''RECOMENDING THE PESTICIDES USED'''
def pesticides():
    pests=tk.Tk()
    pests.geometry("1000x500") 
    pests.title("PESTICIDES SUGGESTION")
    crop=myresult[0][7]
    crop=crop.lower()
    pesticide=""
    use=""
    temp=''
    nd=number_of_days()
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

    
    insert(pesticide)    
    ourMessage="\nIT'S BEEN {0} DAYS,SO THE PESTCIDES AND THEIR DOSAGES THAT CAN BE USED ARE AS  FOLLOWS:\n".format(nd)
    messageVar = Message(pests,text = ourMessage,width=900)
    messageVar.config(font=('times', 20, 'italic'))
    messageVar.pack()
    pest=pesticide[0][0].split('.')
    for i in range(len(pest)):
        if i==0 or i%2==0:
            temp+="PESTICIDE:"+pest[i]+'\n'
        else:
            temp+=pest[i]+'\n\n'
    p=Label(pests,text=temp,width=1000)
    p.config(font=('times', 20, 'italic'))
    p.pack()
    backbtn = tk.Button(pests,text ="BACK",bg ='red',height=3,width=5,command=pests.destroy) 
    backbtn.place(x=950,y=600)
    pests.mainloop()    



'''TO INSERT THE PESTICIDE SUGGESTED INTO THE DATABASE'''
def insert(pesticide):
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

    

'''DISPLAYING THE PESTICIDES SUGGESTED SO FAR..'''
def display_pesticides():
    display=tk.Tk()
    display.geometry("1200x600") 
    display.title("PESTICIDES SUGGESTED SO FAR")
    uid=str(myresult[0][2])
    mycursor.execute(f"select ID,DATE_OF_QUERY,PESTICIDE from PESTICIDES_USED where ID={uid}")
    res = mycursor.fetchall()
    if len(res)==0:
        msg= tk.Label(display,text ="WE DID'NT SUGGEST ANY PESTICIDES SO FAR...")
        msg.config(font=('times', 20, 'italic'))
        msg.place(x=320,y=250) 
    else:
        temp=''
        for i in res:
            temp+='\n\n\n\nPESTICIDES:'+i[2]+'\n'+'DATE OF QUERY:'+i[1]
            
        ps=Label(display,text=temp,width=1000)
        ps.config(font=('times', 20, 'italic'))
        ps.pack()
    backbtn = tk.Button(display, text ="BACK",bg ='red',height=3,width=5,command=display.destroy) 
    backbtn.place(x=950,y=900)
    display.mainloop()



'''NEW USER'''
def newuser():
    global new_user         
    new_user=tk.Tk()
    new_user.geometry("3000x1000") 
    new_user.title("NEW USER PAGE")
    ourMessage="\nPLEASE ENTER THE DETAILS ASKED\n"
    message=Label(new_user,text=ourMessage,anchor='w',font=('times', 15, 'italic')).pack(fill='both')


    '''NAME'''
    name=tk.Label(new_user,text="NAME:") 
    name.place(x=0,y=90)
    namefinal=StringVar()
    global namein
    namein=tk.Entry(new_user,width=30,textvariable=namefinal) 
    namein.place(x=70,y=90)


    '''PHONE NUMBER'''
    phno=tk.Label(new_user,text="PHNO:")
    phno.place(x=0,y=170)
    global phnoin
    phnoin=tk.Entry(new_user,width=30) 
    phnoin.place(x=70,y=170)


    ''' GENDER'''
    gend=tk.Label(new_user,text="GENDER:").place(x=0,y=230)
    global var
    var=IntVar()
    R1=Radiobutton(new_user,text="MALE",variable=var,value=1,command=sel).place(x=20,y=250)
    R2=Radiobutton(new_user,text="FEMALE",variable=var,value=2,command=sel).place(x=20,y=270)
    
    
    '''VILLAGE'''
    vill=tk.Label(new_user,text="LOCATION:")
    vill.place(x=0,y=340)
    global village
    village=tk.Entry(new_user,width=30) 
    village.place(x=100,y=340)



    '''SOILS'''
    lbl = Label(new_user,text = "SELECT THE SOIL")
    lbl.place(x=0,y=370)
    global listbox
    listbox = Listbox(new_user)
    listbox.place(x=10,y=370) 
    listbox.insert(1,"Clay Loam")  
    listbox.insert(2, "Peaty soil")  
    listbox.insert(3, "Slit Loam")  
    listbox.insert(4, "Sandy soil")
    listbox.insert(5, "Sandy Loam")
    listbox.insert(6,"Clayey soil")  
    listbox.insert(7, "Red Clayey Soils")  
    listbox.insert(8, "Red Sandy Loam")  
    listbox.insert(9, "Black Soil")
    listbox.insert(10, "Red Loam")
    listbox.insert(11,"Alluvial Loam")  
    listbox.insert(12, "chalky Soil")  
    listbox.insert(13, "Red Sandy Soil")  
    listbox.insert(14, "Red Soil")
    listbox.insert(15, "Red clay loam")
    lbl.pack()
    listbox.pack()


    '''ACERS'''
    acers=tk.Label(new_user,text="NO.OF ACERS:") 
    acers.place(x=0,y=410)
    acersfinal=StringVar()
    global acersin
    acersin=tk.Entry(new_user,width=30,textvariable=acersfinal) 
    acersin.place(x=130,y=410)



    '''START DATE'''
    sd=tk.Label(new_user,text="START DATE:") 
    sd.place(x=0,y=480)
    sdfinal=StringVar()
    global sdin
    sdin=tk.Entry(new_user,width=30,textvariable=sdfinal) 
    sdin.place(x=130,y=480)

    
    '''CROPS BUTTON'''
    cropsbtn=tk.Button(new_user,text="CROPS",bg ='orange',command=getcrops) 
    cropsbtn.place(x=1200,y=300,width=95) 
    
    '''SUBMIT BUTTON'''
    submitbtn=tk.Button(new_user,text="SUBMIT",bg ='red',command=sub) 
    submitbtn.place(x=200,y=600,width=95)

    '''REFERSH BUTTON'''
    refreshbtn=tk.Button(new_user,text="REFRESH",bg ='yellow',command=refresh) 
    refreshbtn.place(x=400,y=600,width=95)
    
    new_user.mainloop()




'''SUBMIT BUTTON ACTION'''
def sub():
    namef=namein.get()
    phnof=str(phnoin.get())
    genf=sel()
    unid=uid()
    locf=village.get()
    soilf=listbox.get(ANCHOR)
    if status==0:
       messagebox.showerror("ERROR", "PLEASE SELECT A SOIL TYPE AND CROP")
    else:
        cropf=cropbox.get(ANCHOR)
        acersf=acersin.get()
        sdf=sdin.get()
        if len(namef)==0 or len(phnof)==0 or len(genf)==0 or len(soilf)==0 or len(cropf)==0 or len(acersf)==0 or len(sdf)==0:
            messagebox.showerror("ERROR", "NO FIELD SHOULD BE LEFT EMPTY!!")
            new_user.destroy()
            newuser()
        else:
            edf=expected_date(cropf,sdf)
            mycursor.execute("select * from Farmer_Details")
            res=mycursor.fetchall()
            snf=len(res)+1
            q="""INSERT INTO Farmer_Details(SNO,NAME,UID,PHNO,GENDER,LOCATION,SOIL_TYPE,CROP_NAME,ACERS,START_DATE,EXPECTED_HARVEST_DATE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            ar=(snf,namef,unid,phnof,genf,locf,soilf,cropf,acersf,sdf,edf)
            mycursor.execute(q,ar)
            mydb.commit()
            new_user.destroy()

    
            newuser_details=tk.Tk()
            newuser_details.geometry("5000x5000")
            newuser_details.title("NEW USER DETAILS")

            mycursor.execute(f"select * from Farmer_Details where UID={unid}")
            res=mycursor.fetchall()
            one='\n\n\n\n\nUID='+str(res[0][2])
            UID = tk.Label(newuser_details, text=one,)
            UID.config(font=('times', 20, 'italic'),width=35)
            UID.pack()
            name='\n\n\nNAME='+str(res[0][1])
            NAME = tk.Label(newuser_details, text=name)
            NAME.config(font=('times', 20, 'italic'),width=35)
            NAME.pack()
            cname='\n\n\nCROP NAME='+str(res[0][7])
            CNAME = tk.Label(newuser_details, text=cname)
            CNAME.config(font=('times', 20, 'italic'),width=35)
            CNAME.pack()
            sdate='\n\n\nSTART DATE='+str(res[0][9])
            SDATE = tk.Label(newuser_details, text=sdate)
            SDATE.config(font=('times', 20, 'italic'),width=35)
            SDATE.pack()
            edate='\n\n\nEXPECTED HARVEST DATE='+str(res[0][10])
            EDATE = tk.Label(newuser_details, text=edate)
            EDATE.config(font=('times', 20, 'italic'),width=35)
            EDATE.pack()
            backbtn = tk.Button(newuser_details, text ="BACK",bg ='red',height=3,width=5,command=newuser_details.destroy) 
            backbtn.place(x=950,y=900)



def sel():
    global temp
    temp=var.get()
    g=''
    if temp==1:
        g='M'
    elif temp==2:
        g='F'
    else:
        g='M'
    return g

    

'''ASSIGNING AN UNIQUE UID TO THE NEW USER'''
def uid():
    unid=random.randrange(1,10000)
    mycursor.execute(f"select * from Farmer_Details where UID={unid}")
    res=mycursor.fetchall()
    if len(res)==0:
        return unid
    else:
        uid()




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


    
'''CROP SELECTION'''
def getcrops():
    global status
    status=1
    soilf=listbox.get(ANCHOR)
    global crop
    crop=crop_suggestion(soilf)

    msg = Label(new_user,text = "SELECT THE CROP")
    msg.place(x=0,y=390)
    global cropbox
    cropbox = Listbox(new_user)
    for i in range(len(crop)):
        cropbox.place(x=10,y=390) 
        cropbox.insert(1+i,crop[i])  
    msg.pack()
    cropbox.pack()
    


'''REFERSH ACTION'''
def refresh():
    new_user.destroy()
    newuser()


    
def crop_suggestion(soil):
    soil=soil.lower()
    temp=[]
    if soil=="black soil":
        temp.append("Cotton")
        temp.append("Mirchi")
        temp.append("Sugarcane")
    elif soil=="slit loam":
        temp.append("Cotton")
        temp.append("Groundnut")
    elif soil=="red soil":
        temp.append("Mirchi")
    elif soil == "clay loam":
        temp.append("Rice")
    elif soil == "chalky soil":
        temp.append("Groundnut")
    elif soil == "red clay loam":
        temp.append("Pigeon Pea")
    elif soil == "peaty soil":
        temp.append("Groundnut")
    elif soil == "red clayey soils":
        temp.append("Rice")
    elif soil == "red sandy loam":
        temp.append("Cotton")
    elif soil == "alluvial loam":
        temp.append("Rice")
    elif soil == "red loam":
        temp.append("Rice")
    elif soil == "sandy loam":
        temp.append("Pigeon Pea")
    elif soil == "sandy soil":
        temp.append("Groundnut")
    elif soil == "red sandy soil":
         temp.append("Sugarcane")
    elif soil == "clayey soil":
         temp.append("Groundnut")
    return temp
    
    

        
    

'''ESTABLISHING THE CONNECTION WITH THE MySQL SERVER'''
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="pa$$word",
    database="Annadata_Sukhibava"
    )
mycursor = mydb.cursor()

root = tk.Tk() 
root.geometry("500x300") 
root.title("ANNADATA SUKHIBAVA LOGIN PAGE") 

C = Canvas(root, bg ="blue", height = 250, width = 300) 

'''TAKING THE UID AS INPUT'''
lblfrstrow = tk.Label(root, text ="UID") 
lblfrstrow.place(x=140,y=50)


id= tk.Entry(root, width = 35) 
id.place(x=200, y = 50, width = 100) 

'''LOGIN BUTTON'''
loginbtn=tk.Button(root,text="LOGIN",bg='blue',command=submitact) 
loginbtn.place(x=200,y=135,width=95)

status=0
'''NEW USER BUTTON'''
newuserbtn=tk.Button(root, text="NEWUSER",bg ='red',command=newuser) 
newuserbtn.place(x=200,y=180,width=95) 

root.mainloop()






    

