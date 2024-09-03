""" main """

from textnode import TextNode

def main():
    """ static site generator """
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)

main()
