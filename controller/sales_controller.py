import sys
import operator
from model.sales import sales
from view import terminal as view


def list_transactions():
    database = sales.get_data()
    if database != []:
        view.print_table(database, sales.HEADERS)
    else:
        view.print_error_message("Database is empty!!!\n")


def add_transaction():
    user_data = view.get_inputs(["Customer ID:\t", "Product:\t", "Price:\t", "Transaction date:\t"])
    if sales.add(user_data):
        view.print_message(f"New data has been added.\n")
    else:
        view.print_error_message(f"Transaction's data has not been created!!!\n")


def update_transaction():
    transaction_id = view.get_input("Please enter transaction ID:\t")
    if sales.is_contained(transaction_id):
        user_data = view.get_inputs(["Customer ID:\t", "Product:\t", "Price:\t", "Transaction date:\t"])

        user_data.insert(0, transaction_id)
        sales.update(user_data)
        view.print_message(f"Record with transaction ID {transaction_id} has been update.\n")
    else:
        view.print_error_message(f"Transaction ID {transaction_id} not found!!!\n")


def delete_transaction():
    transaction_id = view.get_input("Please enter transaction ID:\t")

    if sales.remove(transaction_id):
        view.print_message(f"Record with transaction ID {transaction_id} has been removed.\n")
    else:
        view.print_error_message(f"Transaction ID {transaction_id} not found!!!\n")


def get_biggest_revenue_transaction():
    database = sales.get_data()
    id_price_set = {line[0]: float(line[3]) for line in database}
    id_transaction = max(id_price_set, key=id_price_set.get)

    if database != []:
        view.print_general_results(id_transaction, 'ID transactions: ')
    else:
        view.print_error_message("Database is empty!!!\n")


def get_biggest_revenue_product():
    database = sales.get_data()

    if database != []:
        result = sales.look_for_biggest_revenue_product(database)
        view.print_general_results(result, "Product with biggest revenue is: ")
    else:
        view.print_error_message("Database is empty!!!\n")


def count_transactions_between():
    first_date = view.get_input("Please, give first date")
    second_date = view.get_input("Please, give second date")

    dates_list = sales.get_column_from_data(column_index=-1)

    first_date, second_date = sales.get_pair_sorted_by_order(first_date, second_date, dates_list)

    start_counting_position = sales.get_index_of_element(first_date, dates_list)
    end_counting_position = sales.get_index_of_element(second_date, dates_list, reverse=True)

    amount_of_transactions = end_counting_position - start_counting_position + 1

    view.print_general_results(amount_of_transactions, "The amount of transactions between selected dates is: ")


def sum_transactions_between():
    first_date = view.get_input("Please, give first date")
    second_date = view.get_input("Please, give second date")

    dates_list = sales.get_column_from_data(column_index=-1)

    first_date, second_date = sales.get_pair_sorted_by_order(first_date, second_date, dates_list)

    start_counting_position = sales.get_index_of_element(first_date, dates_list)
    end_counting_position = sales.get_index_of_element(second_date, dates_list, reverse=True)

    transactions_list = sales.get_column_from_data(column_index=-2, type_data_in_column=float)
    sum_of_transactions = sales.count_transactions_beetween(start_counting_position, end_counting_position,
                                                            transactions_list)

    view.print_general_results(sum_of_transactions, "The sum of transactions between selected dates is: ")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            print("")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)