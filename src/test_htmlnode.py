import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode(tag="Hello")
        expected_result = "Hello"
        self.assertEqual(node.tag, expected_result)

    
    def test_props(self):
        test_case = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        expected_result = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode(props=test_case)
        self.assertEqual(node.props_to_html(), expected_result)

    def test_props_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
        

if __name__ == "__main__":
    unittest.main()