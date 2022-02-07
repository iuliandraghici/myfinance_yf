# create a database for a hospital, make these tables: patients, doctors & medicine
# patients have a name, email, telephone & a family doctor assigned
# doctors have a name & specialty
# medicine has a name, type & number of items in stock
# create method for removing an amount of medicine from stock
# create methods for adding a medicine, patient & doctors
# create method for removing patient & doctors
# create method for listing all medicines & doctors
import sqlite3


def connect_to_database():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()
    return connection, cursor

def execute_sql(commands: list[str]):
    connection, cursor = connect_to_database()
    for one_command in commands:
        cursor.execute(one_command)
    connection.commit()  # we save to the system
    connection.close()  # we close so other processes can write


def init_database():
    commands = ["CREATE TABLE patients ('name' TEXT, 'doctor' TEXT)",
                "CREATE TABLE doctors ('name' TEXT, 'specialty' TEXT)",
                "CREATE TABLE medicine ('name' TEXT, 'items' INTEGER)"]
    execute_sql(commands)


# init_database()

#               ('name' TEXT, 'items' INTEGER)
def add_medicine(name: str, items: int):
    commands = ["INSERT INTO medicine (name, items) VALUES ('" + name + "', " + str(items) + ")"]
    execute_sql(commands)


# add_medicine("faringosept", 200)

def take_medicine(name: str, items_to_remove: int):
    connection, cursor = connect_to_database()
    cursor.execute("SELECT * FROM medicine WHERE name = '" + name + "'")
    medicine = cursor.fetchone()
    connection.close()
    current_items = medicine[1]
    current_items -= items_to_remove
    execute_sql(["UPDATE medicine SET items=" + str(current_items) + " WHERE name='" + name + "'"])


def get_all_medicine() -> list[str]:
    connection, cursor = connect_to_database()
    cursor.execute("SELECT name FROM medicine")
    medicines = cursor.fetchall()
    connection.close()
    return medicines
m = get_all_medicine()
print(m)

# take_medicine("nurofen", 10)
