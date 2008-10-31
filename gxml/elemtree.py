### MODULE IMPORTS ###
from base import node

### LIBRARY IMPORTS ###
import elementtree.ElementTree as et

def Element(tag):
    return elemtree(et.Element(tag))

def to_string(node,pretty_print=False):
    return et.tostring(node.node,pretty_print)

def from_string(xml_str):
    t = elemtree()
    return t.from_string(xml_str)

class elemtree(node):
    """An abstract XML API for elementetree"""

    # def __repr__(self):
#         try:
#             return "<%s>" % self.tag
#         except AttributeError:
#             return "gXML instance(elemtree)"

    tail = property( lambda obj: obj.node.tail )

    def from_string(self,xml_str):
        """Parse a string."""
        self.node = et.fromstring(xml_str)
        
        return self
    
    def parse(self,file_object):
        """Parse a file object."""
        t = et.parse(file_object)

        self.node = t.getroot()
        
        return self
    
    def get_child_nodes(self):
        """Return the child_nodes."""

        #if they haven't changed since last time we asked for them
        if not self._child_nodes_changed:
            return self.children
        
        #if they have or if we've never asked for them before
        children = []
        #find them
        for child in self.node.getchildren():
            children.append(elemtree(child,self))

        #save them
        self.children = children
        
        #mark until dirtied
        self._child_nodes_changed = False

        return self.children

    #a list of the child nodes
    child_nodes = property(get_child_nodes)

    keys = property( lambda obj: obj.node.keys )
    
    #the tag of the node
    tag = property( lambda obj: obj.node.tag )

    #get an attribute
    get = property( lambda obj: obj.node.get )

    #set an attribute
    set = property( lambda obj: obj.node.set )

    def remove_attr(self,attribute):
        """Remove an attribute."""
        return self.node.attrib.pop(attribute)

    def set_text(self,text):
        self.node.text = text

    #get the nodes text
    text = property( lambda obj: obj.node.text , set_text)

    def append(self,node):
        """Append a child node."""
        #append the node to the elementree instance
        self.node.append(node.node)
        #mark the child_nodes as dirty
        self._child_nodes_changed = True

        return self

if __name__ == '__main__':
    import pdb

    t = elemtree()
    t.parse('test.xml')

    pdb.set_trace()

        
