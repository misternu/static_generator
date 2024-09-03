""" HTMLNode """

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
        if self.props is None:
            return ""
        strings = [f" {key}=\"{self.props[key]}\"" for key in self.props]
        return "".join(strings)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    """ single HTMLNode with no children """
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("All leaf nodes must have a value")
        super().__init__(tag, value, [], props)

    def to_html(self):
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
