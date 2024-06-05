# SPDX-FileCopyrightText: 2024-present yangxuenian <yangxn@cicvd.com>
#
# SPDX-License-Identifier: MIT
import os
import click
import pypandoc

from markdown2textile.__about__ import __version__


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version=__version__, prog_name="markdown2textile")
@click.option("-i", "--input", type=click.File("rb"), default="-", help="The input markdown file. Default is stdin.")
@click.option("-o", "--output", type=click.File("wb"), default="-", help="The output textile file. Default is stdout.")
def markdown2textile(input, output):
    def convert_markdown_to_textile(markdown):
        filter_path = os.path.join(os.path.dirname(__file__), "../pandoc_filter.py")
        return pypandoc.convert_text(markdown, "textile", format="md", filters=[filter_path])[:-1]

    input_data = input.read().decode("utf-8")
    output_data = convert_markdown_to_textile(input_data)
    output.write(output_data.encode("utf-8"))
    output.write(b"\n")
    output.flush()


if __name__ == "__main__":
    markdown2textile()
