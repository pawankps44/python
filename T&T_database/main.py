import sqlite3


def Create_table():
    connection = sqlite3.connect('cinema.db')
    connection.execute(""" 
CREATE TABLE "Seat" (
	"seat_id"	TEXT,
	"Availabilty"	INTEGER,
	"Price"	REAL
);
""")
    connection.commit()
    connection.close()


# Create_table()

def insert_record():
    connection = sqlite3.connect('cinema.db')
    connection.execute(""" 
    INSERT INTO "Seat" 
    	("seat_id","Availabilty","Price") VALUES ("A1","0","100"),("A2",'1',"90"),('A3',"0","100")
    """)
    connection.commit()
    connection.close()


def select_all_record():
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM "Seat" 
    """)
    result = cursor.fetchall()
    print(result)
    connection.close()

def select_specific_columns():
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT "seat_id","Price" FROM "Seat"
    """)
    result = cursor.fetchall()
    print(result)
    connection.close()

def select_specific_values():
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute("""
        SELECT "seat_id","Price" FROM "Seat" WHERE "Price" >90
        """)
    result = cursor.fetchall()
    print(result)
    connection.close()

def update_records():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
            UPDATE "Seat" SET "Availabilty" = 1 WHERE "Price" = 100
            """)
    connection.commit()
    connection.close()

def delete_records():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
                DELETE  FROM "Seat" WHERE "seat_id" = "A3"
                """)
    connection.commit()
    connection.close()

# insert_record()
# select_all_record()
# select_specific_columns()
# select_specific_values()

# update_records()
delete_records()