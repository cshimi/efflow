import pandas as pd
import re

csv_file_path = 'csv_viewer_project/sourcedata/export_transactions_20231004.csv'


def detect_delimiter(file_path, num_lines=5):
    """
    Detect the delimiter used in a CSV file.

    Args:
        file_path (str): The path to the CSV file.
        num_lines (int): The number of lines to inspect for delimiter detection.

    Returns:
        str: The detected delimiter character.
    """
    possible_delimiters = [',', ';', '\t', '|']
    delimiter_counts = {}

    with open(file_path, 'r') as file:
        # Read the first few lines
        first_lines = [next(file) for _ in range(num_lines)]

    for delimiter in possible_delimiters:
        counts = [line.count(delimiter) for line in first_lines]
        total_count = sum(counts)
        delimiter_counts[delimiter] = total_count

    most_common_delimiter = max(delimiter_counts, key=delimiter_counts.get)

    return most_common_delimiter


# Define a function to extract information from the file and return it as a list
def extract_summaryInfo_from_file(file_path):
    extracted_info = {}  # Initialize an empty dictionary to store the extracted information

    with open(file_path, 'r') as file:
        file_content = file.read()

        # Use regular expressions to search for patterns
        date_from_match = re.search(r'Date from:;="([^"]+)"', file_content)
        date_to_match = re.search(r'Date to:;="([^"]+)"', file_content)
        entry_type_match = re.search(r'Entry type:;="([^"]+)"', file_content)
        account_match = re.search(r'Account:;="([^"]+)"', file_content)
        currency_match = re.search(r'Currency:;="([^"]+)"', file_content)

        # print(file_content)

        # Extract and add the matched information to the dictionary
        if date_from_match:
            extracted_info['Date from'] = date_from_match.group(1)
        if date_to_match:
            extracted_info['Date to'] = date_to_match.group(1)
        if entry_type_match:
            extracted_info['Entry type'] = entry_type_match.group(1)
        if account_match:
            extracted_info['Account'] = account_match.group(1)
        if currency_match:
            extracted_info['Currency'] = currency_match.group(1)

    return extracted_info


def extract_header_and_table(file_path):
    try:
        # Read the CSV file starting from line 6
        df = pd.read_csv(file_path, sep=';', skiprows=6, encoding='utf-8')

        # Extract the header and table
        header = df.columns.tolist()
        table = df.values.tolist()

        return header, table

    except Exception as e:
        return None, None  # Return None if there's an error


def print_summary_info(file_path):
    # Detect the delimiter
    detected_delimiter = detect_delimiter(file_path)
    print(f"The detected delimiter is '{detected_delimiter}'")

    # Extract and print the summary information
    info_dict = extract_summaryInfo_from_file(file_path)
    print("Summary Information:")
    for key, value in info_dict.items():
        print(f"{key}: {value}")

    # Extract and print the header and table
    header, table = extract_header_and_table(file_path)
    if header is not None and table is not None:
        print("\nHeader:")
        print(header)

        print("\nTable:")
        for row in table:
            print(row)
    else:
        print("\nError: Unable to extract header and table.")


# Call the print_summary_info function with your CSV file path
file_path = csv_file_path
print_summary_info(file_path)