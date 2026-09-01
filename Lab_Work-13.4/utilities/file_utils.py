def write_file(filename, content):
    """Writes content to a text file."""
    with open(filename, 'w') as file:
        file.write(content)
    return f"Successfully written to {filename}"

def read_file(filename):
    """Reads and returns the content of a text file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file {filename} does not exist."
