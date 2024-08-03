class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if not self:
            return 0
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    def size(self):
        if not self:
            return 0
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        return 1 + left_size + right_size

    def traverse_in_order(self):
        if not self:
            return []
        return (self.left.traverse_in_order() if self.left else []) + \
               [self.key] + \
               (self.right.traverse_in_order() if self.right else [])

    def display_keys(self, space='\t', level=0):
        # If the node is empty (which shouldn't occur if `self` exists)
        if not self:
            print(space * level + '∅')
            return   

        # If the node has children, display the right subtree first
        if self.right:
            self.right.display_keys(space, level + 1)
        print(space * level + str(self.key))
        if self.left:
            self.left.display_keys(space, level + 1)

    def to_tuple(self):
        if not self:
            return None
        if not self.left and not self.right:
            return self.key
        return (self.left.to_tuple() if self.left else None, 
                self.key, 
                self.right.to_tuple() if self.right else None)

    def __str__(self):
        return f"BinaryTree <{self.to_tuple()}>"

    def __repr__(self):
        return f"BinaryTree <{self.to_tuple()}>"

    @staticmethod    
    def parse_tuple(data):
        if data is None:
            return None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node
