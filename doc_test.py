def test_gxml():
    """
    >>> import gxml
    
    Creating a basic element.
    >>> node_a = gxml.Element('a')
    >>> node_a
    <a/>

    Printing it out in XML.
    >>> print(gxml.to_string(node_a))
    <a />

    Accessing the objects tag.
    >>> print(node_a.tag)
    a

    Adding SubElements
    >>> node_b = gxml.SubElement(node_a,'b')
    >>> node_b
    <b/>
    
    Attribute Access
    >>> node_a.set('this','that')
    >>> print(node_a.get('this'))
    that

    Creating a node with attributes
    >>> test_node = gxml.Element('a',this='is',awesome='True')
    >>> print(test_node.get('this'))
    is
    >>> print(test_node.get('awesome'))
    True
    
    Adding a child node:
    >>> node_c = gxml.Element('c')
    >>> node_a.append(node_c)

    Let's check out our tree.
    >>> print(gxml.to_string(node_a))
    <a this="that"><b /><c /></a>

    Elements are lists!
    >>> print len(node_a)
    2
    
    >>> for child in node_a:
    ...     print child
    <b/>
    <c/>

    Accessing child nodes:
    >>> node_a.child_nodes
    [<b/>, <c/>]

    Accessing child nodes by index:
    >>> node_a[0]
    <b/>

    Accessing a child's parent.
    >>> node_a[0].parent
    <a/>
    >>> node_a[0].getparent()
    <a/>

    Accessing the next child.
    >>> node_a[0].getnext() is node_a[1]
    True

    Accessing the previous child.
    >>> node_a[0].getprevious() is node_a[-1]
    True

    Working with text.
    >>> test_node = gxml.Element('a')
    >>> test_node.text = "Hello world!"
    >>> print(gxml.to_string(test_node))
    <a>Hello world!</a>

    Parsing from a string.
    >>> test_node = gxml.from_string("<a/>")
    >>> test_node
    <a/>

    >>> test_node = gxml.XML("<a/>")
    >>> test_node
    <a/>

    Parsing from a file.
    >>> test_node = gxml.parse('test.xml')
    >>> print(gxml.to_string(test_node))
    <base>
      <a this="that">
        <c>
        </c>
      </a>
      <b />
      <d>
        Hello!
      </d>
    </base>

    Accessing the different APIs
    You can get a list of the system detected APIs by importing
    import the available_apis
    >>> from gxml import available_apis
    >>> available_apis
    [['minidom', <module 'gxml.minidom' from '/Users/xkenneth/work/gxml/gxml/minidom.pyc'>], ['elementtree', <module 'gxml.elemtree' from '/Users/xkenneth/work/gxml/gxml/elemtree.pyc'>]]
    
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
