def write_to_console(text):
    """
    Function to output text to the console.

    Parameters:
        text (str): The text to be output to the console.
    """
    print(text)

def write_to_file(filename, content):
    """
    Function to write to a file using Python's built-in capabilities.

    Parameters:
        filename (str): The path to the file to write the content to.
        content (str): The content to be written to the file.
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print("Data successfully written to the file.")
    except Exception:
        print("An error occurred while writing to the file.")