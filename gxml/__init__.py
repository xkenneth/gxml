#gxml will be the api we want to use
gxml = None

import base

#keep track of the available apis
available_apis = []

#apis in order of "awesomeness" 
try:
    import xml.dom.minidom
    import minidom
    #define it's api
    class gxml(minidom.minidom):
        __api__ = minidom.minidom
    #list it as an available api
    to_string = minidom.to_string
    available_apis.append(['minidom',minidom])
    Element = minidom.Element

except ImportError:
    pass

try:
   import elementtree
   import elemtree
   
   class gxml(elemtree.elemtree):
      __api__ = elemtree.elemtree

   to_string = elemtree.to_string

   available_apis.append(['elementtree',elemtree])

   Element = elemtree.Element

except ImportError:
   pass



if not gxml:
    raise ImportError("No Supported XML library found!")

def from_string(xml_str):
    t = gxml()
    t.from_string(xml_str)
    return t

XML = from_string

def clone(node):
    t = gxml()
    return t.from_string(to_string(node))

def is_element(element):
    return hasattr(element,'node') or isinstance(element,base.node)    

def SubElement(parent, child_tag):
    """Create a SubElement of child_tag and append it to the parent."""
    #create the child
    t = Element(child_tag)
    #append it to the parent
    parent.append(t)
    #return the child
    return t

def parse(file_like):
    t = gxml()
    return t.parse(file_like)




        

