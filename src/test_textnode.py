import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_text_none_url(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertIsNone(node.url)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINKS, "example.com")
        self.assertIsNotNone(node.url, "url is None on a link text type")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a", "tag missing for link type")
        self.assertIsNotNone(html_node.props, "props is missing, should contain 'href' key")
        if html_node.props != None:
            self.assertIn("href", html_node.props)

    def test_image_url(self):
        node = TextNode("This is a text node", TextType.IMAGE, "example.com")
        self.assertIsNotNone(node.url)


if __name__ == "__main__":
    unittest.main()