import sqlite3

conn = sqlite3.connect('people.sqlite')

cursor = conn.cursor()

#Table creation
query = """ CREATE TABLE people ( 
            id integer PRIMARY KEY,
            name varchar(100) NOT NULL,
            lastname varchar(150) NOT NULL,
            email varchar(200) NOT NULL,
            address text,
            reference_address text,
            phone_number varchar(20)
            )
        """
cursor.execute(query)
conn.commit()

#Fill the table

sql= "INSERT INTO people (name,lastname,email,address,reference_address,phone_number) values (?,?,?,?,?,?)"

cursor.execute(sql,("Fabrizio","Garcia","fabrizio.garcia@utec.edu.pe","Oasis 160 Remigio Silva", "Mercado del pueblo","951378747"))

conn.commit()

cursor.execute(sql,("Jorge","Wong","jwong@utec.edu.pe","Tumbes 154", "","923147489"))

conn.commit()


cursor.execute(sql,("Rodrigo","Arriaga","rodrigo.arriaga@utec.edu.pe","", "","989114423"))

conn.commit()
