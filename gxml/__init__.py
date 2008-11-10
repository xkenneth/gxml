#gxml will be the api we want to use
gxml = None

import base

#keep track of the available apis
available_apis = []

#apis in order of "awesomeness" 

#attempt to import minidom first
try:
    import xml.dom.minidom
    import minidom
    #define it's api
    gxml = minidom.minidom
    #list it as an available api
    Element = minidom.Element
    to_string = minidom.to_string
    from_string = minidom.from_string
    available_apis.append(['minidom',minidom])
except ImportError:
    pass

try:
   import elementtree
   import elemtree
   gxml = elemtree.elemtree
   Element = elemtree.Element
   to_string = elemtree.to_string
   from_string = elemtree.from_string
   available_apis.append(['elementtree',elemtree])
except ImportError:
   pass

if not gxml:
    raise ImportError("No Supported XML library found!")

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

            


        

