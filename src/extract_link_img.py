import re


def extract_markdown_images(text : str) -> list[tuple[str, str]]:
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images

def extract_markdown_links(text : str) -> list[tuple[str, str]]:
    links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return links