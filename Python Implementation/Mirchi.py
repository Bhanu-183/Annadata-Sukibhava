import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='pa$$word',
    database='Annadata_Sukhibava'
)
mycursor = mydb.cursor()
mycursor.execute("create table MIRCHI_PESTICIDES(DAYS varchar(10) primary key,PESTICIDE varchar(1000),USES varchar(500));")

data = """insert into MIRCHI_PESTICIDES values
("000-030","Bengard.Dosage:2 g/litre.Anant.Dosage:1 g/litre.Kranti.Dosage:2 mL/litre.Spraywell.Dosage.1 mL/litre","For leaf sopt and Damping off"),
("031-050","Econeem plus.Dosage:1 mL /litre.Jashn.Dosage:2 mL /litre.Saaf.Dosage:2 g/litre.Viral out.Dosage:2 gm/L","Against the Thrips and plant hoppers"),
("051-070","Gibrax phytozyme.Dosage:2 mL /litre.M6 [20% Bo].Dosage:1 g/litre.Ridomil gold 80 WP.Dosage:2 g/litre","Against leaf eating caterpillars and Aphids"),
("071-095","Multiplex General liquid.Dosage:3 mL/L.Marshall.Dosage:2mL/litre.V–Bind.Dosage:3 mL/L.Avtar.Dosage:2 g/litre","Against Thrips and fruit Borers and white flies"),
("096-135","Confidor.Dosage:1 mL/L.Silixol.Dosage:2 mL/L.Kavach.Dosage:2 gm/L.Spraywell.Dosage:1 mL/litre","Against mites and root knot nematodes"),
("136-180","Kavach.Dosage:2 gm/L.Spraywell.Dosage:1 mL/litre","Against mites and root knot nematodes");
"""
mycursor.execute(data)
mydb.commit()
