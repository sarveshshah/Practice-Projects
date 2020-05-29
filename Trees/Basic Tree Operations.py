from random import randint

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def print_node(self):
        if self.data:
            if self.left!=None:
                self.left.print_node()
            print(self.data)
            if self.right!=None:
                self.right.print_node()
    
    def insert(self,data):
        if self.data:
            # print(self.data)
            if self.data > data:
                if self.left != None:
                    self.left.insert(data)
                else:
                    self.left = node(data)
            elif self.data < data:
                if self.right != None:
                    self.right.insert(data)
                else:
                    self.right = node(data)
        else:
            self.data = data

    def search(self,n):
        if self.data:
            if self.data == n:
                print('Found it')
            elif self.data>n:
                if self.left is None:
                    print('Not in tree')
                else:
                    self.left.search(n)
            elif self.data<n:
                if self.right is None:
                    print('Not in tree')
                else:
                    self.right.search(n)
        else:
            print('Not in tree')

def fill_tree(node, n):
    for i in n:
        r.insert(i)

def find_value(node, n):
    for i in range(n):
        r.search(randint(1,100))

r = node(randint(1,100))
fill_tree(r,[43, 23, 69, 29, 44, 9, 60, 60, 68, 87])
r.print_node()




