import json
import random
import subprocess

from load_noscrape_lib import load_noscrape_lib


class Noscrape:
    """
    A class to obfuscate text using a mapping of characters to Unicode Private Use Area (PUA) characters
    and render the obfuscated text using an external binary.
    """

    def __init__(self, font_path: str):
        """
        Initialize the Noscrape object with a font path.

        Parameters:
            font_path (str): The path to the font file to be used for rendering.
        """
        self.font_path = font_path
        self.mapping = {}
        self.pua_range = list(range(0xE000, 0xF8FF + 1))

    def obfuscate(self, s):
        """
        Obfuscate the input based on its type (string, integer, or list).

        Parameters:
            s (str, int, list): The input to be obfuscated.

        Returns:
            str or list: The obfuscated version of the input.

        Raises:
            TypeError: If the input is not a string, integer, or list.
        """
        if isinstance(s, str):
            return self.obfuscate_string(s)
        elif isinstance(s, int):
            return self.obfuscate_string(str(s))
        elif isinstance(s, list):
            return [self.obfuscate(item) for item in s]
        else:
            raise TypeError("Input must be a string, integer, or list")

    def obfuscate_string(self, s):
        """
        Obfuscate a string by mapping its characters to random PUA characters.

        Parameters:
            s (str): The string to be obfuscated.

        Returns:
            str: The obfuscated string.

        Raises:
            ValueError: If no available PUA characters are left for obfuscation.
        """
        # Available characters are those in the PUA range that haven't been mapped yet
        available_chars = list(set(self.pua_range) - set(self.mapping.values()))

        obfuscated = ''
        for c in s:
            # If the character hasn't been mapped yet, map it to a random available PUA character
            if c not in self.mapping:
                if not available_chars:
                    raise ValueError("No available PUA characters left to use for obfuscation")
                random_char = random.choice(available_chars)
                self.mapping[c] = random_char
                available_chars.remove(random_char)

            # Convert the PUA character code to a UTF-8 encoded character and append it to the result
            obfuscated += chr(self.mapping[c])

        return obfuscated

    def render(self):
        """
        Render the obfuscated text using the external binary.

        Returns:
            str: The output from the rendering binary.

        Raises:
            subprocess.CalledProcessError: If there is an error during the rendering process.
        """
        # Load the appropriate binary for the current system
        binary = load_noscrape_lib()

        # Prepare the parameters for the rendering library
        param = json.dumps({
            "font": self.font_path,
            "translation": self.mapping,
        })

        # Execute the rendering command and return the output
        try:
            result = subprocess.check_output([binary, param], text=True)
            return result
        except subprocess.CalledProcessError as e:
            print(f"Error during rendering: {e}")
            return None
