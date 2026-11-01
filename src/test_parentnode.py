import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_without_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_without_children(self):
        parent_node = ParentNode("p", [])
        self.assertRaises(ValueError, parent_node.to_html)
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_empty_child(self):
        child_node = LeafNode("", "")
        parent_node = ParentNode("div", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_children_and_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        child_node2 = LeafNode("i", "child")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span><i>child</i></div>")
        