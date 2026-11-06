import unittest

from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType


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