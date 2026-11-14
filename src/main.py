from sys import argv

from markdown_to_page import copy_static_to_dir, generate_pages


def main():
    basepath = argv[-1] if argv[-1] != None else "/"
    print("starting")
    copy_static_to_dir()
    generate_pages("content", "template.html", "docs", basepath)
    print("finished")


if __name__:
    main()
