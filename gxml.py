import unittest
from copy import copy

import pdb

class gxml:
    def __init__(self):
        try:
            import xml.dom.minidom
            
            #parse function -> _parse function
            self._parse = xml.dom.minidom.parse

            #parsestring function -> _parse_string function
            self._parse_string = xml.dom.minidom.parseString

            #childNodes function -> _child_nodes PROPERTY
            self._child_nodes = "self.dom.childNodes"

            #nodeName function -> _node_name PROPERTY
            #self._node_name = """self.dom.nodeName"""
            self._node_name = "self.dom.nodeName"
            
            
            return
            
        except ImportError:
            
            print "Could not find minidom!"
        
        raise Exception("NO XML MODULE FOUND!!!")

    def __repr__(self):
        """Makes the class a little more intelligent work with."""
        return "<%s>" % self.node_name

    def new(self,dom=None,parent=None):
        """Clone a new gxml instance."""
        
        #we need to clone this node in order to keep all of the functions we assigned without
        #having to explicitly reassign them
        t = copy(self)

        if dom:
            t.dom = dom
            
        if parent:
            t.parent = self

        return t

    def parse(self,*args,**kwargs):
        """Parse a file or stream."""

        self.dom = self._parse(*args,**kwargs)

        return self

    def parse_string(self,*args,**kwargs):
        """Parse a string."""
        
        self.dom = self._parse_string(*args,**kwargs)

        return self

    def get_child_nodes(self):
        #create a new child array
        children = []

        #get the child nodes
        for child in eval(self._child_nodes):

            #wrap them in a new class instance and link to the parent
            children.append(self.new(child,self))

        return children
            
    child_nodes = property(get_child_nodes)

    def get_node_name(self):
        return eval(self._node_name)
    
    node_name = property(get_node_name)
    


    

if __name__ ==  '__main__':

    class GXMLTests(unittest.TestCase):
        def setUp(self):
            self.g = gxml()
            self.g.parse_string("""<node><a><b></b></a></node>""")

        def test_init(self):
            pass
            #print self.g
            #print self.g.dom
            
        def test_child_nodes(self):
            for child in self.g.child_nodes:
                print child, child.dom


    unittest.main()
