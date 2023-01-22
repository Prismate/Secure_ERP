from model import util, data_manager


DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def get_data():
    database = data_manager.read_table_from_file(DATAFILE)
    return database


def add(data_to_add):
    database = data_manager.read_table_from_file(DATAFILE)
    user_id = util.generate_id()
    data_to_add.insert(0, user_id)

    for data in database:
        if data[0] == user_id:
            return False

    if data_to_add not in database:
        database.append(data_to_add)

    data_manager.write_table_to_file(DATAFILE, database, separator=';')


def update(new_data_table):
    database = data_manager.read_table_from_file(DATAFILE)
    user_id = new_data_table[0]
    for i, data in enumerate(database):
        if data[0] == user_id:
            database[i] = new_data_table

    data_manager.write_table_to_file(DATAFILE, database, separator=';')


def remove(user_id):
    data = data_manager.read_table_from_file(DATAFILE)
    for entry in data:
        if entry[0] == user_id:
            data.remove(entry)
            data_manager.write_table_to_file(DATAFILE, data, separator=';')
            return True
    return False


def is_contained(user_id):
    database = get_data()
    column_for_check = []
    for data in database:
        column_for_check.append(data[0])
    return user_id in column_for_check