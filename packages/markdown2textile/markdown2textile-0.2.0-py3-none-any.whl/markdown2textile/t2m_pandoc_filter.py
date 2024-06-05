#!/usr/bin/env python3

import os
from panflute import BlockQuote, CodeBlock, HorizontalRule, Inline, LineBreak, Para, RawBlock, RawInline, SoftBreak, Space, Str, run_filters

import re

re_uri = re.compile(r"\w+://")

def code_block(elem, _doc):
    if isinstance(elem, CodeBlock):
        match = re.search(r'<code class="([^"]*)">', elem.text)
        if match:
            language = match.group(1)
            code = re.sub(r'<\/?code[^>]*>\n?', '', elem.text)
            return CodeBlock(code, classes=[language])


def stripped_quote(elem, _doc):
    if isinstance(elem, Para) :
        child_elems = []
        def append(child, _doc):
            nonlocal child_elems
            if child == Str(">") or child == Space():
                return
            if isinstance(child, Inline):
                child_elems.append(child)

        elem.walk(append)
        return BlockQuote(Para(*child_elems))


if __name__ == "__main__":
    run_filters(
        [
            code_block,
            stripped_quote,
        ]
    )
