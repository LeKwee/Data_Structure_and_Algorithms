from Binary_tree import fill_tree
from collections import deque

def levelOrder(root):
    '''
    Have 2 list for results:
        - one to hold all values of all levels (overall_result)
        - one to hold values of a single level to be appended to results (current_level_result)

    Have 2 queues:
        - one for the current level of nodes (current_level_queue)
        - one to append the next level of nodes by popping from current_queue (append to current_level_result to gather values of this level) and getting its children nodes. (next_level_queue)

    Logic:
        1) Add current level nodes to current_level_queue
        2) for each node in current_level_queue,
            - pop node
            - add node to current_level_result
            - add node's children to next_level_queue
        3) Now that current_level_queue is empty
            - append current_level_result to overall_result
            - empty current_level_result
            - assign next_level_queue to current_level_queue
            - assign current_level_queue to next_level_queue
        4) repeat steps 1 to 3 until both current_level_queue and next_level_queue are empty and return overall_result
    '''

    # check if root is empty, return empty list
    if not root:
        return []

    # init our return lists
    overall_result, current_level_result = [], []

    # init our 2 queues
    current_level_queue, next_level_queue = deque(), deque()

    # add root node to current_level_queue
    current_level_queue.append(root)

    # loop logic which current_level_queue is not empty
    while current_level_queue:
        # pop node 
        node = current_level_queue.popleft()
        # add node to current_level_result
        current_level_result.append(node.value)
        # add node's children to next_level_queue
        if node.left:
            next_level_queue.append(node.left)
        if node.right:
            next_level_queue.append(node.right)
        
        # if current_level_queue is empty
        if not current_level_queue:
            # append current_level_result to overall_result
            overall_result.append(current_level_result)
            # empty current_level_result
            current_level_result = []
            # swap queues
            current_level_queue, next_level_queue = next_level_queue, current_level_queue
            
    return overall_result


if __name__ == '__main__':
    import Binary_tree

    # init tree
    tree = Binary_tree.Binary_tree()
    tree = fill_tree(tree, 20)
    tree.print_tree()

    # get level ordered nodes
    print(levelOrder(tree.root))
