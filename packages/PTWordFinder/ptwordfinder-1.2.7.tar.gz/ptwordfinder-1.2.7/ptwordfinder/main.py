""" Entrypoint of the CLI """

import click
from ptwordfinder.commands.PTWordFinder import calculate_words


@click.group()
def cli():
    """
    The method cli is decorated with @click.group(),
    indicating it serves as the entry point
    for a Click-based command-line interface (CLI).
    """
    pass


cli.add_command(calculate_words)
