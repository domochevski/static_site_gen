import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_4_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()


    def test_no_tag(self):
        node = LeafNode(None, "Some text")
        result = node.to_html()
        expected = "Some text"
        self.assertEqual(result, expected)

    def test_lefnodes_with_props(self):
        node = LeafNode("a", "Link!", {"href": "https://example.com"})
        result = node.to_html()
        expected = "<a href=\"https://example.com\">Link!</a>"
        self.assertEqual(result, expected)

    


if __name__ == "__main__":
    unittest.main()