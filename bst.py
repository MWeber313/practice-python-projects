class BinarySearchTree(self, value):
    def __init__:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value and self.left is None:
            self.left = BinarySearchTree(value)
        elif value > self.value and self.right is None:
            self.right = BinarySearchTree(value)
        elif value <= self.value and self.left is not None:
            self.left.insert(value)
        else:
            self.right.insert(value)
