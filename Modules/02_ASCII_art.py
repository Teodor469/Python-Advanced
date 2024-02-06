from pyfiglet import figlet_format


def create_ascii_art(text, font="standard"):
    """
    Create ASCII art from the given text using pyfiglet.

    Parameters:
    - text (str): The text to be converted to ASCII art.
    - font (str): The font style to be used (default is "standard").

    Returns:
    - str: The ASCII art representation of the input text.
    """
    ascii_art = figlet_format(text, font=font)
    return ascii_art


text_to_convert = "Hello, ASCII Art!"
ascii_art_result = create_ascii_art(text_to_convert)
print(ascii_art_result)
