import unittest

from markdown_to_blocks import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
    markdown_to_html_node,
)


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph\n\nThis is another paragraph with _italic_ text and `code` here\n This is the same paragraph on a new line\n\n- This is a list\n- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_block_with_blanks(self):
        md = """This is **bolded** paragraph\n\n\n\nThis is another paragraph with _italic_ text and `code` here\n This is the same paragraph on a new line\n\n- This is a list\n- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestMarkdownToBlockTypes(unittest.TestCase):
    def test_paragraph(self):
        self.assertEqual(block_to_block_type("hello, this is a paragraph"), BlockType.PARAGRAPH)

    def test_headings(self):
        self.assertEqual(block_to_block_type("# Heading level 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading level 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading level 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Heading level 4"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Heading level 5"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading level 6"), BlockType.HEADING)

    def test_bad_heading(self):
        self.assertEqual(block_to_block_type("#Not A heading"), BlockType.PARAGRAPH)

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\n#This is a code block\nprint hi\n```"), BlockType.CODE)

    def test_bad_code_block(self):
        self.assertEqual(block_to_block_type("```\n#This is a not code block\nprint failure``"), BlockType.PARAGRAPH)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> this\n>should\n>be a quote"), BlockType.QUOTE)

    def test_bad_quote(self):
        self.assertEqual(block_to_block_type("> good\nnot a quote\n> good"), BlockType.PARAGRAPH)

class TestMarkdownToHTMLNodes(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_heading(self):
        md = """
# Heading test

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading test</h1><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_quote_block(self):
        md = """
        > This is hard

        Me"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is hard</blockquote><p>Me</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_ordered_list(self):
        md = """
1. thing
2. thing 2
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>1. thing</li><li>2. thing 2</li></ol></div>",
        )

    def test_unordered_list(self):
        md = """
- a thing
- another thing
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>- a thing</li><li>- another thing</li></ul></div>",
        )

    def d_test_full(self):
        md = """
# Full Test

This is **bolded** paragraph
text in a p
tag here

> HTML is hard

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        print(html)
        self.assertEqual(
            html,
            "<div><h1>Full Test</h1><p>This is <b>bolded</b> paragraph text in a p tag here</p><quoteblock>HTML is hard</quoteblock><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
