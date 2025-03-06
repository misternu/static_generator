""" splitting and typing markdown blocks """
from enum import Enum
import re

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
