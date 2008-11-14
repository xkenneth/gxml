import unittest
import gxml
import new

first = True

for name, api in gxml.available_apis:
    
    print "Setting up %s tests" % name

    class APIParseTestCase:
        def setUp(self):
            self.dom = self.api()
            self.dom.parse('test.xml')
            
        def test_get_root_tag(self):
            self.failUnlessEqual('base',self.dom.tag)

        def test_root_child_tags(self):
            correct_tag_names = ['a','b','d']
            tag_names = []
            for child in self.dom.child_nodes:
                tag_names.append(child.tag)

            self.failUnlessEqual(tag_names,correct_tag_names)

        def test_a_attr(self):
            self.failUnlessEqual(self.dom.child_nodes[0].get('this'),'that')
            
        def test_d_text(self):
            self.failUnlessEqual(self.dom.child_nodes[-1].text,'\n    Hello!\n  ')
            
        def test_parse_string(self):
            self.failUnlessEqual(self.api().from_string("<a/>").tag,'a')

        def test_basic_xpath(self):
            pass

        def test_get_next(self):
            self.failUnless(self.dom.child_nodes[0].getnext() is self.dom.child_nodes[1])
            self.failUnless(self.dom.child_nodes[1].getnext() is self.dom.child_nodes[2])
            self.failUnless(self.dom.child_nodes[2].getnext() is self.dom.child_nodes[0])

        def test_get_next(self):
            self.failUnless(self.dom.child_nodes[2].getnext() is self.dom.child_nodes[0])
            self.failUnless(self.dom.child_nodes[1].getnext() is self.dom.child_nodes[2])
            self.failUnless(self.dom.child_nodes[0].getnext() is self.dom.child_nodes[1])

    class APICreateTestCase:
        def setUp(self):
            self.a = self.module.Element('a')

        def test_create(self):
            self.failUnlessEqual('a',self.module.Element('a').tag)
        
        def test_get_parent(self):
            test_node_a = self.module.Element('a')
            test_node_b = self.module.Element('b')
            test_node_a.append(test_node_b)
            self.failUnless(test_node_b.parent is test_node_a)
            self.failUnless(test_node_b.getparent() is test_node_a)

        def test_create_with_attributes(self):
            test_node = self.module.Element('a',awesome=True)
            self.failUnless(test_node.get('awesome'))
            
        def test_create_text(self):
            test_node = self.module.Element('a')
            test_node.text = "Ello!"
            self.failUnlessEqual(test_node.text,"Ello!")
            self.module.to_string(test_node)

        def test_append(self):
            a = self.module.Element('a')
            b = self.module.Element('b')
            a.append(b)
            
            self.failUnlessEqual(a.child_nodes[0].tag,'b')

        def test_print(self):
            a = self.module.Element('a')
            self.module.to_string(a)

        def test_assign_text(self):
            #try assiging it to a new element
            a = self.module.Element('a')
            a.text = 'Hello'
            self.failUnlessEqual(a.text,'Hello')

            #try reassigning it
            a.text = 'Hello2'
            self.failUnlessEqual(a.text,'Hello2')
            
            #try assigning it to a child
            b = self.module.Element('b')
            a.append(b)
            b.text = 'Hello'
            self.failUnlessEqual('Hello',a.child_nodes[0].text)
            
            #now try reassigning it now that we have a child
            a.text = 'last'
            self.failUnlessEqual('last',a.text)

        def test_assign_attribute(self):
            self.a.set('this','that')
            self.failUnlessEqual(self.a.get('this'),'that')

        def test_remove_attribute(self):
            self.a.set('this','that')
            self.a.remove_attr('this')
            self.failUnlessEqual(self.a.get('this'),None)

        def test_get_keys(self):
            self.a.set('this','that')
            self.a.set('a','b')
            self.failUnlessEqual(self.a.keys(),['this','a'])
            
            
    test_case_name = '%sParseTestCase' % name
    locals()[test_case_name] = new.classobj(test_case_name, (APIParseTestCase, unittest.TestCase), {})
    locals()[test_case_name].api = getattr(api,api.__name__.split('.')[-1])
    locals()[test_case_name].module = api

    test_case_name = '%sCreateTestCase' % name
    locals()[test_case_name] = new.classobj(test_case_name, (APICreateTestCase, unittest.TestCase), {})
    locals()[test_case_name].api = getattr(api,api.__name__.split('.')[-1])
    locals()[test_case_name].module = api

unittest.main()

