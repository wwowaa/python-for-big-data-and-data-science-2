def read_from_console():
    """
    Function to input text from the console.

    Returns:
        str: The text entered from the console.
    """
    text = input("Enter text: ")
    return text

def read_from_file(filename):
    """
    Function to read from a file using Python's built-in functions.

    Parameters:
        filename (str): The path to the file to be read.

    Returns:
        str or None: The content of the file or None if the file is not found.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found.")
        return None

def read_with_pandas(filename):
    """
    Function to read from a file using the pandas library.

    Parameters:
        filename (str): The path to the file to be read.

    Returns:
        DataFrame or None: The data from the file as a DataFrame or None if the file is not found.
    """
    try:
        import pandas as pd
        data = pd.read_csv(filename)
        return data
    except FileNotFoundError:
        print("File not found.")
        return None
