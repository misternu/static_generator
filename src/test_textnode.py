""" test textnode """
import unittest

from textnode import TextNode

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

if __name__ == "__main__":
    unittest.main()
