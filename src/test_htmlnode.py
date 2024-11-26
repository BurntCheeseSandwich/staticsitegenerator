import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()