class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not yet implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        attributeString = ""
        for item in self.props:
            attributeString +=f' {item}="{self.props[item]}"'
        return attributeString

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: should have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: should have a tag")
        if self.children == None:
            raise ValueError("Invalid HTML: no child nodes")
        childString = ""
        # for child in self.children:
        #     childString +=f"{child.to_html()}"
        # return f"<{self.tag}>{childString}</{self.tag}>"
        for child in self.children:
            childString +=child.to_html()
        return f"<{self.tag}>{self.props_to_html()}{childString}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"