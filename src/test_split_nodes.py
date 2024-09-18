""" test split_nodes_delimiter """

import unittest
from split_nodes import split_nodes_delimiter
from textnode import (
    TextNode,
    node_types
)

class TestInlineMarkdown(unittest.TestCase):
    """ test parsing of inline delimiters """
    def test_delim_bold(self):
        """ test inline bold """
        node = TextNode("This is text with a **bolded** word", node_types.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", node_types.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", node_types.TEXT),
                TextNode("bolded", node_types.BOLD),
                TextNode(" word", node_types.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        """ test inline bold used twice """
        node = TextNode(
            "This is text with a **bolded** word and **another**", node_types.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", node_types.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", node_types.TEXT),
                TextNode("bolded", node_types.BOLD),
                TextNode(" word and ", node_types.TEXT),
                TextNode("another", node_types.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        """ test multiple bold with delimiter at end of string """
        node = TextNode(
            "This is text with a **bolded word** and **another**", node_types.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", node_types.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", node_types.TEXT),
                TextNode("bolded word", node_types.BOLD),
                TextNode(" and ", node_types.TEXT),
                TextNode("another", node_types.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        """ test italics """
        node = TextNode("This is text with an *italic* word", node_types.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", node_types.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", node_types.TEXT),
                TextNode("italic", node_types.ITALIC),
                TextNode(" word", node_types.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        """ test bold and italic """
        node = TextNode("**bold** and *italic*", node_types.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", node_types.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", node_types.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", node_types.BOLD),
                TextNode(" and ", node_types.TEXT),
                TextNode("italic", node_types.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        """ test inline code block """
        node = TextNode("This is text with a `code block` word", node_types.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", node_types.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", node_types.TEXT),
                TextNode("code block", node_types.CODE),
                TextNode(" word", node_types.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
