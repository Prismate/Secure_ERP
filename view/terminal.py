def print_menu(title, list_options):
    print(title)

    for i, option in enumerate(list_options):
        if i > 0:
            print(f'({i}) {option}')

    print(f'(0) {list_options[0]}')


def print_message(message):
    print(f"{message}\n")


def print_general_results(result, label):
    print(f"{label}\n {result}")

# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/


def get_list_of_column_width(table):
    columns_width = []

    number_of_rows = len(table)
    number_of_cols = len(table[0])

    for number_of_col in range(number_of_cols):
        temp_list = []
        for number_of_row in range(number_of_rows):
            column_width = len(table[number_of_row][number_of_col])
            column_width += 2
            temp_list.append(column_width)

        max_column_width = max(temp_list)

        columns_width.append(max_column_width)

    return columns_width


def calculate_table_width(list_of_width):
    inside_width = sum(list_of_width)
    number_of_cols = len(list_of_width)
    number_of_inside_partition = number_of_cols - 1

    table_width = inside_width + number_of_inside_partition

    return table_width


def get_prepared_row_for_print(some_list, list_with_column_width, prepared_row_is_not_partition_row=True):
    row_for_print = []

    for i in range(len(some_list)):
        column = some_list[i]
        column_width = list_with_column_width[i]

        row_for_print.append("|")

        if prepared_row_is_not_partition_row:
            centered_data = column.center(column_width)
            row_for_print.append(centered_data)
        else:
            row_for_print.append("-" * column_width)

    row_for_print.append("|")

    return row_for_print


def get_table_prepared_for_print(some_table, list_of_columns_width):
    table_prepared_for_print = []

    for i in range(len(some_table)):
        row_for_print = get_prepared_row_for_print(some_table[i], list_of_columns_width)
        delimiter_row = get_prepared_row_for_print(some_table[i], list_of_columns_width, False)

        table_prepared_for_print.append(row_for_print)
        table_prepared_for_print.append(delimiter_row)

    return table_prepared_for_print


def convert_list_to_string(some_list):
    converted_string = "".join(some_list)

    return converted_string


def print_table(table, title_list):
    table.insert(0, title_list)

    columns_width = get_list_of_column_width(table)
    table_width = calculate_table_width(columns_width)
    table_prepared_for_print = get_table_prepared_for_print(table, columns_width)

    print("/" + "-" * table_width + "\\")

    for i in range(len(table_prepared_for_print) - 1):
        row = table_prepared_for_print[i]
        string_for_print = convert_list_to_string(row)
        print(string_for_print)

    print("\\" + "-" * table_width + "/" + "\n")


def get_input(label):
    return input(f"{label}:\t")


def get_inputs(labels):
    labels_list = []

    for label in labels:
        labels_list.append(input(label))

    return labels_list


def print_error_message(message):
    print(f"{message}\n")