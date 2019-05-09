#!/usr/bin/env python3


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def process(self):
        """
        Can be any data processing instruction you want according to your problem.
        :return: Print the node data.
        """
        print(self.data)


# Depth-first search
def pre_order(node):
    """
    Pre-order traversal is topologically sorted.
    NLR :
    Process the Node data
    Traverse left sub-tree recursively
    Traverse right sub-tree recursively
    """
    if node:
        node.process()
        pre_order(node.left)
        pre_order(node.right)


def in_order(node):
    """
    In-order traversal retrieves data in sorted order.
    LNR :
    Traverse left sub-tree recursively
    Process the Node data
    Traverse right sub-tree recursively
    """
    if node:
        in_order(node.left)
        node.process()
        in_order(node.right)


def out_order(node):
    """
    Out-order traversal retrieves data in reverse sorted order
    RNL:
    Traverse right sub-tree recursively
    Process the Node data
    Traverse left sub-tree recursively
    """
    if node:
        in_order(node.right)
        node.process()
        in_order(node.left)


def post_order(node):
    """
    LRN :
    Traverse left sub-tree recursively
    Traverse right sub-tree recursively
    Process the Node data
    """
    if node:
        in_order(node.right)
        in_order(node.left)
        node.process()
