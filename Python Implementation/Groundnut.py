import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='pa$$word',
    database='Annadata_Sukhibava'
)
mycursor = mydb.cursor()
mycursor.execute("create table GROUNDNUT_PESTICIDES(DAYS varchar(10) primary key,PESTICIDE varchar(1000),USES varchar(500));")

data = """insert into GROUNDNUT_PESTICIDES values
("000-025","Quizalofop Ethyl.Dosage:5% EC WDG:2 g/litre","It is used to control narrow leaf weeds in broad leaf crops"),
("026-040","Carboxin 38% + Thiram 36% DS G:1 mL /litre.Mortar.Dosage:2 mL /litre.Chlorantraniliprole 18.5% W/W SC.Dosage:2 g/litre","Which controls seed and soil borne diseases"),
("041-070","Lustre SC.Dosage:2 mL /litre.Caldan 50SP.Dosage:3 g/litre","To control the longer duration diseases"),
("071-100","Imidacloprid 18% SL Sc.Dosage:3 mL/L.Thiamethoxam 25% Wg.Dosage:2mL/litre","Which control the sucking insects and termites very effectively"),
("101-150","Mancozeb 63%Wp.Dosage:3 mL/L.Carbendazim 12%Wp:3 gm SL.Dosage:2 gm/L.Spectrum.Dosage:1 mL/litre","Germination and ensures double protection from inside & from outside");
"""
mycursor.execute(data)
mydb.commit()
