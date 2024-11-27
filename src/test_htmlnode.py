import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_input(self):
        node = HTMLNode('div','no no')
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'no no')
        self.assertEqual(node.children, None)
        self.assertEqual(node.props,None)
    
    def test_method(self):
        node = HTMLNode(None,None,None,{
        "href": "https://www.google.com", 
        "target": "_blank",
        })
        a2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(),a2)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "what a strange place",
            None,
            {"class": "tertiary"}
        )
        self.assertEqual(node.__repr__(), "HTMLNode(p, what a strange place, None, {'class': 'tertiary'})")

class TestLeafNode(unittest.TestCase):
    def test_input(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, "This is a paragraph of text.")

    def test_html(self):
        node = LeafNode(None, "This is a paragraph of text.")
        ans = "This is a paragraph of text."
        self.assertEqual(node.to_html(),ans)

    def test_repr(self):
        node = LeafNode("p", "Hello world")
        self.assertEqual(node.to_html(), "<p>Hello world</p>")

class TestParentNode(unittest.TestCase):
    def test_input(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
        self.assertEqual(node.tag, 'p')
        # self.assertEqual(node.children, [
        #     LeafNode("b", "Bold text"),
        #     LeafNode(None, "Normal text"),
        #     LeafNode("i", "italic text"),
        #     LeafNode(None, "Normal text"),
        # ])
        self.assertEqual(node.props, None)

    def test_html(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
        ans = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(),ans)

    def test_repr(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
        ],
    )
        ans = "ParentNode(p, [LeafNode(b, Bold text, None)], None)"
        self.assertEqual(node.__repr__(), ans)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()