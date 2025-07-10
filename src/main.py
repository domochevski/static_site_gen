from textnode import * 


def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev"))
    print(TextNode("This is some anchor text 2", TextType.LINK, "https://www.boot.dev 2"))

main()