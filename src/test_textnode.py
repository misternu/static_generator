import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", "plain")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_equrl(self):
        node = TextNode("This is a text node", "bold")
        node_url = TextNode("This is a text node", "bold", "http://www.google.com")
        self.assertNotEqual(node, node_url)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        rep = "TextNode(This is a text node, bold, None)"
        self.assertEqual(node.__repr__(), rep)

if __name__ == "__main__":
    unittest.main()
