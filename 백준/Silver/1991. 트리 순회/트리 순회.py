n = int(input())
tree = {}
result = ['', '', '']

for i in range(n):
    a, b, c = map(str, input().split())
    tree[a] = [b, c]
    
def preorder(root):
    if root != '.':
        result[0] += root
        preorder(tree[root][0])
        preorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        result[2] += root
        
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        result[1] += root
        inorder(tree[root][1])

preorder('A')
inorder('A')
postorder('A')
       
print(result[0])
print(result[1])
print(result[2])