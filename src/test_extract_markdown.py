""" test extract markdown """

import unittest
from extract_markdown import (
    extract_markdown_images,
    extract_markdown_links
)

TEXT_1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) " \
         "and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
TEXT_2 = "This is text with a link [to boot dev](https://www.boot.dev) and " \
         "[to youtube](https://www.youtube.com/@bootdotdev)"

class TestExtractMarkdown(unittest.TestCase):
    """ test helper functions for extracting markdown images and links """

    def test_extract_markdown_images(self):
        """ test extract markdown images on string with images """
        result = extract_markdown_images(TEXT_1)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            result
        )

    def test_extract_markdown_images_na(self):
        """ test extract markdow images on string without images """
        result = extract_markdown_images(TEXT_2)
        self.assertListEqual([], result)

    def test_extract_markdown_links(self):
        """ test extract markdown images on string with links """
        result = extract_markdown_links(TEXT_2)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev")
            ],
            result
        )

    def test_extract_markdown_links_na(self):
        """ test extract markdow images on string without links """
        result = extract_markdown_links(TEXT_1)
        self.assertListEqual([], result)

if __name__ == "__main__":
    unittest.main()
