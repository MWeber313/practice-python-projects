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
        elif value <= self.value and self.left:
            self.left.left = BinarySearchTree(value)
        elif value > self.value and self.right:
            self.right.right = BinarySearchTree(value)

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

        print('please insert a number between 2-99 to modify your value by')

        value = int(input())

        filling = True

        while filling:

            if value <= 1:
                filling = False

            elif value >= 100:
                filling = False

            elif self.value > value:
                self.left.insert(value // 2)
            
            elif self.value < value:
                self.right.insert(value * 2)

        print('ascending')
        self.print_node_ascending()
        print('descending')
        self.print_node_descending()


a = BinarySearchTree(42)
a.insert(33)
a.insert(99)

a.print_node_ascending()
a.print_node_descending()
a.fill_tree_halves()