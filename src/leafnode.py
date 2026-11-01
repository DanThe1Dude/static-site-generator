from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None, props: dict | None = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value == None or self.value == "":
            raise ValueError("value missing")
        if self.tag == None or self.tag == "":
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"