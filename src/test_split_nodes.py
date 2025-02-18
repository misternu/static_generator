""" test split_nodes_delimiter """

import unittest
from split_nodes import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes
)
from textnode import (
    TextNode,
    node_types
)

TEXT_1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) " \
         "and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
TEXT_2 = "This is text with a link [to boot dev](https://www.boot.dev) and " \
         "[to youtube](https://www.youtube.com/@bootdotdev)"
TEXT_3 = "This is **text** with an *italic* word and a `code block` and an " \
         "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

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

    def test_extract_markdown_images(self):
        """ test extract markdown images on string with images """
        result = extract_markdown_images(TEXT_1)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            result,
        )

    def test_extract_markdown_images_na(self):
        """ test extract markdow images on string without images """
        result = extract_markdown_images(TEXT_2)
        self.assertListEqual([], result)

    def test_extract_markdown_links(self):
        """ test extract markdown images on string with links """
        result = extract_markdown_links(TEXT_2)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev")
            ],
            result,
        )

    def test_extract_markdown_links_na(self):
        """ test extract markdow images on string without links """
        result = extract_markdown_links(TEXT_1)
        self.assertListEqual([], result)

    def test_split_nodes_image(self):
        """ test split a plain text with images """
        node = TextNode(TEXT_1, node_types.TEXT)
        result = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", node_types.TEXT),
                TextNode("rick roll", node_types.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", node_types.TEXT),
                TextNode("obi wan", node_types.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            result,
        )

    def test_split_nodes_link(self):
        """ test split a plain text with links """
        node = TextNode(TEXT_2, node_types.TEXT)
        result = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", node_types.TEXT),
                TextNode("to boot dev", node_types.LINK, "https://www.boot.dev"),
                TextNode(" and ", node_types.TEXT),
                TextNode("to youtube", node_types.LINK, "https://www.youtube.com/@bootdotdev")
            ],
            result,
        )

    def test_text_to_textnodes(self):
        """ test function that outputs complex result from text """
        result = text_to_textnodes(TEXT_3)
        self.assertEqual(
            [
                TextNode("This is ", node_types.TEXT),
                TextNode("text", node_types.BOLD),
                TextNode(" with an ", node_types.TEXT),
                TextNode("italic", node_types.ITALIC),
                TextNode(" word and a ", node_types.TEXT),
                TextNode("code block", node_types.CODE),
                TextNode(" and an ", node_types.TEXT),
                TextNode("obi wan image", node_types.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", node_types.TEXT),
                TextNode("link", node_types.LINK, "https://boot.dev"),
            ],
            result,
        )


if __name__ == "__main__":
    unittest.main()
