import sys
from model import util, data_manager

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def get_data():
    database = data_manager.read_table_from_file(DATAFILE)

    return database


def add(data_to_add):
    database = data_manager.read_table_from_file(DATAFILE)
    transaction_id = util.generate_id()
    data_to_add.insert(0, transaction_id)

    for data in database:
        if data[0] == transaction_id:
            return False

    if data_to_add not in database:
        database.append(data_to_add)

    data_manager.write_table_to_file(DATAFILE, database, separator=';')
    return True


def update(new_data_table):
    database = data_manager.read_table_from_file(DATAFILE)
    user_id = new_data_table[0]
    for i, data in enumerate(database):
        if data[0] == user_id:
            database[i] = new_data_table

    data_manager.write_table_to_file(DATAFILE, database, separator=';')


def is_contained(transaction_id):
    database = get_data()
    column_for_check = []
    for data in database:
        column_for_check.append(data[0])
    return transaction_id in column_for_check


def remove(transaction_id):
    database = get_data()
    for entry in database:
        if entry[0] == transaction_id:
            database.remove(entry)
            data_manager.write_table_to_file(DATAFILE, database, separator=';')
            return True
    return False


def look_for_biggest_revenue_product(database):
    products_and_prices_dict = {}

    for entry in database:

        if entry[2] in products_and_prices_dict.keys():
            products_and_prices_dict[entry[2]] += float(entry[3])
        else:
            products_and_prices_dict[entry[2]] = float(entry[3])
    id_price_set = products_and_prices_dict

    product = max(id_price_set, key=id_price_set.get)
    return product


def get_index_of_element(element, data_list, reverse=False):
    last_index_in_list = len(data_list) - 1

    if reverse:
        copied_list = data_list.copy()
        copied_list.reverse()

        index_of_element_in_revers = copied_list.index(element)
        index_of_element = last_index_in_list - index_of_element_in_revers
    else:
        index_of_element = data_list.index(element)

    return index_of_element


def get_pair_sorted_by_order(first_element, second_element, data_list):
    position_of_first_element = data_list.index(first_element)
    position_of_second_element = data_list.index(second_element)

    if position_of_first_element > position_of_second_element:
        first_element, second_element = second_element, first_element

    return first_element, second_element


def get_column_from_data(column_index, data=DATAFILE, type_data_in_column=str):
    data_list = []

    database = get_data()

    for row in database:
        needed_data = type_data_in_column(row[column_index])
        data_list.append(needed_data)

    return data_list


def count_transactions_beetween(first_index, second_index, data_list):
    sum_of_transactions = 0

    for i in range(first_index, second_index + 1):
        sum_of_transactions += data_list[i]

    return sum_of_transactions