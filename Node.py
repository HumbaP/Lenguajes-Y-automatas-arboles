class Node:
    '''Clase nodo'''
    def __init__(self,data):
        self.data=data
        self.left_node=None
        self.right_node=None

    def add_left(self,node):
        self.left_node=node

    def add_right(self, node):
        self.right_node=node

    def say_hi(self):
        print("Hello, how are you?")

class BinaryTree:
    '''Clase nodo tiene los atributos: 
    Root=raiz del arbol binario'''

    def __init__(self,infix_exp):
        operators = "()-+/*"
        node_stack = []
        root=[]
        right=[]
        left=[]

        for char in infix_exp :
            if(char not in operators):
                root =Node(char)
                node_stack.append(root)
            else:
                root=Node(char)
                #Asignar
                right = node_stack.pop()
                left = node_stack.pop()
                root.add_left(left)
                root.add_right(right)
                #Subarbol a la pila
                node_stack.append(root)
        self.root=node_stack.pop()

    def preorder_print(self):
        self.pr_preorder_print(self.root)

    def pr_preorder_print(self, node):
        if(node is None):
            return
        print(node.data)
        self.pr_preorder_print(node.left_node)
        self.pr_preorder_print(node.right_node)

    def inorder_print(self):
        self.pr_inorder_print(self.root)

    def pr_inorder_print(self, node):
        if(node is None):
            return
        self.pr_inorder_print(node.left_node)            
        print(node.data)
        self.pr_inorder_print(node.right_node)

    def posorder_print(self):
        self.pr_posorder_print(self.root)

    def pr_posorder_print(self, node):
        if(node is None):
            return
        self.pr_posorder_print(node.left_node)
        self.pr_posorder_print(node.right_node)
        print(node.data)       
    
    def add_node(self,node):
        if(node==None):
            self.root=node
            return True
        return self.pr_add_node(self.root,node)
    
    def pr_add_node(self,act_node,insert_node):
        if(act_node.data== insert_node.data):
            return False
        if(act_node.data > insert_node.data):
            if(act_node.left_node is None):
                act_node.add_left(insert_node)
                return True
            else:
                return self.pr_add_node(act_node.left_node,insert_node)
        else:
            if(act_node.right_node is None):
                act_node.add_right(insert_node)
                return True
            else:
                return self.pr_add_node(act_node.right_node,insert_node)

"""node = Node(500)
node2 = Node(130)
node3 = Node(800)
tree = BinaryTree(node)
tree.add_node(node2)
tree.add_node(node3)

print("Preorder")
tree.preorder_print()

print("Inorder")
tree.inorder_print()

print("Posorder")
tree.posorder_print()
"""

def greater(to_compare, compared):
    operators_high="/*"
    operators_low= "-+"
    if(compared in operators_high and to_compare in operators_low):
        return True
    return False

def equals(to_compare, compared):
    operators_high="/*"
    operators_low= "-+"
    if(compared in operators_high and to_compare in operators_high):
        return True
    elif(compared in operators_low and to_compare in operators_low):
        return True
    return False


###Check this shit
def infix_posfix(infix_expression):
    op_stack =[]
    operators = "()-+/*"
    out_infix=""
    for char in infix_expression:
        if(char not in operators):#Es operador
            out_infix+=char
        else: #No es operador
            if(not(op_stack) or op_stack[-1]=='('):
                op_stack.append(char)
            elif(char==')'):
                while(not(op_stack) or op_stack[-1]=='('):
                    out_infix+=op_stack.pop()
                op_stack.pop()#Descartamos el (
            elif(greater(char,op_stack[-1])):
                op_stack.append(char)
            elif(equals(char, op_stack[-1])):
                op_stack.append(char)
            else:
                while(not(op_stack) and (greater(op_stack[-1],char))):
                    out_infix+=op_stack.pop()
    while(op_stack):
        out_infix+=op_stack.pop()
    return out_infix
            

expression="A*B/C+D"

infix_exp= infix_posfix(expression)

print(infix_exp)

tree = BinaryTree(infix_exp)


print('Preorder--------------------')
tree.preorder_print()

print('Inorder--------------------')
tree.inorder_print()

print('POSORDER--------------------')
tree.posorder_print()

