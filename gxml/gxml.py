#gxml will be the api we want to use
gxml = None

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
    tostring = minidom.tostring
    available_apis.append(minidom)
except ImportError:
    pass

try:
    import elementtree
    import elemtree
    gxml = elemtree.elemtree
    Element = elemtree.Element
    tostring = elemtree.tostring
    available_apis.append(elemtree)
except ImportError:
    pass

if not gxml:
    raise ImportError("No Supported XML library found!")

def clone(node):
    t = gxml()
    return t.from_string(tostring(node))
