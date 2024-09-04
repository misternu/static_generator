""" test HTMLNode """
import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_p_tag(self):
        """ can render a p tag """
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_a_tag(self):
        """ can render an a tag """
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_parent_node(self):
        """ can render nested nodes """
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        example = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), example)

    def test_to_html_with_grandchildren(self):
        """ can render with grandchildren """
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
