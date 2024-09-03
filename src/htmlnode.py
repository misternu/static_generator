""" html node """

class HTMLNode:
    """ represents a node in html """
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """ not implemented """
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        """ map props to html attribute string """
        strings = [f" {key}=\"{self.props[key]}\"" for key in self.props]
        return "".join(strings)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
