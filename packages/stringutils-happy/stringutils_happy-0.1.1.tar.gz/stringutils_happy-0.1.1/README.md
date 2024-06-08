# stringutils_happy

stringutils_happy is a Python library for various string manipulation tasks.

## Features

- Convert strings to snake_case
- Convert strings to camelCase
- Remove special characters from strings
- Normalize whitespace in strings

## Installation

You can install the library using pip:

```bash
pip install stringutils_happy
ll stringutils
```

# Usage

Here are some examples of how to use the library:

```python
from stringutils import to_snake_case, to_camel_case, remove_special_characters, normalize_whitespace

# Convert to snake_case
print(to_snake_case('CamelCaseString'))  # Output: camel_case_string

# Convert to camelCase
print(to_camel_case('snake_case_string'))  # Output: snakeCaseString

# Remove special characters
print(remove_special_characters('Hello, World!'))  # Output: Hello World

# Normalize whitespace
print(normalize_whitespace('Hello   World'))  # Output: Hello World
```

# Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

# License

This project is licensed under the MIT License.
