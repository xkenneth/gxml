### MODULE IMPORTS ###
from base import tag_node
from helper import assemble

### LIBRARY IMPORTS ###
import elementtree.ElementTree as et

def Element(tag,**kwargs):
    return elemtree(et.Element(tag),**kwargs)

def to_string(node):
    return et.tostring(node.node)

def from_string(xml_str):
    t = elemtree()
    return assemble(t,elemtree)

class elemtree(tag_node):
    """An abstract XML API for elementetree"""

    def __repr__(self):
        try:
            return "<%s/>" % self.tag
        except AttributeError:
            return "gXML instance(elemtree)"

    tail = property( lambda obj: obj.node.tail )

    def from_string(self,xml_str):
        """Parse a string."""
        self.node = et.fromstring(xml_str)
        
        
        return self
    
    def parse(self,file_object):
        """Parse a file object."""
        t = et.parse(file_object)

        self.node = t.getroot()
        
        assemble(self,self.__class__)

        return self
    
    def get_child_nodes(self):
        """Return the child_nodes."""

        children = []
        #find them
        for child in self.node.getchildren():
            children.append(child)

        return children

    keys = property( lambda obj: obj.node.keys )
    
    #the tag of the node
    tag = property( lambda obj: obj.node.tag )

    #get an attribute
    get_attribute = property( lambda obj: obj.node.get )

    #set an attribute
    set_attribute = property( lambda obj: obj.node.set )

    def remove_attr(self,attribute):
        """Remove an attribute."""
        return self.node.attrib.pop(attribute)

    def set_text(self,text):
        self.node.text = text

    #get the nodes text
    text = property( lambda obj: obj.node.text , set_text)

    def append_node(self,node):
        """Append a child node."""
        #append the node to the elementree instance
        self.node.append(node)

if __name__ == '__main__':
    import pdb

    t = elemtree()
    t.parse('test.xml')

    pdb.set_trace()

        
