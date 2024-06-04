"""
This module provides tools for counting the occurrences of words
or patterns in a text file.

It offers several functionalities:

* Counting the occurrences of words from a provided file containing words
  (using the `--words-input-file` option).
* Counting occurrences of a specific word
  (using the `--single-word` option).
* Counting occurrences of a regular expression pattern
  (using the `--pattern` option).

**Features:**

* Handles both single words and word lists.
* Supports regular expressions for pattern matching.
* Provides informative error messages and usage instructions.
* Efficiently iterates through the file, considering only non-blank lines.

**Usage:**

```bash
python word_counter.py [--words-input-file FILE] [--single-word WORD] \
                        [--pattern PATTERN] searched_file
"""

from typing import Iterator, List, Set

import sys
import time
import re
import click


@click.command()
@click.option(
    "--words-input-file",
    "-i",
    type=click.File("r", lazy=True),
    help="File containing words to search for",
)
@click.option(
    "--searched-file",
    "-s",
    type=click.Path(exists=True),
    required=True,
    help="Text file to search in",
)
@click.option(
    "--single-word",
    "-w",
    type=click.STRING,
    help="Specific word to count (exclusive to --words-input-file)",
)
@click.option("--pattern", "-p", help="Regular expression pattern to match")
def calculate_words(
    words_input_file: click.File,
    searched_file: str,
    single_word: str,
    pattern: str,
) -> None:
    """
    Count the occurrence of words in a text file.

    Args:
        words_input_file (file, optional): File containing words to search for.
                                           Defaults to None.
        searched_file (str): Path to the text file to search in. Required.
        single_word (str, optional): Specific word to count. Defaults to None.
        pattern (str, optional): Regular expression pattern to match.
                                 Defaults to None.

    Note:
        --words-input-file and --single-word are mutually exclusive.
        At least one of --words-input-file, --single-word,
        or --pattern must be provided.
    """

    op1 = "--words-input-file"
    op2 = "--single-word"
    op3 = "--pattern"

    if words_input_file and single_word:

        click.echo(
            f"Error: {op1} and {op2} are mutually exclusive.",
            err=True,
        )
        sys.exit(1)

    if not (words_input_file or single_word or pattern):
        click.echo(
            f"Error: At least one of {op1}, {op2}, or {op3} must be provided.",
            err=True,
        )
        sys.exit(1)

    start_time = time.time()

    if words_input_file:
        # Process list of words
        with open(words_input_file.name, "r", encoding="utf8") as file:
            word_list = [elt.strip() for elt in file.readlines()]
            words = set(word_list)
            counter = count_multiple_words_in_file(words, searched_file)
            file1 = words_input_file.name
            file2 = searched_file
        print(f"Found {counter} matching words from '{file1}' in '{file2}'.")

    elif single_word:
        # Count specific word
        counter = count_word_in_file(single_word, searched_file)
        print(f"Found '{single_word}' {counter} times in '{searched_file}'.")

    else:
        # Match regular expression pattern
        c = count_pattern_in_file(pattern, searched_file)
        with open(searched_file, "r", encoding="utf8") as f:
            print(f"Found {c} matches for pattern '{pattern}' in '{f.name}'.")

    stop_time = time.time()
    elapsed_time = stop_time - start_time
    print(f"Time elapsed: {elapsed_time:.1f} seconds")


def count_multiple_words_in_file(words: Set[str], searched_file: str) -> int:
    """
    Count the occurrences of words from a given word set in a text file.

    Args:
        words (set): A set containing the words to search for.
        searched_file (str): The path to the text file to search in.

    Returns:
        int: The total count of occurrences of words
             from the word set in the text file.

    Note:
        This function reads the content of the text file specified
        by 'searched_file' and counts the occurrences of words
        from 'words' in each non-blank line of the file.
        It utilizes the 'non_blank_lines' generator to yield non-blank lines
        from the file.
        The function returns the total count of occurrences of words
        from 'words' in the file.
    """

    counter = 0
    with open(searched_file, "r", encoding="utf8") as file:
        for line in non_blank_lines(file):
            for word in line:
                if word in words:
                    counter += 1
    return counter


def count_word_in_file(word: str, searched_file: str) -> int:
    """Count how many times a word appears in a file.

    Args:
        word (str): The word to search for.
        searched_file (str): The path to the file to search in.

    Returns:
        int: The count of occurrences of the word in the file.
    """
    try:
        count = 0
        # Open the file in read mode
        with open(searched_file, "r", encoding="utf8") as file:
            # Read the file line by line
            for line in file:
                # Count occurrences of the word in the line
                count += line.count(word)

        # Print the count of occurrences
        return count

    except FileNotFoundError:
        # If the file is not found,
        # print an error message and return a non-zero exit code
        click.echo(f"Error: Path '{searched_file}' does not exist.", err=True)
        raise


def count_pattern_in_file(pattern: str, searched_file: str) -> int:
    """Counts occurrences of a pattern in a file, considering non-blank lines.

    Args:
        pattern (str): The pattern to search for.
        searched_file (str): The path to the file to search.

    Returns:
        int: The number of occurrences of the pattern in the file.
    """
    sanitized_pattern = sanitize_pattern(pattern)
    counter = 0
    with open(searched_file, "r", encoding="utf8") as file:
        # Iterate through each line in the file
        for line in file:
            # Count occurrences of the pattern in the line
            counter += sum(1 for _ in re.finditer(sanitized_pattern, line))
    return counter


def non_blank_lines(text_file: Iterator[str]) -> Iterator[List[str]]:
    """Generate non-blank lines from a text file.

    - erased blank lines from begin and end of string
    - it also remove all non alphanumerical characters
    - exclude space character

    Input: any string text from opened file

    Args:
        text_file (file): The input text file.

    Yields:
        list: Non-blank lines of the text file.
        example : ['word','','word']
    """
    for line in text_file:
        line = line.strip()
        if line:
            text = re.split(r"\s+", line)
            stripped_line = []
            for item in text:
                stripped = "".join(ch for ch in item if ch.isalnum())
                stripped_line.append(stripped)
            yield stripped_line


def sanitize_pattern(pattern: str) -> str:
    """
    Sanitizes a pattern string to prevent potential security vulnerabilities
    in regular expressions, specifically injection attacks like SQL injection.

    Args:
        pattern (str): The pattern to sanitize.

    Returns:
        str: The sanitized pattern.
    """

    if not isinstance(pattern, str):
        raise TypeError("Input must be a string")

    # Escape metacharacters like `.` (`\.`), `^` (`\^`), `$` (`\$`), etc.
    escaped_pattern = re.escape(pattern)

    # Additional sanitization (optional):
    # - Remove control characters (e.g., \n, \t, \r)
    # - Limit allowed characters based on context (e.g., alphanumeric only)
    # - Consider context-specific whitelisting
    #   or blacklisting for sensitive filters

    return escaped_pattern
