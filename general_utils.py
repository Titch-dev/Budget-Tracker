def display_formatter(template: str, *dynamic_vars: str | int | float):
    """Function to dynamically enter variables to display strings

    Parameters:
        template: string to format with variables
        *dynamic_vars: strings and integers to format template

    Returns:
        Concatenated string
    """
    return template.format(*dynamic_vars)


def date_formatter(full_date: bool):

    year = input('Enter year (YYYY): ')
    month = input('Enter month (MM): ')
    if full_date:
        day = input(f'Enter day (DD): ')
        return f'{year}-{month}-{day}'
    else:
        return f'{year}-{month}'
