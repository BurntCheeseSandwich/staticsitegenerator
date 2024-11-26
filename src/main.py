from textnode import *

def main():
    testNode = TextNode("This is a test node",TextType.BOLD, "https://www.boot.dev")
    print(testNode.__repr__())

if __name__ == "__main__":
    main()
