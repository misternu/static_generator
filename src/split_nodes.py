""" split delimiter """
import re
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

def split_nodes_link(nodes):
    """ return a new list of nodes with the links extracted """
    result = []
    for node in nodes:
        if node.text_type != 'text':
            result.append(node)
            continue
        result.extend(split_node_link(node))
    return result

def split_node_link(node):
    """ return a list of nodes separating text and links """
    split_text = re.split(r"(?<!!)\[[^\]]*\]\([^\)]*\)", node.text)
    link_tuples = extract_markdown_links(node.text)
    result = []
    for i in range(len(split_text)-1):
        result.append(TextNode(split_text[i], 'text'))
        result.append(TextNode(link_tuples[i][0], 'link', link_tuples[i][1]))
    if split_text[-1] != '':
        result.append(TextNode(split_text[-1], 'text'))
    return result

def split_nodes_image(nodes):
    """ return a new list of nodes with the images extracted """
    result = []
    for node in nodes:
        if node.text_type != 'text':
            result.append(node)
            continue
        result.extend(split_node_image(node))
    return result

def split_node_image(node):
    """ return a list of nodes separating text and images """
    split_text = re.split(r"!\[[^\]]*\]\([^\)]*\)", node.text)
    image_tuples = extract_markdown_images(node.text)
    result = []
    for i in range(len(split_text)-1):
        result.append(TextNode(split_text[i], 'text'))
        result.append(TextNode(image_tuples[i][0], 'image', image_tuples[i][1]))
    if split_text[-1] != '':
        result.append(TextNode(split_text[-1], 'text'))
    return result

def extract_markdown_images(text):
    """ return list of tuples of images """
    regex = r"!\[([^\]]*)\]\(([^\)]*)\)"
    return re.findall(regex, text)

def extract_markdown_links(text):
    """ return list of tuples of links """
    regex = r"(?<!!)\[([^\]]*)\]\(([^\)]*)\)"
    return re.findall(regex, text)

def text_to_textnodes(text):
    """ return textnodes for raw markdown string """
    result = [TextNode(text, 'text')]
    result = split_nodes_delimiter(result, "**", 'bold')
    result = split_nodes_delimiter(result, "*", 'italic')
    result = split_nodes_delimiter(result, "`", 'code')
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result
