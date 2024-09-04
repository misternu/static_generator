""" test TextNode """
import unittest

from textnode import TextNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    """ test TextNode class """
    def test_eq(self):
        """ equal  arguments are equal """
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_uneq(self):
        """ unequal arguments are not equal """
        node = TextNode("This is a text node", "plain")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_equrl(self):
        """ url required for equality """
        node = TextNode("This is a text node", "bold")
        node_url = TextNode("This is a text node", "bold", "http://www.google.com")
        self.assertNotEqual(node, node_url)

    def test_repr(self):
        """ does it repr """
        node = TextNode("This is a text node", "bold")
        rep = "TextNode(This is a text node, bold, None)"
        self.assertEqual(repr(node), rep)

class TestTextNodeToHTMLNode(unittest.TestCase):
    """ tests for converting text nodes to html nodes """
    def test_text(self):
        """ plain text node """
        node = TextNode("This is a text node", 'text')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        """ image node """
        node = TextNode("This is an image", 'image', "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        """ bold node """
        node = TextNode("This is bold", 'bold')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()
