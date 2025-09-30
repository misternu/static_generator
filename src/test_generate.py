""" test generate """
import unittest

from generate import extract_title, generate_page

class TestGenerate(unittest.TestCase):
    """ test generation functions """

    def test_extract_title(self):
        """ test extract_title """
        markdown = """# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien"""
        title = extract_title(markdown)
        self.assertEqual('Tolkien Fan Club', title)

    def test_extract_title_exception(self):
        """ test extract_title exception """
        markdown = """Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien"""
        with self.assertRaises(ValueError):
            extract_title(markdown)
