from markdown2textile.pandoc_filter import convert_markdown_to_textile

def test_convert_markdown_to_textile():
    markdown = "**bold text**"
    expected_textile = "*bold text*"
    assert convert_markdown_to_textile(markdown) == expected_textile

def test_convert_markdown_to_textile_empty_input():
    markdown = """\
# My Text

This is a pen.
My name is Pen.

[Link to panflute](http://scorreia.com/software/panflute/index.html)

https://elixir-lang.org

## Your Text

Run the bellow code with `--option`:

```python
print("Hello, world")
```

---

> 2019/06/23

> 2019/06/23
> 2019-06-23

> 2019/06/23
>
> 2019-06-23

* **Bold** and __Bold__
- *Italic* and _Italic_
"""
    expected_textile = """\
h1(#my-text). My Text

This is a pen.
My name is Pen.

"Link to panflute":http://scorreia.com/software/panflute/index.html

https://elixir-lang.org

h2(#your-text). Your Text

Run the bellow code with @--option@:

<pre><code class="python">
print("Hello, world")
</code></pre>

---

> 2019/06/23

> 2019/06/23
> 2019&#45;06&#45;23

> 2019/06/23
>
> 2019&#45;06&#45;23

* *Bold* and *Bold*
* _Italic_ and _Italic_
"""
    assert convert_markdown_to_textile(markdown) == expected_textile