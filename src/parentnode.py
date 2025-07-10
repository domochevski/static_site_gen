from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, value = None, children = children, props = props)

    def to_html(self):
        if self.tag is None:
            raise ValueError
        output = ""
        if self.children is None:
            raise ValueError("No children")
        elif self.children == []:
            return f"<{self.tag}{self.props_to_html()}></{self.tag}>"
        else:
            output += f"<{self.tag}{self.props_to_html()}>"
            for child in self.children:
                output += f"{child.to_html()}"
            output += f"</{self.tag}>"
            return output