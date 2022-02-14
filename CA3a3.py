class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
   


def insert(tree, key):
    if not tree:
        return Node(key)
    else:
        if tree.val == key:
            return tree
        elif tree.val < key:
            tree.right = insert(tree.right, key)
        else:
            tree.left = insert(tree.left, key)
    return tree


def search(tree, key):
    if not tree:
        return "NO"
    if  tree.val == key:
        return "YES"

    if tree.val < key:
        return search(tree.right, key)

    return search(tree.left, key)


INSERT='1'
SEARCH='2'
DEFAULT=-99
usr_input = [DEFAULT,DEFAULT]
temp = input()
rb_tree = Node(1000000)
for i in range(int(temp)):
    command = input()
    usr_input = command.split(" ")
    if usr_input[0] == INSERT:
        rb_tree = insert(rb_tree,int(usr_input[1]))
    elif usr_input[0] == SEARCH:
        result = search(rb_tree,int(usr_input[1]))
        print(result)

