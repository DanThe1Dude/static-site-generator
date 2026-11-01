from textnode import TextNode, TextType


def main():
    textnode = TextNode("This is some anchor text", TextType.BOLD, "https://www.boot.dev")
    print(textnode)

if __name__:
    main()