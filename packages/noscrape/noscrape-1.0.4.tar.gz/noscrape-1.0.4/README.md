# _noscrape_ Wrapper

## Overview
Welcome to the official documentation for _noscrape_! This wrapper simplifies the integration of _noscrape_ into your Python projects. _noscrape_ is a tool designed to prevent web scraping by obfuscating HTML elements using true-type fonts with shuffled unicodes.

## Concept
The primary mechanism behind _noscrape_ is the utilization of true-type fonts. _noscrape_ generates a new version with shuffled unicodes, making it impossible to reverse-calculate them. Additionally, glyph-paths inside the font are obfuscated by randomly shifting them slightly.

## Platform Implementation
_noscrape_ is implemented using platform-specific binaries optimized for different operating systems and architectures. These binaries include:

- `noscrape_darwin_arm64`
- `noscrape_darwin_x86_64`
- `noscrape_linux_arm64`
- `noscrape_linux_x86_64`
- `noscrape_windows_x86_64.exe`

These binaries serve as the core engine of _noscrape_, handling the generation of obfuscated text using true-type fonts with shuffled unicodes.

## Wrapper Implementations
Wrapper implementations provided in languages such as PHP, Java, and Node.js facilitate communication with the _noscrape_ binaries. They collect input data, call the appropriate _noscrape_ binary based on the host platform, pass the input data for obfuscation, and return the obfuscated text or other outputs.

## Installation
You can install the _noscrape_ wrapper using pip:

```bash
pip install noscrape
```

## Usage

```python

from noscrape import Noscrape

n = Noscrape("example/example.ttf")

text = n.obfuscate("test")

b64_font = n.render()
```

## Putting it together

