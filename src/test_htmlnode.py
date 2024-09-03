""" test html node """
import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    """ tests for HTMLNode class """

    def test_repr(self):
        """ does the class repr """
        node = HTMLNode('p', 'value', [], { 'foo': 'bar', 'baz': 'boop' })
        self.assertEqual(repr(node), "HTMLNode(p, value, [], {'foo': 'bar', 'baz': 'boop'})")

    def test_prop_string(self):
        """ can you make a html prop string """
        node = HTMLNode('p', 'value', [], { 'foo': 'bar', 'baz': 'boop' })
        self.assertEqual(node.props_to_html(), ' foo="bar" baz="boop"')

    def test_empty_props(self):
        """ empty props should return empty string """
        node = node = HTMLNode('p', 'value', [], {})
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()
