""" extract markdown """
import re

def extract_markdown_images(text):
    """ return list of tuples of images """
    regex = r"!\[([^\]]*)\]\(([^\)]*)\)"
    return re.findall(regex, text)

def extract_markdown_links(text):
    """ return list of tuples of links """
    regex = r"(?<!!)\[([^\]]*)\]\(([^\)]*)\)"
    return re.findall(regex, text)
