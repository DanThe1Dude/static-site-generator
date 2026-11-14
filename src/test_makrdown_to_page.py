from multiprocessing import Value
import unittest

from markdown_to_page import extract_title


class TestTitleExtraction(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(extract_title("# heading here\n not a heading"), "heading here")

    def test_failure(self):
        self.assertRaises(ValueError, extract_title, "not heading here\n not a heading")