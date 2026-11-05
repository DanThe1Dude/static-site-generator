def markdown_to_blocks(markdown : str):
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