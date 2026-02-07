class DoctorNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, manager_dr, employee_dr, side, current_node=None):
        #Empty Tree
        if self.root is None:
            print("Tree is empty, cant insert without root")
        #Start from root
        if current_node is None:
            current_node = self.root
        #Found the manager node
        if current_node.value == manager_dr:
            if side == "left" and current_node.left is None:
                current_node.left = DoctorNode(employee_dr)
                return True
            elif side == "right" and current_node.right is None:
                current_node.right = DoctorNode(employee_dr)
                return True
            else:
                print(f"{manager_dr} already has a {side} subordinate")
                return True
            
        found_left = False
        found_right = False

        if current_node.left:
            found_left = self.insert(manager_dr, employee_dr, side, current_node.left)

        if current_node.right and not found_left:
            found_right = self.insert(manager_dr, employee_dr, side, current_node.right)
    
    def preorder(self, node=None):
        if node is None:
            node = self.root
        
        result = [node.value]
            
        if node.left:
            result.extend(self.preorder(node.left))

        if node.right:
            result.extend(self.preorder(node.right))

        return result

    def inorder(self, node=None):
        if node is None:
            node = self.root

        result = []

        if node.left:
            result.extend(self.inorder(node.left))
        
        result.append(node.value)

        if node.right:
            result.extend(self.inorder(node.right))

        return result

    def postorder(self,node=None):
        if node is None:
            node = self.root
        
        result = []

        if node.left:
            result.extend(self.postorder(node.left))
        
        if node.right:
            result.extend(self.postorder(node.right))

        result.append(node.value)

        return result
        


# Test your DoctorTree and DoctorNode classes here

tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft") 
# Insert values
tree.insert("Dr. Croft", "Dr. Goldsmith", "right") 
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right") 
tree.insert("Dr. Phan", "Dr. Morgan", "left")
print(tree.preorder())
print(tree.inorder())
print(tree.postorder())
