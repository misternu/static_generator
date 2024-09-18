""" split delimiter """
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """ return a new list of nodes with delimeted using text_type """
    result = []
    for old_node in old_nodes:
        if old_node.text_type != 'text':
            result.append(old_node)
            continue
        result.extend(split_node_delimiter(old_node, delimiter, text_type))
    return result

def split_node_delimiter(old_node, delimiter, text_type):
    """ return a new list of nodes with delimited using text_type """
    split_text = old_node.text.split(delimiter)
    if len(split_text) % 2 == 0:
        raise ValueError("Invalid Markdown syntax")
    result = []
    for i, text in enumerate(split_text):
        if text == "":
            continue
        if i % 2 == 0:
            result.append(TextNode(text, 'text'))
        else:
            result.append(TextNode(text, text_type))
    return result
