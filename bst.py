class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value and self.left is None:
            self.left = BinarySearchTree(value)
        elif value > self.value and self.right is None:
            self.right = BinarySearchTree(value)

    def print_node_ascending(self):
        if self.left:
            self.left.print_node_ascending()

        print(self.value)

        if self.right:
            self.right.print_node_ascending()
    
    def print_node_descending(self):
        if self.right:
            self.right.print_node_descending()
        
        print (self.value)

        if self.left:
            self.left.print_node_descending()

    def fill_tree_halves(self):
        print('please insert a number between 2-99 to be halved')

        value = int(input())

        new_tree = BinarySearchTree(int(value))

        filling = True

        while filling:

            if value <= 1:
                filling = False

            elif value >= 100:
                filling = False

            elif new_tree.value > value:
                self.left.insert(value // 2)
            
            elif new_tree.value < value:
                self.right.insert(value * 2)

        print('ascending')
        new_tree.print_node_ascending()
        print('descending')
        new_tree.print_node_descending()


a = BinarySearchTree(42)
a.insert(33)
a.insert(99)

a.print_node_ascending()
a.print_node_descending()
