from textnode import TextNode, LeafNode, TextType

from extract_link_img import extract_markdown_images, extract_markdown_links


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

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]: #inefficent code copy paste. could use advanced method to combine common code into one function
    new_nodes : list[TextNode] = []
    for old_node in old_nodes:
        original_text = old_node.text
        temp = extract_markdown_images(original_text)
        if temp != []:
            rest_of_text = original_text
            for image_alt, image_link in temp:
                sections = rest_of_text.split(f"![{image_alt}]({image_link})", 1)
                rest_of_text = sections[1]
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            if rest_of_text != "":
                new_nodes.append(TextNode(rest_of_text, TextType.TEXT))
        else:
            new_nodes.append(old_node)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]: #inefficent code copy paste. could use advanced method to combine common code into one function
    new_nodes : list[TextNode] = []
    for old_node in old_nodes:
        original_text = old_node.text
        temp = extract_markdown_links(original_text)
        if temp != []:
            rest_of_text = original_text
            for link_text, link in temp:
                sections = rest_of_text.split(f"[{link_text}]({link})", 1)
                rest_of_text = sections[1] if len(sections) > 1 else ""
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINKS, link))
            if rest_of_text != "":
                new_nodes.append(TextNode(rest_of_text, TextType.TEXT))
        else:
            new_nodes.append(old_node)
    return new_nodes

def text_to_text_nodes(text):
    with_links = split_nodes_link([TextNode(text, TextType.TEXT)])
    with_images = split_nodes_image(with_links)
    with_bold = split_nodes_delimiter(with_images, "**", TextType.BOLD)
    with_italics = split_nodes_delimiter(with_bold, "_", TextType.ITALIC)
    with_code_block = split_nodes_delimiter(with_italics, "`", TextType.CODE_TEXT)
    results = with_code_block
    return results