from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type == TextType.TEXT:
            texts = old_node.text.split(delimiter)
            if len(texts) % 2 == 0:
                raise SyntaxError(f"Invalid Markdown Syntax: Delimiter {delimiter} is missing")

            for i in range(len(texts)):
                text = texts[i]
                if text != "":
                    if i % 2 == 1:
                        new_text_type = text_type
                    else:
                        new_text_type = TextType.TEXT
                    new_nodes.append(TextNode(text, new_text_type))
            
        else:
            new_nodes.append(old_node)

    
    return new_nodes