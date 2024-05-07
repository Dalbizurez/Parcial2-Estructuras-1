class Node:
    def __init__(self, data, key) -> None:
        self.key = key
        self.data = data
        self.right : Node = None
        self.left : Node = None

    def __str__(self) -> str:
        return f"{self.data}"

    def __repr__(self) -> str:
        return f"{self.key}: {self.data}"
    
class Tree:
    def __init__(self) -> None:
        self.root: Node = None

    def insert(self, value, key = None):
        if not self.root:
            self.root = Node(value, key)
        else:
            self._insert(value, self.root, key)

    def _insert(self, value, node : Node = None, key = None):
        # key = key if key else value
        if key < node.key:
            if node.left:
                self._insert(value, node.left, key)
            else:
                node.left = Node(value, key)
        else:
            if node.right:
                self._insert(value, node.right, key)
            else:
                node.right = Node(value, key)
    def height(self):
        if not self.root:
            return 0
        return 1 + max(self.height(self.root.left), self.height(self.root.right))
    
    def balanced(self):
        return abs(self._height(self.root.left) - self._height(self.root.right)) <= 1
    
    def level(self, value, key, lvl = 0):
        if not self.root:
            return -1
        if self.root.data == value:
            return lvl
        if key < self.root.key:
            return self._level(value, key, lvl + 1, self.root.left)
        return self._level(value, key, lvl + 1, self.root.right)
    
    def delete(self, key):
        if not self.root:
            return
        if key < self.root.key:
            self.root.left = self._delete(key, self.root.left)
        elif key > self.root.key:
            self.root.right = self._delete(key, self.root.right)
        else:
            if not self.root.left:
                return self.root.right
            if not self.root.right:
                return self.root.left
            temp = self.root.right
            while temp.left:
                temp = temp.left
            self.root.key = temp.key
            self.root.data = temp.data
            self.root.right = self._delete(temp.key, self.root.right)
        return self.root
    
    def key_binary_search(self, key):
        if not self.root:
            return None
        if self.root.key == key:
            return self.root
        if key<self.root.key:
            return self._key_binary_search(key, self.root.left)
        return self._key_binary_search(key, self.root.right)
    
    def binary_search(self, value, key = -1):
        if not self.root: 
            return False
        if self.root.data == value:
            return True
        if key < self.root.key:
            return self.binary_search(value, key, self.root.left)
        return self.binary_search(value, key, self.root.right)
    
    def reorganize(self):
        elements = []
        if self.root:
            self.reorganize(self.root.left, elements)
            elements.append(self.root)
            self.reorganize(self.root.right, elements)
        new = Tree()
        for e in elements:
            new.insert(e.data, e.key)
        return new
    
def preorder(node : Node):
    txt = ""
    if node:
        txt += str(node.key) + ','
        txt += preorder(node.left)
        txt += preorder(node.right)
    return txt

def inorder(node : Node):
    txt = ""
    if node:
        txt += inorder(node.left)
        txt += str(node.key) + ','
        txt += inorder(node.right)
    return txt

def postorder(node : Node):
    txt = ""
    if node:
        txt += postorder(node.left)
        txt += postorder(node.right)
        txt += str(node.key) + ','
    return txt


def insert(value, key, node:Node = None):
    if not node:
        return Node(value, key)
    if key < node.key:
        node.left = insert(value, key, node.left)
    else:
        node.right = insert(value, key, node.right)
    return node

def height(node:Node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

    h_l = 1
    left =  node
    while left:
        h_l += 1
        left = left.left
    h_r = 1
    right =  node
    while right:
        h_r += 1
        right = right.right
    return max(h_l, h_r)

def balanced(node:Node):
    return abs(height(node.left) - height(node.right)) <= 1
    

def level(node:Node, value, key, lvl = 0):
    if not node:
        return -1
    if node.data == value:
        return lvl
    if key < node.key:
        return level(node.left, value, key, lvl + 1)
    return level(node.right, value, key, lvl + 1)

def delete(key, node):
    if not node:
        return
    if key < node.key:
        node.left = delete(key, node.left)
    elif key > node.key:
        node.right = delete(key, node.right)
    else:
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        temp = node.right
        while temp.left:
            temp = temp.left
        node.key = temp.key
        node.data = temp.data
        node.right = delete(temp.key, node.right)
    return node

def key_binary_search(key, node:Node):
    if not node:
        return None
    if node.key == key:
        return node
    if key<node.key:
        return key_binary_search(key, node.left)
    return key_binary_search(key, node.right)

def binary_search(value, node:Node, key = -1):
    if not node: 
        return False
    if node.data == value:
        return True
    if key < node.key:
        return binary_search(value, node.left, key)
    return binary_search(value, node.right, key)
        
def reorganize(node:Node, elements = []):
    if node:
        reorganize(node.left, elements)
        elements.append(node)
        reorganize(node.right, elements)
    new = Tree()
    for e in elements:
        new.insert(e.data, e.key)
    return new

def preorder(node : Node):
    txt = ""
    if node:
        txt += str(node.key) + ','
        txt += preorder(node.left)
        txt += preorder(node.right)
    return txt

def inorder(node : Node):
    txt = ""
    if node:
        txt += inorder(node.left)
        txt += str(node.key) + ','
        txt += inorder(node.right)
    return txt

def postorder(node : Node):
    txt = ""
    if node:
        txt += postorder(node.left)
        txt += postorder(node.right)
        txt += str(node.key) + ','
    return txt

