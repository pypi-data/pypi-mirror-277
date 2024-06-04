from typing import Dict, List
import copy

def extract_inner_tables(data: Dict) -> List[Dict]:
    """
    Recursively extracts inner tables from a dictionary structure and returns them as a list of tables.

    Args:
        data (dict): The dictionary containing the table data, potentially with nested inner tables.

    Returns:
        list of dict: A list containing all extracted inner tables as dictionaries.
    """
    inner_table_list = []  # List to hold all found inner tables
    
    
    # Helper function to recursively search for inner tables
    def recurse_find_inner_tables(current_data):
        if 'rows' in current_data:
            for row in current_data['rows']:
                for column_value in row.values():
                    if 'inner_tables' in column_value:
                        for inner_table in column_value['inner_tables']:
                            for table in inner_table:
                                inner_table_list.append(table)
                                recurse_find_inner_tables(table)  # Recursively check for more inner tables within
                        # Once inner tables are collected, clear them to avoid duplication if later processed
                        column_value['inner_tables'] = []

    # Start the recursive search from the initial data
    recurse_find_inner_tables(data)
    
    return inner_table_list

def table_dict_to_plain_text(table_data:Dict) -> str:
    """
    Converts a nested dictionary (representing rows and columns of a table) into plain text.
    
    Args:
        data (dict): The dictionary containing the table data.
    
    Returns:
        str: A plain text string representing the content of the table.
    """
    plain_text = ''
    # Process each row in the 'rows' list
    for row in table_data.get('rows', []):
        for column_key, column_value in row.items():
            # Append the 'value' from each column to the plain text string
            plain_text += column_value.get('value', '') + '\n'
            
            # Check if there are inner tables and process them recursively
            if 'inner_tables' in column_value:
                for inner_table in column_value['inner_tables']:
                    # Since inner_tables can be lists of tables, iterate through each
                    for table in inner_table:
                        # Recursively convert inner table dictionary to plain text
                        plain_text += table_dict_to_plain_text(table)
    
    return plain_text


def table_dict_to_html_table(data: Dict) -> str:
    """
    Converts a dictionary representing table data with possible nested tables into an HTML table.

    Args:
        data (dict): The dictionary containing the table data.

    Returns:
        str: HTML string representing the table.
    """
    html = '<table border="1">\n'  # Start the table; you can customize style as needed
    
    # Process each row in the 'rows' list
    for row in data.get('rows', []):
        html += '  <tr>\n'  # Start a new row
        for column_key, column_value in row.items():
            # Get the text value, rowspan, and colspan for the current cell
            value = column_value.get('value', '')
            row_span = column_value.get('row_span', 0)
            col_span = column_value.get('col_span', 0)

            # Create the table cell with rowspan and colspan attributes if they are greater than 0
            html += f'    <td{" rowspan=" + str(row_span) if row_span > 0 else ""}{" colspan=" + str(col_span) if col_span > 0 else ""}>{value}\n'
            
            # Check for inner tables and process them recursively
            if 'inner_tables' in column_value:
                for inner_table in column_value['inner_tables']:
                    for table in inner_table:
                        # Recursively convert inner table dictionary to HTML table
                        html += table_dict_to_html_table(table)
        
        html += '  </td></tr>\n'  # End the current row
    html += '</table>\n'  # End the table

    return html


def remove_inner_tables(data: Dict) -> Dict:
    """
    Removes all inner tables from a dictionary representing a table, preserving only the main table structure.

    Args:
        data (dict): The original dictionary containing the table data with potential inner tables.

    Returns:
        dict: A new dictionary that represents the main table without any inner tables.
    """
    # Create a deep copy of the data to avoid modifying the original data
    main_table = copy.deepcopy(data)
    
    # Recursive function to traverse the dictionary and remove 'inner_tables' keys
    def strip_inner_tables(current_data):
        if 'rows' in current_data:
            for row in current_data['rows']:
                for column_key, column_value in row.items():
                    # Check if 'inner_tables' key exists and remove it
                    if 'inner_tables' in column_value:
                        del column_value['inner_tables']

                    # Recursively check for deeper nested structures (not typically necessary with your structure but for completeness)
                    strip_inner_tables(column_value)

    # Apply the recursive removal function to the copied data
    strip_inner_tables(main_table)

    return main_table

