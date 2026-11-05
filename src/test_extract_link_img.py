import unittest

from extract_link_img import extract_markdown_images, extract_markdown_links


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_case_normal(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://www.boot.dev))"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_case_none_found(self):
        matches = extract_markdown_links(
            "This is text"
        )
        self.assertListEqual([], matches)

class TestExtractMarkdownImages(unittest.TestCase):
    def test_case_normal(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_case_none_found(self):
        matches = extract_markdown_images(
            "This is text"
        )
        self.assertListEqual([], matches)