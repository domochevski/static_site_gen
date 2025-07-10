import unittest

from htmlnode import HTMLNode
from textnode import TextNode,TextType
from leafnode import LeafNode
from utils import text_node_to_html_node


class TestConverters(unittest.TestCase):
    def test_text(self):
        node_text = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node_text)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node_bold = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node_bold)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node_italic = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node_italic)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")
        
    def test_code(self):
        node_code = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node_code)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")        
        
    def test_url(self):
        node_none_url = TextNode("This is a text node with link and no url", TextType.LINK, None)
        node_url = TextNode("This is a text node with url", TextType.LINK, "https://go.home")
        html_node_none_url = text_node_to_html_node(node_none_url)
        html_node_with_url = text_node_to_html_node(node_url)
        self.assertEqual(html_node_none_url.tag, "a")
        self.assertEqual(html_node_with_url.tag, "a")
        self.assertEqual(html_node_none_url.props["href"], None)
        self.assertEqual(html_node_with_url.props["href"], "https://go.home")

    def test_image(self):
        node_image = TextNode("This is a text node with image", TextType.IMAGE, "https://go.home")
        html_node = text_node_to_html_node(node_image)
        self.assertEqual(html_node.props["src"], "https://go.home")
        self.assertEqual(html_node.props["alt"], "This is a text node with image")
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")

if __name__ == "__main__":
    unittest.main()