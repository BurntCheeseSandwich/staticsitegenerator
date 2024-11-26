import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a new text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_URL(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode('This is a text node', TextType.ITALIC,'www.dot.com')
        self.assertEqual("TextNode(This is a text node, italic, www.dot.com)", repr(node))


if __name__ == "__main__":
    unittest.main()