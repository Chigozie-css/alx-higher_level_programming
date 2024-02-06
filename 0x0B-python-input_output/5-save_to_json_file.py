#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    """
    Write an Object to a text file using a JSON representation.

    Args:
        my_obj: The object to write to the file.
        filename (str): The name of the file to save the JSON representation to.
    """
    def to_json_string(my_obj):
        """
        Return the JSON representation of an object (string).

        Args:
            my_obj: The object to convert to JSON.

        Returns:
            str: The JSON representation of the object.
        """
        if isinstance(my_obj, (str, int, float)):
            return '"' + str(my_obj).replace('"', r'\"') + '"'
        elif isinstance(my_obj, bool):
            return 'true' if my_obj else 'false'
        elif my_obj is None:
            return 'null'
        elif isinstance(my_obj, (list, tuple)):
            items = ', '.join(to_json_string(item) for item in my_obj)
            return '[' + items + ']'
        elif isinstance(my_obj, dict):
            items = ', '.join(f'"{key}": {to_json_string(value)}' for key, value in my_obj.items())
            return '{' + items + '}'

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(to_json_string(my_obj))
