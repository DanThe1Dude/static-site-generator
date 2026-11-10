from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str | None, children: list["HTMLNode"] | None, props: dict | None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag == None or self.tag == "":
            raise ValueError("tag missing")
        if self.children == None or len(self.children) == 0:
            raise ValueError(f"children missing or too few: {self.tag}, {self.value}, {self.children}")
        children_as_html = ""
        for child in self.children:
            children_as_html = children_as_html + child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{children_as_html}</{self.tag}>"