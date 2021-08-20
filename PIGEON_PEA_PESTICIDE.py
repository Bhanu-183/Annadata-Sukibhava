import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", password="pa$$word", database="Annadata_Sukhibava")

mycursor=mydb.cursor()

mycursor.execute("create table PIGEON_PEA_PESTICIDE(DAYS varchar(10) primary key, PESTICIDE varchar(1000), USES varchar(500));")

data="""insert into PIGEON_PEA_PESTICIDE values
("000-020","HNPV or Neem extract.Dosage:50gm/Litre of water","Use disease free seeds and Use of chemicals are necessary after ETL level."),
("021-050","Deltamethrin 2.8EC.Dosage:200ml per acre using 100-125 litres of water per acre","Take spray in evening hours and if necessary repeat the spray after 10 days."),
("051-090","Spinosad 45SC.Dosage:60ml/100-125litres of water per acre ","Install Pheromone traps for Helicoverpa armigera @ 12/ha."),
("091-125","Fenazaquin 10% EC.Dosage:300 ml/acre with 200 Ltr water","Controls mite and in severe conditions, spray crop with Mancozeb "),
("126-160","Mix of 1 kg of Trichoderma in 200 kg well decomposed cow dung.Dosage:300ml/200 Litre of water per acre","Keep it for 21-28 days, then apply it in wilt affected area."),
("161-210","Mancozeb.Dosage:64% 2gm/Ltr of water","Infestation Phytophthora blight is controlled and the crop is ready to be harvested.");"""

mycursor.execute(data)
mydb.commit()


