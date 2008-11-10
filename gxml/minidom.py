import xml.dom.minidom
from base import tag_node
import pdb

def is_junk(node):
    """Lets us know if this is a node we don't want to work with."""
    if node.nodeName == u'#text' or node.nodeName == u'#comment' or node.nodeName == u'#cdata-section':
        return True

def Element(tag):
    """Creates an element with given tag."""
    return minidom(xml.dom.minidom.parseString("<%s/>"%tag).childNodes[0])

def to_string(node,pretty_print=False):
    """Turns an element tree into a string."""
    if pretty_print:
        return node.node.toprettyxml()

    return str(node.node.toxml())

def from_string(xml_str):
    t = minidom()
    return t.from_string(xml_str)

class minidom(tag_node):
    # def __repr__(self):
#         try:
#             return "<%s>" % self.node.nodeName
#         except AttributeError:
#             return 'gxml instance'
        
#         return self.__repr__()
        
    def from_string(self,xml_str):
        """Parse a string."""
        self.node = xml.dom.minidom.parseString(xml_str).childNodes[0]
        
        return self

    def parse(self,file_object):
        """Parse a file object."""
        
        #parse it
        self.node = xml.dom.minidom.parse(file_object).childNodes[0]

        return self
    
    def get_child_nodes(self):
        """Returns the child nodes of an object."""
        #if they haven't changed since last time
        if not self._child_nodes_changed:
            return self.children
        
        #if they have or we've never asked for them before
        children = []
        #find them
        for child in self.node.childNodes:
            if not is_junk(child):
                children.append(minidom(child,self))

        #save them
        self.children = children

        #mark false until dirtied
        self._child_nodes_changed = False
        
        return self.children
    
    child_nodes = property(get_child_nodes)

    keys = property( lambda obj: obj.node.attributes.keys )

    def get_tag(self):
        """Get the nodes tag."""
        return str(self.node.nodeName)

    tag = property(get_tag)

    def get(self,attribute):
        """Get the value of an attribute."""
        val = self.node.getAttribute(attribute)

        if val == '': 
            return None

        return str(val)

    def set(self,attribute,value):
        """Set the value of an attribute."""
        self.node.setAttribute(attribute,value)

    def remove_attr(self,attribute):
        """Remove an attribute."""
        save = self.get(attribute)
        self.node.removeAttribute(attribute)
        return str(save)
    
    def get_tail(self):
        if self.node.childNodes[-1].nodeName == u'#text' and self.node.childNodes[0] != self.node.childNodes[-1]:
            return str(self.node.childNodes[-1].wholeText)

    tail = property(get_tail)
            

    def get_text(self):
        """Get the nodes text."""
        
        return str(self.node.childNodes[0].wholeText)
    
    def set_text(self,text):
        """Set the text of the given node."""
        try:
            #try to see if a text node is already there, and set it
            if self.node.childNodes[0].nodeName == u'#text':
                self.node.childNodes[0].data = unicode(text)
                return
        except IndexError:
            pass

        #if not, let's make one
        t = minidom()
        t.from_string("<a>%s</a>" % text)
        
        text_node = t.node.childNodes[0]
        
        #now we need to see if the target node has more than one child
        if len(self.node.childNodes) == 0:
            #if not just append it
            self.node.appendChild(text_node)
        else:
            #else we need to insert it infront of the current node
            self.node.insertBefore(text_node,self.node.childNodes[0])
        
    text = property(get_text,set_text)

    def append(self,node):
        """Append a child node."""
        #append the child
        self.node.appendChild(node.node)

        #mark it as dirty
        self._child_nodes_changed = True
        

if __name__ == '__main__':
    import pdb

    t = minidom()
    t.parse('test.xml')
    
    pdb.set_trace()
