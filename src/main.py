import os
import shutil

from src.markdown_to_blocks import markdown_to_html_node


def main():
    copy_static_to_public()


def copy_static_to_public():
    shutil.rmtree("public/")
    os.mkdir("public")


if __name__ == "main":
    main()
