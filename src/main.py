import os
import shutil

from markdown_to_blocks import markdown_to_html_node


def main():
    copy_static_to_public()


def copy_static_to_public():
    clear_public()

def clear_public():
    shutil.rmtree("public/")
    os.mkdir("public")

def copy_all_r(source, destination):
    print(f"source: {source}")
    if not os.path.exists(source):
        return
        
    shutil.copy(source, destination)
    if os.path.isdir(source):
        branches = os.listdir(source)
        for branch in branches:
            copy_all_r(source+branch, destination+branch)
        
        

if __name__ == "main":
    main()
