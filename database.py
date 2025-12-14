import sqlite3

# Database setup
connection=sqlite3.connect("student.db")

# Create cursor
cursor=connection.cursor()

# Create the table
create_table_query="""
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME    VARCHAR(25),
    COURSE   VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS   INT
);
"""

cursor.execute(create_table_query)

# Insert Records
sql_query = """INSERT INTO STUDENT (NAME, COURSE, SECTION, MARKS) VALUES (?, ?, ?, ?)"""
values = [
    ('Student1', 'Data Science', 'A', 90),
    ('Student2', 'Python', 'B', 78),
    ('Student3', 'Java', 'C', 85),
    ('Student4', 'DEVOPS', 'A', 50),
    ('Student5', 'Data Science', 'B', 92),
    ('Student6', 'Python', 'A', 88),
    ('Student7', 'Java', 'B', 76),
    ('Student8', 'DEVOPS', 'C', 61),
    ('Student9', 'Data Science', 'A', 95),
    ('Student10', 'Python', 'B', 82),
    ('Student11', 'Java', 'A', 89),
    ('Student12', 'DEVOPS', 'B', 54),
    ('Student13', 'Data Science', 'C', 91),
    ('Student14', 'Python', 'A', 80),
    ('Student15', 'Java', 'C', 73),
    ('Student16', 'DEVOPS', 'A', 65),
    ('Student17', 'Data Science', 'B', 87),
    ('Student18', 'Python', 'C', 79),
    ('Student19', 'Java', 'B', 90),
    ('Student20', 'DEVOPS', 'C', 58)

]

cursor.executemany(sql_query, values)
connection.commit()

# Display the records
data=cursor.execute("""Select * from STUDENT""")

for row in data:
    print(row)

if connection:
    connection.close()