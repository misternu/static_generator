""" TextNode and helpers """
import types
from htmlnode import LeafNode

node_types = types.SimpleNamespace()
node_types.TEXT = "text"
node_types.BOLD = "bold"
node_types.ITALIC = "italic"
node_types.CODE = "code"
node_types.LINK = "link"
node_types.IMAGE = "image"

class TextNode:
    """ represents node of text """
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    """ convert text node to html node """
    match text_node.text_type:
        case node_types.TEXT:
            return LeafNode(None, text_node.text)
        case node_types.BOLD:
            return LeafNode('b', text_node.text)
        case node_types.ITALIC:
            return LeafNode('i', text_node.text)
        case node_types.CODE:
            return LeafNode('code', text_node.text)
        case node_types.LINK:
            return LeafNode('a', text_node.text, { 'href': text_node.url })
        case node_types.IMAGE:
            return LeafNode('img', '', { 'src': text_node.url, 'alt': text_node.text })
