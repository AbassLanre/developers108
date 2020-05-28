 class NodeLinkedList(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class NodeTree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def dfs(self, root):
        import collections
        stack = [root]
        leafs = []
        while stack:
            curr_node = stack.pop()
            if curr_node.left == None and curr_node.right == None:
                leafs.append(curr_node.val)     
            children = [curr_node.right, curr_node.left]
            for child in children:
                if child:
                    stack.append(child)
        return leafs

tree = NodeTree(1)
tree.left = NodeTree(2)
tree.right = NodeTree(3)
tree.left.left = NodeTree(4)
tree.left.right = NodeTree(5)

leafs = tree.dfs(tree)
final = myLinked = NodeLinkedList(leafs[0])

for i in range(1,len(leafs)):
    curr_node = NodeLinkedList(leafs[i])
    myLinked.next = curr_node
    myLinked = myLinked.next

while final:
    print(final.val)
    final = final.next




                            #      1
                            #    /  \
                            #   2    3
                            #  / \
                            # 4  5


# listt = [4, 5,3]
# stack = [1]
# #   seen = {}
# curr_node = 1; stack = [3, 2]
# # seen= {1: True}
# curr_node = 2; stack = [3]
# #  seen = {1:True, 2: True}
# stack = [3, 5, 4]
# curr_node = 4; stack = [3, 5]
# curr_node = 5; stack = [3]
# curr_node = 3; stack = []



# node = '1'
# import collections
# hashTable = collections.defaultdict = {}


# hashTable[node] = True, {1: True}

# d = {}
# d[1] = True , {1: True}





