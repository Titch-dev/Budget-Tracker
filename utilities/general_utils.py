def display_formatter(template: str, *dynamic_vars: str | int):
    """Function to dynamically enter variables to display strings

    Parameters:
        template: string to format with variables
        *dynamic_vars: strings and integers to format template

    Returns:
        Concatenated string
    """
    return template.format(*dynamic_vars)


def enumerate_object(objects: list[dict]) -> dict:
    """Function to enumerate a list of json dictionary

    Parameters:
        objects: List of object json dictionary

    Returns:
        Dictionary of enumerated keys and json values
    """
    enumerated_objects = dict()
    for idx, obj in enumerate(objects, 1):
        enumerated_objects[idx] = obj
    return enumerated_objects