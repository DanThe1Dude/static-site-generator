class HTMLNode:
    def __init__(self, tag : str | None = None, value : str | None = None, children : list["HTMLNode"] | None = None, props : dict | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        return NotImplemented

    def props_to_html(self) -> str:
        if self.props is None or len(self.props) == 0:
            return ""
        results = ""
        for key, value in self.props.items():
            results = f'{results} {key}="{value}"'
        return results

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

        
        