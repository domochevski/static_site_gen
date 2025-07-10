from htmlnode import HTMLNode
from textnode import TextNode,TextType
from leafnode import LeafNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag = None, value = text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag = "i", value = text_node.text)
        case TextType.BOLD:
            return LeafNode(tag = "b", value = text_node.text)
        case TextType.CODE:
            return LeafNode(tag = "code", value = text_node.text)
        case TextType.LINK:
            return LeafNode(tag = "a", value = text_node.text, props = {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag = "img", value = "", props = {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if old_nodes.TextType is not "text":
        return new_nodes.append(old_nodes)

    new_nodes_list = old_nodes.copy()
    if len(new_nodes_list)%2 is not 0:
        raise Exception("Open delimiter")
    while delimiter in new_nodes_list:
        pass

    




    