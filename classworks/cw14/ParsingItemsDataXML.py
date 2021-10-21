import xml.etree.ElementTree as Et

tree = Et.parse('ItemsData.xml')

# the root gets the content of <data> tag
root = tree.getroot()

# the child is each <country> tag content
for elem in root:
    for subroot in elem:
        print("subroot is: ", subroot)
        print("subroot.text is: ", subroot.text)
        print("subroot.tag is: ", subroot.tag)
        print("subroot.attrib is: ", subroot.attrib)
        print("elem.text is: ", elem.text)

print("root[0][1] is: ", root[0][1])
print("root[0][1].text is: ", root[0][1].text)
