from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="noscrape",  # Replace with your own package name
    version="1.0.3",  # Initial release version
    author="Bernhard Schönberger",
    author_email="noscrape@gmx.de",
    description="A package to obfuscate text using Unicode Private Use Area characters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/noscrape/noscrape-python",  # Replace with the URL of your project
    packages=find_packages(),  # Automatically find and include all packages in the project
    package_data={
        'noscrape': [
            'bin/noscrape_darwin_arm64',
            'bin/noscrape_darwin_x86_64',
            'bin/noscrape_linux_arm64',
            'bin/noscrape_linux_x86_64',
            'bin/noscrape_windows_x86_64.exe'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
