""" test the splitting and typing of markdown blocks """
import unittest
from markdown_blocks import markdown_to_blocks

class TestMarkdownToHTML(unittest.TestCase):
    """ tests for transforming markdown to blocks to nodes to html """
    def test_markdown_to_blocks(self):
        """ test the splitting of markdown blocks """
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\n" \
                "This is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

if __name__ == "__main__":
    unittest.main()
