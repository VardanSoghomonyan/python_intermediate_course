import xml.etree.ElementTree as Et

p = Et.Element('parent')

c = Et.SubElement(p, 'child1')
d = Et.SubElement(c, 'child2')
e = Et.SubElement(c, 'child3')
f = Et.SubElement(c, 'child4')

c.set('child1_name', 'Child1')
c.text = 'This is Child1'

d.set('child2_name', 'Child2')
d.text = 'This is Child2'
Et.dump(p)

tree = Et.ElementTree(p)
tree.write('XMLCreatedByCode.xml', xml_declaration=True)

comment = Et.Comment('Added comment')
p.append(comment)

e.set('child3_name', 'Child3')
e.text = 'This is Child3'

Et.dump(p)
tree.write('XMLCreatedByCode.xml')

tree = Et.parse('XMLCreatedByCode.xml')

# the root gets the content of <parent> tag
root = tree.getroot()

# the child is each <country> tag content
for child in root:
    print("child.tag, child.attrib is: ", child.tag, child.attrib)
