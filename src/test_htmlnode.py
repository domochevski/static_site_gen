import unittest

from htmlnode import HTMLNode


class TestHTMLnode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()


    def test_props_to_html(self):
        props_dic = {
            "href": "https://www.google.com",
            "target": "_blank",    
        }
        node = HTMLNode(props = props_dic)
        result = node.props_to_html()
        expected = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(result, expected)

    def test_view(self):
        props_dic = {
        "href": "https://www.google.com",
        "target": "_blank",    
        }
        node = HTMLNode("p", "TextValue", None, props_dic)
        result = str(node)
        expected = "Tag: p, Value: TextValue, Children: None, Props: {'href': 'https://www.google.com', 'target': '_blank'}"
        self.assertEqual(result, expected)

    


if __name__ == "__main__":
    unittest.main()