import os
import platform


def load_noscrape_lib():
    """
    Determines the appropriate binary file for the current operating system and architecture,
    checks if the file exists and is readable, and returns the path to the binary file.

    Returns:
        str: The path to the binary file.

    Raises:
        Exception: If the binary file for the current OS and architecture is not found or is not readable.
    """

    # Get the operating system name and convert it to lowercase
    os_name = platform.system().lower()

    # Get the machine architecture and convert it to lowercase
    arch = platform.machine().lower()

    # Construct the path to the binary file based on the current script's directory, OS name, and architecture
    filename = os.path.join(os.path.dirname(__file__), f"bin/noscrape_{os_name}_{arch}")

    # Append the '.exe' extension for Windows systems
    if os_name == "windows":
        filename += ".exe"

    # Check if the file exists and is readable
    if not os.path.isfile(filename) or not os.access(filename, os.R_OK):
        # Raise an exception if the file does not exist or is not readable
        raise Exception(f"os/arch not supported: %s" % filename)

    # Return the path to the binary file
    return filename
