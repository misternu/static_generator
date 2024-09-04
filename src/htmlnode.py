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
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    """ parent HTMLNode with children """
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.children is None:
            raise ValueError("All parent nodes must have children")
        if self.tag is None:
            raise ValueError("Cannot render without tag")
        children_html = map(lambda x: x.to_html(), self.children)
        return f"<{self.tag}{self.props_to_html()}>{"".join(children_html)}</{self.tag}>"
