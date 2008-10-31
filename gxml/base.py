class node(object):
    def __init__(self,node=None,parent=None):
        """A base class for all API Abstractions."""
        
        #the library dependent xml node
        self.node = node

        #the gXML object parent
        self.parent = parent
        
        #the text after the tag? oddness
        
        #whether or not we've altered the child_nodes, needs to be marked
        #for proper operation, should be true on instantiation
        self._child_nodes_changed = True

    def __len__(self):
        return len(self.child_nodes)
        
    def __iter__(self):
        return self.child_nodes.__iter__()

    def __repr__(self):
        return "gXML <%s>" % self.tag

    def __eq__(self,other):
        """Test if two nodes are equal."""
        #if the nodes aren't equal, the respective toolkits should handle overloading this operator
        if self.node != other.node:
            return False

    def __ne__(self,other):
        """Test if two nodes are not equal."""
        return not self == other
