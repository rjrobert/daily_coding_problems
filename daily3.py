"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    if root is None:
        return '[null]'
    if root.left is None and root.right is None:
        return root.val

    leftVal = serialize(root.left)
    rightVal = serialize(root.right)

    retVal = root.val
    if leftVal is not '':
        retVal += ' ' + leftVal
    if rightVal is not '':
        retVal += ' ' + rightVal
    return retVal


def deserialize(nodeStr):
    serial = nodeStr.split()
    serial.reverse()
    return _deserialize(serial)


def _deserialize(nodeStr):
    if not nodeStr:
        return None

    node = None
    value = nodeStr.pop()
    if value != '[null]':
        leftValue = _deserialize(nodeStr)
        rightValue = _deserialize(nodeStr)
        node = Node(value, leftValue, rightValue)

    return node


node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
print(serialize(deserialize(serialize(node))))
assert deserialize(serialize(node)).left.left.val == 'left.left'
