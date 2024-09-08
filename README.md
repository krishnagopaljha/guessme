# GuessME

GuessME is a Python script for generating custom wordlists based on user profiles and configuration settings. It is useful for password cracking and security testing by creating wordlists with various combinations of personal information.

## Features

- **Interactive Mode**: Allows users to input personal details to create a customized wordlist.
- **Configuration File**: Supports configuration through a file (`guessme.cfg`) for settings like special characters, numeric ranges, and leet transformations.
- **Leet Speak Transformation**: Converts words into leet speak based on configurable mappings.
- **Special Characters and Numeric Variations**: Includes options for appending special characters and numbers.
- **Flexible Wordlist Generation**: Combines personal information in various ways to generate diverse password lists.
- **Output**: Saves the generated wordlist to a file.

## Tech Stack

- **Python 3**: The script is written in Python 3.x.
- **Libraries**:
  - `argparse` for command-line argument parsing.
  - `configparser` for reading configuration files.
  - `functools` for partial function application.
- **OS**: Utilizes OS functions for file handling and directory operations.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/krishnagopaljha/guessme.git
   cd guessme
   pip3 install -r requirements.txt
   ```
   
## Usage

1. Run in Interactive Mode:
   ``` bash
   python3 guessme.py -i
   ```
