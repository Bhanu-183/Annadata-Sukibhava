import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="pa$$word",database="Annadata_Sukhibava")

mycursor=mydb.cursor()

mycursor.execute("create table SUGARCANE_PESTICIDES(DAYS varchar(10) primary key,PESTICIDE varchar(1000),USES varchar(500));")

data="""insert into SUGARCANE_PESTICIDES values
("000-030","use beauvaria bassiana 1.15% bio pesticides mixed with 60.75 farm yard manure and water sprinkled on it,kept for 8-0 days in shade.Dosage:3-5 kg per hectare","To save from termite insect"),
("031-070","malathion dissolved in 1250 litre water.Dosage: 1 litre","it saves from white flies"),
("071-110","Fenvalrate.Dosage:25 kg 10% EC","To kill white guidar"),
("111-150","tricograma.Dosage: 10 cards per hectare","to kill early shoot borer"),
("151-180","Burn the dry leaves after harvesting of sugarecane","To kill shalk insect");"""

mycursor.execute(data)
mydb.commit()
