import os
import shutil

from markdown_to_blocks import markdown_to_html_node


def copy_static_to_public():
    clear_public()
    copy_all_r("static", "public")


def clear_public():
    shutil.rmtree("public")
    os.mkdir("public")


def copy_all_r(source, destination):
    print(f"source: {source}")
    if not os.path.exists(source):
        return

    if os.path.isfile(source):
        shutil.copy(source, destination)
    elif os.path.isdir(source):
        if not os.path.exists(destination):
            os.mkdir(destination)
        branches = os.listdir(source)
        for branch in branches:
            copy_all_r(f"{source}/{branch}", f"{destination}/{branch}")


def extract_title(markdown : str) -> str:
    line1: str = markdown.split("\n", 1)[0]
    if line1.startswith("#"):
        return line1.lstrip("# ")
    raise ValueError("Title not found at start of input")

def generate_page(from_path : str, template_path : str, dest_path : str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        content = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    title = extract_title(content)
    content_to_html_nodes = markdown_to_html_node(content)
    html_content = content_to_html_nodes.to_html()
    template = template.replace("{{ Title }}", title)
    final = template.replace("{{ Content }}", html_content)

    parts = dest_path.split("/")
    current_path = parts[0]
    for part in parts[1:-1]:
        current_path += "/" + part
        if not os.path.exists(current_path):
            os.mkdir(current_path)
    with open(dest_path.replace(".md", ".html"), "x") as f:
        f.write(final)
        
def generate_pages(from_path : str, template_path : str, dest_path : str) -> None:
    if os.path.isfile(from_path):
        print(f"Generating: {from_path}")
        generate_page(from_path, template_path, dest_path)
    if os.path.isdir(from_path):
        paths = os.listdir(from_path)
        for path in paths:
            generate_pages(from_path + "/" + path, template_path, dest_path + "/" + path)