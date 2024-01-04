import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="studentdb"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# CREATE - Insert a new record
def create_record(first_name, last_name, age, grade):
    query = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
    values = (first_name, last_name, age, grade)
    cursor.execute(query, values)
    conn.commit()
    print("Record created successfully")

# READ - Fetch all records
def read_records():
    query = "SELECT * FROM students"
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)

# UPDATE - Update a record by FirstName
def update_record(first_name, grade):
    query = "UPDATE students SET grade = %s WHERE first_name = %s"
    values = (grade, first_name)
    cursor.execute(query, values)
    conn.commit()
    print("Record updated successfully")

# DELETE - Delete a record by LastName
def delete_record(last_name):
    query = "DELETE FROM students WHERE last_name = %s"
    values = (last_name,)
    cursor.execute(query, values)
    conn.commit()
    print("Record deleted successfully")

# Function Call
#create_record("John", "Carter", 25, 95.5)
read_records()
#update_record("Alice", 97.0)
#read_records()
#delete_record("Carter")
#read_records()

# Close the cursor and connection
cursor.close()
conn.close()
