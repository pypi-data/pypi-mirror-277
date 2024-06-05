# SPDX-FileCopyrightText: 2024-present yangxuenian <yangxn@cicvd.com>
#
# SPDX-License-Identifier: MIT
import os
import click
import pypandoc

from markdown2textile.__about__ import __version__

def convert_markdown_to_textile(markdown):
    filter_path = os.path.join(os.path.dirname(__file__), "../m2t_pandoc_filter.py")
    return pypandoc.convert_text(markdown, "textile", format="md", filters=[filter_path])[:-1]
def convert_textile_to_markdown(textile):
    filter_path = os.path.join(os.path.dirname(__file__), "../t2m_pandoc_filter.py")
    return pypandoc.convert_text(textile, "markdown", format="textile", filters=[filter_path])[:-1]


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version=__version__, prog_name="markdown2textile")
@click.option("-i", "--input", type=click.File("rb"), default="-", help="The input file. Default is stdin.")
@click.option("-o", "--output", type=click.File("wb"), default="-", help="The output file. Default is stdout.")
def mt_converter(input, output):
    is_m2t= True
    if not input.name.endswith(".md") and not input.name.endswith(".markdown"):
        is_m2t = False

    print("Now converting markdown to textile..." if is_m2t else "Now converting textile to markdown...")
    input_data = input.read().decode("utf-8")
    output_data = convert_markdown_to_textile(input_data) if is_m2t else convert_textile_to_markdown(input_data)
    output.write(output_data.encode("utf-8"))
    output.write(b"\n")
    output.flush()


if __name__ == "__main__":
    mt_converter()
