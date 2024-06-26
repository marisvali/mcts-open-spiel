NAIVE_POLICY_EXPLORE = 25 # naive exploring constant: the higher, the more reliable, but slower in execution time

def Policy_Player_Naive(mytree):
    for i in range(NAIVE_POLICY_EXPLORE):
        mytree.explore()
    
    next_tree, next_action = mytree.next()
        
    # note that here we are detaching the current node and returning the sub-tree 
    # that starts from the node rooted at the choosen action.
    # The next search, hence, will not start from scratch but will already have collected information and statistics
    # about the nodes, so we can reuse such statistics to make the search even more reliable!
    next_tree.detach_parent()
    # I don't detach the parent because I want to visualize the entire graph.

    
    return next_tree, next_action