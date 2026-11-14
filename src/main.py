from markdown_to_page import copy_static_to_public, generate_pages


#from markdown_to_blocks import markdown_to_html_node


def main():
    print("starting")
    copy_static_to_public()
    generate_pages("content", "template.html", "public")


if __name__:
    main()
