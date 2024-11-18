def display_formatter(template: str, *dynamic_vars: str | int | float):
    """Function to dynamically enter variables to display strings

    Parameters:
        template: string to format with variables
        *dynamic_vars: strings and integers to format template

    Returns:
        Concatenated string
    """
    return template.format(*dynamic_vars)


def enumerate_object(objects: list[object]) -> dict:
    """Function to enumerate a list of objects

    Parameters:
        objects: List of objects

    Returns:
        Dictionary of enumerated (keys) objects (values)
    """
    enumerated_objects = dict()
    for idx, obj in enumerate(objects, 1):
        enumerated_objects[idx] = obj
    return enumerated_objects