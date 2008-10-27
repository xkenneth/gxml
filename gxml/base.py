class node(object):
    def __init__(self,node=None,parent=None):
        """A base class for all API Abstractions."""
        
        #the library dependent xml node
        self.node = node

        #the gXML object parent
        self.parent = parent
        
        #whether or not we've altered the child_nodes, needs to be marked
        #for proper operation, should be true on instantiation
        self._child_nodes_changed = True
        
        
    def __iter__(self):
        return self.child_nodes.__iter__()

    def __repr__(self):
        return "gXML <%s>" % self.tag
