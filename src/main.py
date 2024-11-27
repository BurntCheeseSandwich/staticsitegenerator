from textnode import *

def main():
    testNode = TextNode("This is a test node",TextType.IMAGE, "https://www.boot.dev")
    leafNode = text_node_to_html_node(testNode)
    print(leafNode.__repr__())

if __name__ == "__main__":
    main()
