#gxml will be the api we want to use
gxml = None

import base

#keep track of the available apis
available_apis = []

#apis in order of "awesomeness" 
try:
   import elementtree
   import elemtree
   
   class gxml(elemtree.elemtree):
      __api__ = elemtree.elemtree
   to_string = elemtree.to_string

   available_apis.append(['elementtree',elemtree])
except ImportError:
   pass

try:
    import xml.dom.minidom
    import minidom
    #define it's api
    class gxml(minidom.minidom):
        __api__ = minidom.minidom
    #list it as an available api
    to_string = minidom.to_string
    available_apis.append(['minidom',minidom])

except ImportError:
    pass



if not gxml:
    raise ImportError("No Supported XML library found!")

ElementTree = gxml

def Element(tag):
    t = gxml()
    t.from_string(tag)
    return t

def from_string(xml_str):
    t = gxml()
    t.from_string(xml_str)
    return t


def clone(node):
    t = gxml()
    return t.from_string(to_string(node))

def preference(pref_list):
    global gxml, Element, to_string
    
    if not isinstance(pref_list,list):
        pref_list = [pref_list]

    """Selects a gxml sub-api by preference."""
    for preferred in pref_list:
        for name, api in available_apis:
            if preferred == name:
                return api
    return gxml

def is_element(element):
    return hasattr(element,'node') or isinstance(element,base.node)    

            


        

