from enum import Enum

from htmlnode import HTMLNode
from md_to_nodes import text_to_text_nodes
from src.leafnode import LeafNode
from src.parentnode import ParentNode
from textnode import text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    to_remove = []
    for i in range(len(blocks)):
        original_block = blocks[i]
        block = original_block
        block = block.strip(" ")
        block = block.strip("\n")
        temp = []
        for string in block.split("\n"):
            temp.append(string.strip(" "))
        block = "\n".join(temp)

        if block == "":
            to_remove.append(original_block)
        blocks[i] = block
    for remove in to_remove:
        if remove in blocks:
            print("blocks: ", blocks)
            print("remove: ", remove)
            blocks.remove(remove)
    return blocks

def block_to_block_type(block : str):
    lines = block.split("\n")
    
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

#def block_to_block_type(block: str) -> BlockType: #experiemtned with regex to achive the same thing with it, due to this I learnt a lot about regex and when it shouldn't be used.
    #if re.match(r"^#{1,6} ", block) != None:
    #    return BlockType.HEADING
    #elif re.fullmatch(r"`{3}\n[^`]*`{3}", block) != None:
    #    return BlockType.CODE
    #elif re.fullmatch(r"(?:> ?.*?\n?)+", block):
    #    return BlockType.QUOTE
    #elif re.fullmatch(r"(?:- .*?\n?)+", block):
    #    return BlockType.UNORDERED_LIST
    #elif block.startswith("1. "):
    #    lines = block.split("\n")
    #    i = 1
    #    for line in lines:
    #        if not line.startswith(f"{i}. "):
    #            return BlockType.PARAGRAPH
    #        i += 1
    #    return BlockType.ORDERED_LIST
    #else:
    #    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown : str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                html_node = ParentNode("p", [*text_to_children(block)])
            case BlockType.HEADING:
                level = 0
                for letter in block[0:6]:
                    if letter == "#":
                        level += 1
                block = block.lstrip("#")
                html_node = ParentNode(f"h{level}", [*text_to_children(block)])
            case BlockType.CODE:
                html_node = ParentNode("pre", [LeafNode("code", block.strip("`").lstrip("\n"))])
            case BlockType.QUOTE:
                html_node = ParentNode("blockquote", [*text_to_children(block.lstrip(">"))])
            case BlockType.UNORDERED_LIST:
                html_node = ParentNode("ul", [*text_to_list_elements(block)])
            case BlockType.ORDERED_LIST:
                html_node = ParentNode("ol", [*text_to_list_elements(block)])
        html_nodes.append(html_node)
    return ParentNode("div", children=html_nodes)

def text_to_children(text : str):
    preppred_text = text.replace("\n", " ").strip(" ")

    return list(map(text_node_to_html_node, text_to_text_nodes(preppred_text)))

def text_to_list_elements(text : str):
    lines = text.split("\n")
    results = []
    for line in lines:
        children = list(map(text_node_to_html_node, text_to_text_nodes(line)))
        for child in children:
            if child.tag == "p":
                child.tag = None
            li_node = ParentNode("li", [*children])
            results.append(li_node)
    return results