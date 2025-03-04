""" splitting and typing markdown blocks """
def markdown_to_blocks(markdown):
    """ takes a markdown formatted string and returns blocks of text """
    strings = markdown.split("\n\n")
    strings = list(map(str.strip, strings))
    strings = list(filter(lambda block: not len(block) == 0, strings))
    return strings
