import re
from enum import Enum


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

def markdown_to_html_node(markdown):
    print("help me")