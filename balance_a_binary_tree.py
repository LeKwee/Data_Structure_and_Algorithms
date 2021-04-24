'''
Types of Tree traversals:

1) InOrder --> Left, Root, Right
2) PreOrder --> Root, Left, Right
3) PostOrder --> Left, Right , Root

Solution:
1) traverse tree BST in inorder adn store results in an array.
time: O(n)
Array will already be sorted as inorder traversal of BST always produces sorted array.

2) Build a new balanced BST recursively.
    - split array in the middle
    - middle element = root
    - repeat above 2 steps for left array and right array.
'''

import Binary_tree

def get_sorted_list(root, sorted_list):
    
    # exit condition
    if not root:
        return 
    
    get_sorted_list(root.left, sorted_list)
    sorted_list.append(root.value)
    get_sorted_list(root.right, sorted_list)

def build_balanced_BST(sorted_list, start, end):
    if start > end:
        return 

    mid = (start+end)//2
    node = Binary_tree.Node(sorted_list[mid])

    node.left = build_balanced_BST(sorted_list, start, mid-1)
    node.right = build_balanced_BST(sorted_list, mid+1, end)
    return node

if __name__ == "__main__":
    print('hello')
    tree = Binary_tree.Binary_tree()
    tree = Binary_tree.fill_tree(tree, 7)
    tree.print_tree()

    sorted_list=[]
    get_sorted_list(tree.root, sorted_list)
    print(sorted_list)

    balanced_BST_root =build_balanced_BST(sorted_list, 0, len(sorted_list)-1)
    balanced_BST = Binary_tree.Binary_tree(balanced_BST_root)
    balanced_BST.print_tree()