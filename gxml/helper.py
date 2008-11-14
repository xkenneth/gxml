def assemble(node,api):
    """Recursively assembles all the child nodes of a node."""
    #We need this for when we parse from a string or file to 
    #create a dom
    for child_node in node.get_child_nodes():
        new_node = api(child_node,node)
        assemble(new_node,api)
        node.child_nodes.append(new_node)

    return node
