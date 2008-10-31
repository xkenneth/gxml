import unittest
import gxml

test_suite = unittest.TestSuite()

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
            print self.dom

    class APICreateTestCase:
        def setUp(self):
            self.a = self.module.Element('a')

        def test_create(self):
            self.failUnlessEqual('a',self.module.Element('a').tag)

        def test_append(self):
            a = self.module.Element('a')
            b = self.module.Element('b')
            a.append(b)
            
            self.failUnlessEqual(a.child_nodes[0].tag,'b')

        def test_print(self):
            a = self.module.Element('a')
            self.module.tostring(a)

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
            
            
    exec("class %sParseTestCase(APIParseTestCase,unittest.TestCase): pass" % name)
    exec("%sParseTestCase.api = %s" % (name, api.__name__ + "." + api.__name__.split('.')[-1]))
    exec("%sParseTestCase.module = api" % name)

    exec("class %sCreateTestCase(APICreateTestCase,unittest.TestCase): pass" % name)
    exec("%sCreateTestCase.api = %s" % (name, api.__name__ + "." + api.__name__.split('.')[-1]))
    exec("%sCreateTestCase.module = api" % name)

    

    #test_suite.addTest(APITestCase('test_get_root_tag'))
    #test_suite.addTest(APITestCase('test_root_child_tags'))
    #test_suite.addTest(APITestCase('test_this'))

unittest.main()

