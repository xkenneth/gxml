class tag_node(object):
    def __init__(self,node=None,parent=None,**kwargs):
        """A base class for all API Abstractions."""
        
        #the library dependent xml node
        self.node = node

        #the gXML object parent
        self.parent = parent
        
        #whether or not we've altered the child_nodes, needs to be marked
        #for proper operation, should be true on instantiation
        self._child_nodes_changed = True

        self.child_nodes = []

        for key in kwargs:
            self.set(key,kwargs[key])
    
    def __getitem__(self,key):
        return self.child_nodes[key]
    
    def __len__(self):
        return len(self.child_nodes)
        
    def __iter__(self):
        return self.child_nodes.__iter__()

    def __eq__(self,other):
        """Test if two nodes are equal."""
        #if the nodes aren't equal, the respective toolkits should handle overloading this operator
        if self.node != other.node:
            return False

    def __ne__(self,other):
        """Test if two nodes are not equal."""
        return not self == other

    def get(self,attribute):
        return self.get_attribute(attribute)

    def set(self,attribute,value):
        self.set_attribute(attribute,value)

    def getparent(self):
        return self.parent
    
    def getnext(self):
        return self.parent.child_nodes[(self.parent.child_nodes.index(self)+1) % (len(self.parent.child_nodes))]

    def getprevious(self):
        return self.parent.child_nodes[self.parent.child_nodes.index(self)-1]
        
    def append(self,node):
        """Add a child node. This method is supported by the api specific append_node method."""
        #call the API specific append
        self.append_node(node.node)

        #assign the parent
        node.parent = self
        
        #keep it a list of child nodes
        self.child_nodes.append(node)
