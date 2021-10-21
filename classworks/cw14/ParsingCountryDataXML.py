import xml.etree.ElementTree as Et

tree = Et.parse('CountryData.xml')

# the root gets the content of <data> tag
root = tree.getroot()

# the child is each <country> tag content
for child in root:
    print("child.tag, child.attrib is: ", child.tag, child.attrib)

print("root[0][1] is: ", root[0][1])
print("root[0][1].text is: ", root[0][1].text)
