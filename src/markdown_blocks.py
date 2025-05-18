""" splitting and typing markdown blocks """
from enum import Enum
import re
from split_nodes import text_to_textnodes
from htmlnode import ParentNode
from textnode import (TextNode, text_node_to_html_node)

class BlockType(Enum):
    """ type enum for blocks """
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def markdown_to_blocks(markdown):
    """ takes a markdown formatted string and returns blocks of text """
    strings = markdown.split("\n\n")
    strings = list(map(str.strip, strings))
    strings = list(filter(lambda block: not len(block) == 0, strings))
    return strings

def block_to_block_type(block):
    """ identify type of block """
    if re.match(r'\A#{1,6} .*', block, re.DOTALL):
        return BlockType.HEADING
    if re.match(r'\A```.*```', block, re.DOTALL):
        return BlockType.CODE
    if re.match(r'(^>.*)+', block, re.DOTALL):
        return BlockType.QUOTE
    if re.match(r'(^- .*)+', block, re.DOTALL):
        return BlockType.UNORDERED_LIST
    if re.match(r'(^\d+\. .*)+', block, re.DOTALL):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    """ make a string into textnodes """
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_html_node(block))
    return ParentNode("div", children)

def block_to_html_node(block):
    match block_to_block_type(block):
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return olist_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return ulist_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case _:
            raise ValueError("invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    children = text_to_children(block.replace("\n", " "))
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    return ParentNode(f"h{level}", text_to_children(block[level+1:]))

def code_to_html_node(block):
    return ParentNode("pre",[
        ParentNode("code", [
            text_node_to_html_node(TextNode(block.strip(' `'), 'text'))
        ])
    ])

def olist_to_html_node(block):
    html_items = []
    for item in block.split("\n"):
        html_items.append(ParentNode("li", text_to_children(item.strip(' 123456789.'))))
    return ParentNode("ol", html_items)

def ulist_to_html_node(block):
    html_items = []
    for item in block.split("\n"):
        html_items.append(ParentNode("li", text_to_children(item.strip(' -'))))
    return ParentNode("ul", html_items)

def quote_to_html_node(block):
    new_lines = []
    for line in block.split("\n"):
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
