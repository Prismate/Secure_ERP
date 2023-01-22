from model.crm import crm
from view import terminal as view


def list_customers():
    database = crm.get_data()

    if database != []:
        view.print_table(database, crm.HEADERS)
    else:
        view.print_error_message("Database is empty!!!\n")


def add_customer():
    customer_data = view.get_inputs(
        ["Enter customer name: ", "Enter customer email: ", "Enter customer subscription status (1 or 0): "])

    if crm.add(customer_data):
        view.print_message(f"User's data has been created")
    else:
        view.print_error_message(f"User's data has not been created")


def update_customer():
    customer_id = view.get_input('Please enter the customer ID')

    if crm.check_customer(customer_id):
        customer_data = view.get_inputs(
            ["Enter customer name: ", "Enter customer email: ", "Enter customer subscription status (1 or 0): "])
        customer_data.insert(0, customer_id)
        crm.update(customer_data)
        view.print_message('Database has been updated')
    else:
        view.print_message('Customer doesn\'t exist')


def delete_customer():
    customer_id = view.get_input("Please provide valid user id: ")
    if crm.remove(customer_id):
        view.print_error_message(f'User id {customer_id} removed.')
    else:
        view.print_error_message(f'User id {customer_id} not found, no records removed.')


def get_subscribed_emails():
    data = crm.select_subscribed_emails()
    headers = ['Subscribed emails']
    view.print_table(data, headers)


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError()


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            print("")
            run_operation(int(operation))
        except KeyError:
            view.print_error_message("There is no such option!")