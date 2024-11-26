def display_template(template: str, *dynamic_vars: str | int | float) -> str:
    """Parse a template string to format with dynamic variables

    Parameters:
        template (str): Template to format
        *dynamic_vars (int | float | str): multiple

    Returns:
        Concatenated string
    """
    return template.format(*dynamic_vars)


def amount_validator(prompt: str) -> float:
    """Prompt the user to input a positive float

    Parameters:
        prompt (str): Dynamic string to specify type of amount

    Returns:
        float: A valid positive float"""
    while True:
        try:
            amount = float(input(f'Enter {prompt} amount: R'))
            if amount < 0:
                print('Invalid amount. please enter a positive number.')
                continue
            return amount
        except ValueError:
            print('Invalid input. Please enter a numeric value.')


def date_formatter(full_date: bool) -> str:
    """Take user input and return a validated date string

    Parameters:
        full_date (bool): Either return a full date ('YYYY-MM-DD') or ('YYYY-MM')

    Returns:
        str: A validated and formatted date string.
    """
    def get_valid_input(prompt: str, min_val: int, max_val: int, length: int) -> str:
        """Helper function to get a valid numerical input within a range and length"""
        while True:
            try:
                value = input(prompt).strip()
                # Ensure input is correct length
                if len(value) != length:
                    print(f'Please enter {length}-digit number')
                    continue
                # Ensure value is a number and within range
                if not (min_val <= int(value) <= max_val):
                    print(f'Please enter a number between {min_val} and {max_val}')
                    continue
                return value
            except ValueError:
                print('Invalid input. Please enter a numeric value.')

    # Get a valid year and month
    year = get_valid_input('Enter year (YYYY): ', 1,9999,4)
    month = get_valid_input('Enter month (MM): ', 1, 12, 2)
    if not full_date:
        return f'{year}-{month}'
    else:
        # Get a valid day
        day = get_valid_input('Enter day (DD): ', 1, 31, 2)
        return f'{year}-{month}-{day}'


def pause_terminal(message="Press Enter to continue..."):
    """
    Halts the terminal display until the user presses Enter.

    Parameters:
        message (str): The message to display prompting the user to proceed.
    """
    input(message)
